const fs = require('fs');
const path = require('path');

const dir = 'c:/Users/Sai chandra Mouli/Desktop/Website';
const files = ['ai-model-training.html', 'aiml-tech-services.html', 'enterprise-ai-agents.html'];

for (const file of files) {
    const fullPath = path.join(dir, file);
    let content = fs.readFileSync(fullPath, 'utf8');
    let original = content;

    // Update JS array for Copilots
    content = content.replace(
        '{ name: "Enterprise AI Copilots", url: "enterprise-ai-copilots.html" }',
        '{ name: "Enterprise AI Copilots", url: "#enterprise-ai-copilots-section" }'
    );
    
    // Also update JS for Enterprise AI Agents to point to `#enterprise-ai-copilots-section` in other files?
    // Wait, if it's on ai-model-training.html, the URL should be `enterprise-ai-agents.html#enterprise-ai-copilots-section`.
    if (file === 'enterprise-ai-agents.html') {
        content = content.replace(
            '{ name: "Enterprise AI Copilots", url: "enterprise-ai-copilots.html" }',
            '{ name: "Enterprise AI Copilots", url: "#enterprise-ai-copilots-section" }'
        );
    } else {
        content = content.replace(
            '{ name: "Enterprise AI Copilots", url: "enterprise-ai-copilots.html" }',
            '{ name: "Enterprise AI Copilots", url: "enterprise-ai-agents.html#enterprise-ai-copilots-section" }'
        );
    }

    if (content !== original) {
        fs.writeFileSync(fullPath, content);
        console.log('Updated JS in ' + file);
    }
}
