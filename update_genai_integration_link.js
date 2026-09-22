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
            /<a href="genai-integration-modernization\.html">/g,
            '<a href="#genai-integration-modernization-section">'
        );
        content = content.replace(
            /<li><a href="genai-integration-modernization\.html">/g,
            '<li><a href="#genai-integration-modernization-section">'
        );
        // Also update JS array
        content = content.replace(
            '{ name: "GenAI Integration & Modernization", url: "genai-integration-modernization.html" }',
            '{ name: "GenAI Integration & Modernization", url: "#genai-integration-modernization-section" }'
        );
    } else {
        content = content.replace(
            /<a href="genai-integration-modernization\.html">/g,
            '<a href="enterprise-ai-agents.html#genai-integration-modernization-section">'
        );
        // Also update JS array
        content = content.replace(
            '{ name: "GenAI Integration & Modernization", url: "genai-integration-modernization.html" }',
            '{ name: "GenAI Integration & Modernization", url: "enterprise-ai-agents.html#genai-integration-modernization-section" }'
        );
    }

    if (content !== original) {
        fs.writeFileSync(fullPath, content);
        console.log('Updated links in ' + file);
    }
}
