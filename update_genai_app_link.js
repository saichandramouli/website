const fs = require('fs');
const path = require('path');

const dir = 'c:/Users/Sai chandra Mouli/Desktop/Website';
const files = ['ai-model-training.html', 'aiml-tech-services.html', 'enterprise-ai-agents.html'];

for (const file of files) {
    const fullPath = path.join(dir, file);
    let content = fs.readFileSync(fullPath, 'utf8');
    let original = content;

    // Update HTML links
    if (file === 'enterprise-ai-agents.html') {
        content = content.replace(
            /<a href="enterprise-genai-app-development\.html">/g,
            '<a href="#enterprise-genai-app-development-section">'
        );
        content = content.replace(
            /<li><a href="enterprise-genai-app-development\.html">/g,
            '<li><a href="#enterprise-genai-app-development-section">'
        );
        // Also update JS array
        content = content.replace(
            '{ name: "Enterprise GenAI Application Development", url: "enterprise-genai-app-development.html" }',
            '{ name: "Enterprise GenAI Application Development", url: "#enterprise-genai-app-development-section" }'
        );
    } else {
        content = content.replace(
            /<a href="enterprise-genai-app-development\.html">/g,
            '<a href="enterprise-ai-agents.html#enterprise-genai-app-development-section">'
        );
        // Also update JS array
        content = content.replace(
            '{ name: "Enterprise GenAI Application Development", url: "enterprise-genai-app-development.html" }',
            '{ name: "Enterprise GenAI Application Development", url: "enterprise-ai-agents.html#enterprise-genai-app-development-section" }'
        );
    }

    if (content !== original) {
        fs.writeFileSync(fullPath, content);
        console.log('Updated links in ' + file);
    }
}
