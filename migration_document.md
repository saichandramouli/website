# People Remotely — Master Migration Document
### Next.js + Supabase → React + Django REST Framework + PostgreSQL + Celery + Redis + AWS S3

---

## 1. Executive Summary

[CONFIRMED] **People Remotely** is an AI-assisted hiring marketplace for US remote tech roles built by People Prime Worldwide. It connects employers who post jobs with candidates who build skill profiles; a recruiter team (People Prime) operates as the human-in-the-loop that reviews AI-generated matches before releasing them to employers. When both sides express interest, a "handoff" is triggered and People Prime coordinates the introduction.

**The migration target** is a decoupled architecture: a React/Vite SPA calling a Django REST Framework API backed by PostgreSQL, with Celery/Redis for async work (matching, email), and AWS S3 for file storage.

---

## 2. Current Architecture

[CONFIRMED]

```
Browser
  │
  ▼
Next.js 16 (App Router, SSR + Server Components)
  │  ├── Public marketing pages  (SSR + dynamic imports)
  │  ├── Employer portal (/employer/*)
  │  ├── Candidate portal (/candidate/*)
  │  ├── Admin portal (/admin/*)
  │  ├── Auth pages (/auth/*)
  │  └── API Route Handlers (/api/*)
  │
  ├── Supabase Auth         (Email + Google OAuth sessions via cookies)
  ├── Supabase PostgreSQL   (All application data)
  ├── Supabase Storage      (resumes bucket, company-logos bucket)
  ├── OpenAI API            (gpt-4o-mini — LLM match reasons + JD parsing)
  ├── Resend API            (transactional ops email)
  └── OpenWeb Ninja API     (external job lead search)

Hosting: Vercel (Next.js)
Database: Supabase managed PostgreSQL
```

---

## 3. Current Technology Stack

[CONFIRMED]

| Layer | Technology | Version |
|---|---|---|
| Framework | Next.js App Router | 16.2.9 |
| UI Library | React | 19.2.4 |
| Language | TypeScript | ^5 |
| Styling | Tailwind CSS | ^4 |
| Auth | @supabase/ssr + @supabase/supabase-js | ^0.12 / ^2.108 |
| Database | Supabase PostgreSQL | hosted |
| Storage | Supabase Storage | hosted |
| Email | Resend | REST API |
| AI | OpenAI API (gpt-4o-mini) | REST API |
| Job Leads | OpenWeb Ninja (JSearch) | REST API |
| File Parsing | xlsx | ^0.18 |
| Hosting | Vercel | — |

---

## 4. Complete Repository Map

[CONFIRMED]

```
primescale/
├── next.config.ts                      # Minimal Next.js config, optimizePackageImports
├── package.json                        # Dependencies: next, react, supabase, openai, xlsx
├── supabase/                           # SQL migration files
│   ├── marketplace-schema.sql          # Core tables: profiles, companies, jobs, matches
│   ├── employer-module.sql             # Extended company fields, company_members, storage buckets
│   ├── candidate-profile-v2.sql        # Extended candidate_profiles + resumes bucket
│   ├── handoff-queue.sql               # handoff_requests table + is_admin() function + RLS
│   ├── match-review.sql                # visible_to_employer + recruiter_notified_at columns
│   └── candidates-admin-views.sql      # candidates_overview + candidate_applications views
└── src/
    ├── middleware.ts                    # Route protection: /employer, /candidate, /admin
    ├── app/                            # App Router pages & API routes
    │   ├── api/                        # REST API handlers
    │   ├── auth/                       # Auth pages (login, signup, callback, redirect)
    │   ├── employer/                   # Employer portal
    │   ├── candidate/                  # Candidate portal
    │   └── admin/                      # Admin portal
    ├── components/                     # UI components (site, auth, candidate, employer, admin)
    └── lib/                            # Business logic (matching, runner, alerts, email, auth, supabase)
```

---

## 5. Route Map

[CONFIRMED]

| Route | Purpose | User Type | Auth Required | Key DB Tables |
|---|---|---|---|---|
| `/` | Marketing homepage | Public | No | candidate_profiles |
| `/auth/employer/signup` | Employer registration | Employer | No | — |
| `/auth/employer/login` | Employer login | Employer | No | profiles |
| `/auth/candidate/signup` | Candidate registration | Candidate | No | — |
| `/auth/candidate/login` | Candidate login | Candidate | No | profiles |
| `/auth/callback` | OAuth PKCE exchange | All | No | profiles |
| `/auth/redirect` | Post-login role router | All | Yes | profiles, companies, candidate_profiles |
| `/employer` | Employer dashboard | Employer | Yes | companies, jobs, matches |
| `/employer/onboarding` | Company onboarding | Employer | Yes | companies |
| `/employer/company` | Edit company profile | Employer | Yes | companies |
| `/employer/jobs` | List employer's jobs | Employer | Yes | jobs |
| `/employer/jobs/new` | Create new job | Employer | Yes | companies |
| `/employer/matches` | View matched candidates | Employer | Yes | matches, candidate_profiles, profiles |
| `/candidate` | Candidate dashboard | Candidate | Yes | candidate_profiles, matches |
| `/candidate/onboarding` | Profile wizard | Candidate | Yes | candidate_profiles |
| `/candidate/profile` | Edit candidate profile | Candidate | Yes | candidate_profiles |
| `/candidate/matches` | View matched jobs | Candidate | Yes | matches, jobs |
| `/admin` | Admin dashboard + stats | Admin | Yes | matches, handoff_requests, profiles, jobs |
| `/admin/candidates` | Candidate registry | Admin | Yes | candidate_profiles, profiles |
| `/admin/candidates/import` | Bulk CSV/XLSX import | Admin | Yes | candidate_profiles, profiles |
| `/admin/jobs` | Job registry | Admin | Yes | jobs, companies |
| `/admin/matches` | Match review queue | Admin | Yes | matches, candidate_profiles, jobs |
| `/admin/handoffs` | Handoff queue | Admin | Yes | handoff_requests, matches |
| `/admin/job-leads` | External job leads browser | Admin | Yes | — |

---

## 6. Database Schema

[CONFIRMED]

- **`profiles`**: `id` (PK, FK auth.users), `role` (candidate/employer/admin), `full_name`, `email`, `phone`, `created_at`, `updated_at`
- **`companies`**: `id` (PK), `owner_id` (FK profiles, UNIQUE), `name`, `website`, `size`, `country`, `logo_url`, `description`, `hq_city`, `industry`, `remote_culture_statement`, `domain_verified`, `profile_complete`
- **`candidate_profiles`**: `id` (PK), `user_id` (FK profiles, UNIQUE), `headline`, `phone`, `current_title`, `years_experience`, `skills` (text[]), `role_categories` (text[]), `experience_level`, `salary_min`, `salary_max`, `work_authorization`, `us_state`, `preferred_work_type`, `resume_url`, `bio`, `availability_status`, `privacy_visibility`, `profile_completeness`, `open_to_matching`, `profile_complete`, `source`
- **`jobs`**: `id` (PK), `company_id` (FK companies), `posted_by` (FK profiles), `title`, `description`, `role_type`, `experience_level`, `tech_stack` (text[]), `salary_range`, `work_type`, `visa_requirements`, `status` (draft/active/paused/closed/archived), `expires_at`, `jd_quality_score`, `jd_quality_feedback`, `featured`
- **`matches`**: `id` (PK), `candidate_profile_id` (FK candidate_profiles), `job_id` (FK jobs), `match_score` (0-100), `match_reason`, `status` (suggested/candidate_interested/employer_shortlisted/mutual_fit/rejected), `visible_to_employer`, `recruiter_notified_at`. UNIQUE(candidate_profile_id, job_id)
- **`handoff_requests`**: `id` (PK), `match_id` (FK matches, UNIQUE), `status` (pending/contacted/intro_made/closed), `notes`, `notified_at`
- **`company_members`**: `id` (PK), `company_id` (FK companies), `user_id` (FK profiles), `member_role`. UNIQUE(company_id, user_id)

---

## 7. Matching Engine

[CONFIRMED]

$$\text{matchScore} = (\text{skillScore} \times 0.7) + (\text{experienceScore} \times 0.3)$$

1. **Skill Overlap Score**: Percentage of job required skills found in candidate skills (substring matching supported).
2. **Experience Score**: 100 if candidate level $\ge$ job level; 70 if one level below; 40 if 2+ levels below; 50 if unknown.
3. **Recruiter Alert Gate**: Score $\ge 85$ triggers an automatic Resend email to the ops team.
4. **LLM Match Reason**: Calls OpenAI `gpt-4o-mini` to generate a 1-sentence explanation stored in `matches.match_reason`.

---

## 8. Proposed Target Architecture (React + Django)

[PROPOSED]

- **Frontend**: React 18+ (Vite) + React Router v6 + TanStack Query + Axios
- **Backend**: Django REST Framework + PostgreSQL
- **Authentication**: SimpleJWT (`djangorestframework-simplejwt`) + Google OAuth (`django-allauth`)
- **Async Processing**: Celery + Redis for match scoring, email alerts, and bulk candidate imports
- **File Storage**: AWS S3 (`django-storages` + `boto3`) with 1-hour presigned URLs for resumes and public access for logos

---

## 9. Migration Risks & Recommendations

[CONFIRMED / PROPOSED]

1. **Password Migration (CRITICAL)**: Supabase Auth bcrypt hashes are internal. Recommendation: Trigger forced password reset via email for all users upon cutover.
2. **Session Invalidation (HIGH)**: Users will be logged out upon cutover and need to log back in.
3. **OAuth Redirects (HIGH)**: Reconfigure Google OAuth application callback URLs to point to the Django API.
4. **Algorithm Precision (MEDIUM)**: Port `matching.ts` logic to Python with unit tests verifying identical output scores.
