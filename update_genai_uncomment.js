const fs = require('fs');
const path = require('path');

const dir = 'c:/Users/Sai chandra Mouli/Desktop/Website';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

const stringsToUncomment = [
    '<a href="enterprise-ai-copilots.html">Enterprise AI Copilots</a>',
    '<a href="document-intelligence-knowledge-ai.html">Document Intelligence &amp; Knowledge AI</a>',
    '<a href="conversational-ai-customer-service.html">Conversational AI / Customer Service AI</a>',
    '<a href="enterprise-genai-app-development.html">Enterprise GenAI Application Development</a>',
    '<a href="genai-integration-modernization.html">GenAI Integration &amp; Modernization</a>',
    '<li><a href="enterprise-ai-copilots.html">Enterprise AI Copilots</a></li>',
    '<li><a href="document-intelligence-knowledge-ai.html">Document Intelligence &amp; Knowledge AI</a></li>',
    '<li><a href="conversational-ai-customer-service.html">Conversational AI / Customer Service AI</a></li>',
    '<li><a href="enterprise-genai-app-development.html">Enterprise GenAI Application Development</a></li>',
    '<li><a href="genai-integration-modernization.html">GenAI Integration &amp; Modernization</a></li>'
];

let replacedCount = 0;

for (const file of files) {
    const fullPath = path.join(dir, file);
    let content = fs.readFileSync(fullPath, 'utf8');
    let original = content;

    for (const str of stringsToUncomment) {
        // We'll replace the commented version with the original string
        const commentedStr = `<!-- ${str} -->`;
        const parts = content.split(commentedStr);
        if (parts.length > 1) {
            content = parts.join(str);
        }
    }

    if (content !== original) {
        fs.writeFileSync(fullPath, content);
        replacedCount++;
        console.log('Updated ' + file);
    }
}

console.log(`Updated ${replacedCount} files`);
