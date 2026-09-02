// ===== HERO SLIDER & TEXT ROTATOR =====
const heroContainer = document.querySelector(".card-section");
if (heroContainer) {
  const slides = document.querySelectorAll(".hero-content");
  let currentSlideIndex = 0;

  function cycleHero() {
    const currentSlide = slides[currentSlideIndex];
    // Find all h1 tags that should rotate
    const rotatingTexts = currentSlide.querySelectorAll(".left-content h1.hero-text");

    if (rotatingTexts.length > 1) {
      let activeIndex = Array.from(rotatingTexts).findIndex(el => el.classList.contains("active"));
      if (activeIndex === -1) activeIndex = 0;

      const currentText = rotatingTexts[activeIndex];
      currentText.classList.remove("active");
      currentText.classList.add("exit");

      setTimeout(() => {
        currentText.classList.remove("exit");
        const nextIndex = (activeIndex + 1) % rotatingTexts.length;

        // If we've circled back to the first text AND there are multiple slides, move to next slide
        if (nextIndex === 0 && slides.length > 1) {
          currentSlideIndex = (currentSlideIndex + 1) % slides.length;
          heroContainer.scrollTo({
            left: currentSlideIndex * currentSlide.offsetWidth,
            behavior: "smooth"
          });
          // Ensure the first text of the new slide is active
          const nextSlideTexts = slides[currentSlideIndex].querySelectorAll(".left-content h1.hero-text");
          if (nextSlideTexts.length > 0) {
            nextSlideTexts.forEach(t => t.classList.remove("active", "exit"));
            nextSlideTexts[0].classList.add("active");
          }
        } else {
          rotatingTexts[nextIndex].classList.add("active");
        }
      }, 800);
    } else if (slides.length > 1) {
      // Just slide banners if no rotating text
      currentSlideIndex = (currentSlideIndex + 1) % slides.length;
      heroContainer.scrollTo({
        left: currentSlideIndex * currentSlide.offsetWidth,
        behavior: "smooth"
      });
    }
  }

  // Initialize: ensure only the first H1 is active in the current slide
  const initialTexts = slides[0].querySelectorAll(".left-content h1.hero-text");
  if (initialTexts.length > 1) {
    initialTexts.forEach((t, i) => {
      if (i === 0) t.classList.add("active");
      else t.classList.remove("active");
    });
  }

  setInterval(cycleHero, 4000);
}

// ===== SIX SECTION (SAFE) =====
const items = document.querySelectorAll(".six-item");

if (items.length > 0) {
  items.forEach((item) => {
    item.addEventListener("click", () => {
      items.forEach((i) => {
        if (i !== item) i.classList.remove("active");
      });
      item.classList.toggle("active");
    });
  });
}

// ===== NAVBAR DROPDOWN (FINAL FIXED) =====
const dropdowns = document.querySelectorAll(".dropdown");

if (dropdowns.length > 0) {
  dropdowns.forEach((drop) => {
    const trigger = drop.querySelector(":scope > a");

    if (trigger) {
      trigger.addEventListener("click", (e) => {
        if (trigger.getAttribute("href") === "javascript:void(0)" || trigger.getAttribute("href") === "#") {
          e.preventDefault();
        }
        e.stopPropagation();

        dropdowns.forEach((d) => {
          if (d !== drop) d.classList.remove("active");
        });

        drop.classList.toggle("active");
      });
    }
  });

  // click outside closes dropdown
  document.addEventListener("click", (e) => {
    if (!e.target.closest(".dropdown")) {
      dropdowns.forEach((d) => d.classList.remove("active"));
    }
  });
}

// ===== HAMBURGER / MOBILE DRAWER =====
const hamburger = document.getElementById("hamburger");
const mobileDrawer = document.getElementById("mobileDrawer");
const drawerOverlay = document.getElementById("drawerOverlay");
const drawerClose = document.getElementById("drawerClose");

function openDrawer() {
  if (mobileDrawer) mobileDrawer.classList.add("open");
  if (drawerOverlay) drawerOverlay.classList.add("open");
  document.body.style.overflow = "hidden";
}

function closeDrawer() {
  if (mobileDrawer) mobileDrawer.classList.remove("open");
  if (drawerOverlay) drawerOverlay.classList.remove("open");
  document.body.style.overflow = "";
}

if (hamburger) hamburger.addEventListener("click", openDrawer);
if (drawerClose) drawerClose.addEventListener("click", closeDrawer);
if (drawerOverlay) drawerOverlay.addEventListener("click", closeDrawer);

// Drawer accordion dropdowns
const drawerDropdowns = document.querySelectorAll(".drawer-dropdown");
if (drawerDropdowns.length > 0) {
  drawerDropdowns.forEach((dd) => {
    const btn = dd.querySelector(".drawer-dropdown-btn");
    if (btn) {
      btn.addEventListener("click", () => {
        drawerDropdowns.forEach((d) => {
          if (d !== dd) d.classList.remove("open");
        });
        dd.classList.toggle("open");
      });
    }
  });
}

// Drawer nested accordion dropdowns
const drawerNestedDropdowns = document.querySelectorAll(".drawer-nested-dropdown");
if (drawerNestedDropdowns.length > 0) {
  drawerNestedDropdowns.forEach((ndd) => {
    const btn = ndd.querySelector(".drawer-nested-btn");
    if (btn) {
      btn.addEventListener("click", (e) => {
        e.stopPropagation();
        drawerNestedDropdowns.forEach((d) => {
          if (d !== ndd) d.classList.remove("open");
        });
        ndd.classList.toggle("open");
      });
    }
  });
}

// Close drawer when any link inside is clicked
const drawerLinks = document.querySelectorAll(".mobile-drawer a");
if (drawerLinks.length > 0) {
  drawerLinks.forEach((link) => {
    link.addEventListener("click", closeDrawer);
  });
}

// ===== SCROLL TRIGGERED ANIMATIONS (HOW & HIRE SECTIONS) =====
const howSection = document.querySelector('.how-section');
const hireSection = document.querySelector('.hire-section');
const hireCards = document.querySelectorAll('.hire-section .card');

const aimlRevealElements = document.querySelectorAll('.aiml-reveal');

if ('IntersectionObserver' in window) {
  const scrollObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        if (entry.target.classList.contains('how-section')) {
          entry.target.classList.add('active');
          scrollObserver.unobserve(entry.target);
        }
        if (entry.target.classList.contains('hire-section')) {
          const half = Math.ceil(hireCards.length / 2);
          hireCards.forEach((card, index) => {
            if (index < half) {
              card.classList.add('animate-left');
            } else {
              card.classList.add('animate-right');
            }
          });
          scrollObserver.unobserve(entry.target);
        }
        if (entry.target.classList.contains('aiml-reveal')) {
          entry.target.classList.add('active');
          scrollObserver.unobserve(entry.target);
        }
      }
    });
  }, {
    threshold: 0.15,
    rootMargin: '0px 0px -40px 0px'
  });

  if (howSection) scrollObserver.observe(howSection);
  if (hireSection) scrollObserver.observe(hireSection);
  if (aimlRevealElements.length > 0) {
    aimlRevealElements.forEach(el => scrollObserver.observe(el));
  }
} else {
  const scrollHandler = () => {
    const triggerPoint = window.innerHeight * 0.85;
    if (howSection && howSection.getBoundingClientRect().top <= triggerPoint) {
      howSection.classList.add('active');
    }
    if (hireSection && hireSection.getBoundingClientRect().top <= triggerPoint) {
      const half = Math.ceil(hireCards.length / 2);
      hireCards.forEach((card, index) => {
        if (index < half) card.classList.add('animate-left');
        else card.classList.add('animate-right');
      });
    }
    if (aimlRevealElements.length > 0) {
      aimlRevealElements.forEach(el => {
        if (el.getBoundingClientRect().top <= triggerPoint) {
          el.classList.add('active');
        }
      });
    }
  };
  window.addEventListener('scroll', scrollHandler);
  scrollHandler();
}

// ===== TALENT BANNERS MODERN TRANSITION =====
const bannersWrapper = document.getElementById("bannersWrapper");
if (bannersWrapper) {
  const banners = bannersWrapper.querySelectorAll(".banner");
  let currentIndex = 0;
  let bannerInterval;
  let touchStartX = 0;
  let touchEndX = 0;

  function setBanner(index) {
    banners.forEach((banner, i) => {
      banner.classList.toggle("active", i === index);
    });
    currentIndex = index;
  }

  function nextBanner() {
    let nextIndex = (currentIndex + 1) % banners.length;
    setBanner(nextIndex);
  }

  function prevBanner() {
    let prevIndex = (currentIndex - 1 + banners.length) % banners.length;
    setBanner(prevIndex);
  }

  function startAutoSlide() {
    stopAutoSlide();
    bannerInterval = setInterval(nextBanner, 6000);
  }

  function stopAutoSlide() {
    if (bannerInterval) {
      clearInterval(bannerInterval);
      bannerInterval = null;
    }
  }

  function handleSwipe() {
    const swipeThreshold = 50;
    const diff = touchEndX - touchStartX;
    if (Math.abs(diff) > swipeThreshold) {
      if (diff > 0) prevBanner();
      else nextBanner();
    }
  }

  setBanner(0);
  startAutoSlide();

  bannersWrapper.addEventListener("touchstart", (e) => {
    touchStartX = e.changedTouches[0].screenX;
    stopAutoSlide();
  }, { passive: true });

  bannersWrapper.addEventListener("touchend", (e) => {
    touchEndX = e.changedTouches[0].screenX;
    handleSwipe();
    startAutoSlide();
  }, { passive: true });
}

// ===== BANNER NEURAL BACKGROUNDS (SAFE) =====
(function () {
  const canvases = document.querySelectorAll('.banner-bg-canvas');
  if (canvases.length === 0) return;

  canvases.forEach(canvas => {
    const ctx = canvas.getContext('2d');
    let W, H, nodes;

    function resize() {
      const rect = canvas.getBoundingClientRect();
      W = canvas.width = rect.width;
      H = canvas.height = rect.height;
      const count = W < 768 ? 35 : 65;
      nodes = Array.from({ length: count }, () => ({
        x: Math.random() * W,
        y: Math.random() * H,
        vx: (Math.random() - 0.5) * 0.6,
        vy: (Math.random() - 0.5) * 0.6,
        r: Math.random() * 2 + 1,
        pulse: Math.random() * Math.PI * 2
      }));
    }

    function draw(t) {
      if (!canvas.offsetParent) {
        requestAnimationFrame(draw);
        return;
      }
      ctx.clearRect(0, 0, W, H);
      ctx.fillStyle = '#050a1a';
      ctx.fillRect(0, 0, W, H);

      nodes.forEach(n => {
        n.x += n.vx;
        n.y += n.vy;
        n.pulse += 0.02;
        if (n.x < 0) n.x = W;
        if (n.x > W) n.x = 0;
        if (n.y < 0) n.y = H;
        if (n.y > H) n.y = 0;
      });

      for (let i = 0; i < nodes.length; i++) {
        for (let j = i + 1; j < nodes.length; j++) {
          const dx = nodes[i].x - nodes[j].x;
          const dy = nodes[i].y - nodes[j].y;
          const d = Math.sqrt(dx * dx + dy * dy);
          if (d < 150) {
            ctx.beginPath();
            ctx.moveTo(nodes[i].x, nodes[i].y);
            ctx.lineTo(nodes[j].x, nodes[j].y);
            const alpha = (1 - d / 150) * 0.3;
            ctx.strokeStyle = `rgba(0, 210, 255, ${alpha})`;
            ctx.lineWidth = 0.8;
            ctx.stroke();
          }
        }
      }

      nodes.forEach(n => {
        const pulse = 0.5 + Math.sin(n.pulse) * 0.5;
        ctx.beginPath();
        ctx.arc(n.x, n.y, n.r * 4, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(0, 255, 180, ${0.05 * pulse})`;
        ctx.fill();
        ctx.beginPath();
        ctx.arc(n.x, n.y, n.r, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(32, 255, 220, ${0.7 + 0.3 * pulse})`;
        ctx.fill();
      });

      const scanY = ((t * 0.0003) % 1.2) * H - (H * 0.1);
      const scanGrad = ctx.createLinearGradient(0, scanY - 50, 0, scanY + 50);
      scanGrad.addColorStop(0, 'transparent');
      scanGrad.addColorStop(0.5, 'rgba(0, 255, 230, 0.08)');
      scanGrad.addColorStop(1, 'transparent');
      ctx.fillStyle = scanGrad;
      ctx.fillRect(0, scanY - 50, W, 100);

      requestAnimationFrame(draw);
    }

    const resizeObserver = new ResizeObserver(() => resize());
    resizeObserver.observe(canvas.parentElement || document.body);
    resize();
    requestAnimationFrame(draw);
  });
})();
