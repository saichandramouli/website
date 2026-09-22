const fs = require('fs');
const path = require('path');

const dir = 'c:/Users/Sai chandra Mouli/Desktop/Website';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

const oldLink = '<a href="enterprise-ai-copilots.html">Enterprise AI Copilots</a>';
const newLink = '<a href="enterprise-ai-agents.html#enterprise-ai-copilots-section">Enterprise AI Copilots</a>';

let replacedCount = 0;

for (const file of files) {
    const fullPath = path.join(dir, file);
    let content = fs.readFileSync(fullPath, 'utf8');
    let original = content;

    content = content.split(oldLink).join(newLink);

    if (content !== original) {
        fs.writeFileSync(fullPath, content);
        replacedCount++;
        console.log('Updated ' + file);
    }
}
console.log(`Updated ${replacedCount} files`);
