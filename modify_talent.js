const fs = require('fs');

let content = fs.readFileSync('ai-ml-talent-services.html', 'utf8');

// Update Titles
content = content.replace(/<title>.*?<\/title>/s, '<title>AI/ML Talent Services | People Prime Worldwide</title>');
content = content.replace(/content="Enterprise AI Agents \| People Prime Worldwide"/g, 'content="AI/ML Talent Services | People Prime Worldwide"');
content = content.replace(/content="Build AI agents that understand requests.*?autonomous\."/s, 'content="Get specialized AI/ML talent, flexible talent access, and scalable teams for faster project delivery."');
content = content.replace(/<h1 class="agent-header-title">.*?<\/h1>/s, '<h1 class="agent-header-title">AI/ML Talent Services</h1>');

// Update Sidebar Menu
const sidebarRegex = /<ul class="agent-sidebar-list">.*?<\/ul>/s;
const newSidebar = `<ul class="agent-sidebar-list">
            <li class="active"><a href="#specialized-aiml-talent-section">Specialized AI/ML Talent</a></li>
            <li><a href="#flexible-talent-access-section">Flexible Talent Access</a></li>
            <li><a href="#scalable-aiml-teams-section">Scalable AI/ML Teams</a></li>
            <li><a href="#faster-project-delivery-section">Faster Project Delivery</a></li>
          </ul>`;
content = content.replace(sidebarRegex, newSidebar);

// Update Main Content
const mainContentRegex = /<div class="agent-content-area">.*?(?=<\/div>\s*<\/div>\s*<\/div>\s*<\/div>\s*<\/section>)/s;
const newMainContent = `<div class="agent-content-area">
          <h2 class="agent-main-heading">AI/ML Talent Services</h2>
          <p class="agent-subheading">Empowering your organization with top-tier AI/ML professionals.</p>
          <p class="agent-lead-text">Access specialized talent and build scalable teams to drive your AI innovation forward with flexibility and speed.</p>
          
          <!-- Specialized AI/ML Talent -->
          <div id="specialized-aiml-talent-section" class="agent-service-section">
            <h3 class="agent-features-section-title">Specialized AI/ML Talent</h3>
            <p>Access top-tier data scientists, ML engineers, and AI specialists to drive your innovation.</p>
          </div>

          <!-- Flexible Talent Access -->
          <div id="flexible-talent-access-section" class="agent-service-section">
            <h3 class="agent-features-section-title">Flexible Talent Access</h3>
            <p>Scale your team up or down based on your project needs with our flexible engagement models.</p>
          </div>

          <!-- Scalable AI/ML Teams -->
          <div id="scalable-aiml-teams-section" class="agent-service-section">
            <h3 class="agent-features-section-title">Scalable AI/ML Teams</h3>
            <p>Build comprehensive AI/ML teams equipped with the right mix of skills for end-to-end delivery.</p>
          </div>

          <!-- Faster Project Delivery -->
          <div id="faster-project-delivery-section" class="agent-service-section">
            <h3 class="agent-features-section-title">Faster Project Delivery</h3>
            <p>Accelerate your time-to-market by leveraging our pre-vetted pool of AI experts ready to contribute from day one.</p>
          </div>`;
content = content.replace(mainContentRegex, newMainContent);

// Also need to ensure links in nav point correctly to the same page if we had href="#something". 
// Actually, earlier I added a dropdown in all files:
// <a href="javascript:void(0)" class="nested-trigger">AI/ML Talent Services <span class="sub-arrow">▶</span></a>
// I should update this href in ALL files to point to ai-ml-talent-services.html, and the sub-items to point to the sections.

fs.writeFileSync('ai-ml-talent-services.html', content);
console.log('Successfully updated ai-ml-talent-services.html');
