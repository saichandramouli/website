const fs = require('fs');

const filePath = 'ai-ml-talent-services.html';
let content = fs.readFileSync(filePath, 'utf8');

const startMarker = '<section class="agent-content-area">';
const endMarker = '      </section>\n    </div>\n  </main>';

const startIdx = content.indexOf(startMarker);
const endIdx = content.indexOf(endMarker);

if (startIdx !== -1 && endIdx !== -1) {
    const newContent = `<section class="agent-content-area">
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
        </div>
`;
    content = content.substring(0, startIdx) + newContent + content.substring(endIdx);
    fs.writeFileSync(filePath, content);
    console.log("Content successfully replaced.");
} else {
    console.log("Markers not found.");
}
