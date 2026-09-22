const fs = require('fs');
const path = require('path');

const dir = 'c:/Users/Sai chandra Mouli/Desktop/Website';
const files = ['ai-model-training.html', 'aiml-tech-services.html', 'enterprise-ai-agents.html'];

const oldLinkStr = 'document-intelligence-knowledge-ai.html';

for (const file of files) {
    const fullPath = path.join(dir, file);
    let content = fs.readFileSync(fullPath, 'utf8');
    let original = content;

    // Update HTML links
    if (file === 'enterprise-ai-agents.html') {
        content = content.replace(
            /<a href="document-intelligence-knowledge-ai\.html">/g,
            '<a href="#document-intelligence-knowledge-ai-section">'
        );
        content = content.replace(
            /<li><a href="document-intelligence-knowledge-ai\.html">/g,
            '<li><a href="#document-intelligence-knowledge-ai-section">'
        );
        // Also update JS array
        content = content.replace(
            '{ name: "Document Intelligence & Knowledge AI", url: "document-intelligence-knowledge-ai.html" }',
            '{ name: "Document Intelligence & Knowledge AI", url: "#document-intelligence-knowledge-ai-section" }'
        );
    } else {
        content = content.replace(
            /<a href="document-intelligence-knowledge-ai\.html">/g,
            '<a href="enterprise-ai-agents.html#document-intelligence-knowledge-ai-section">'
        );
        // Also update JS array
        content = content.replace(
            '{ name: "Document Intelligence & Knowledge AI", url: "document-intelligence-knowledge-ai.html" }',
            '{ name: "Document Intelligence & Knowledge AI", url: "enterprise-ai-agents.html#document-intelligence-knowledge-ai-section" }'
        );
    }

    if (content !== original) {
        fs.writeFileSync(fullPath, content);
        console.log('Updated links in ' + file);
    }
}
