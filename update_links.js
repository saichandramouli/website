const fs = require('fs');
const path = require('path');

const dir = 'c:/Users/Sai chandra Mouli/Desktop/Website';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

let replaced = 0;

for (const file of files) {
    const fullPath = path.join(dir, file);
    let content = fs.readFileSync(fullPath, 'utf8');
    let changed = false;

    // AIML Engineering and MLOps
    const aimlPattern = /<a href="javascript:void\(0\)" class="nested-trigger">AIML Engineering and \s*MLOps <span/g;
    if (content.match(aimlPattern)) {
        content = content.replace(aimlPattern, '<a href="aiml-tech-services.html" class="nested-trigger">AIML Engineering and MLOps <span');
        changed = true;
    }

    // AIML Engineering and MLOps (without newline)
    const aimlPattern2 = /<a href="javascript:void\(0\)" class="nested-trigger">AIML Engineering and MLOps <span/g;
    if (content.match(aimlPattern2)) {
        content = content.replace(aimlPattern2, '<a href="aiml-tech-services.html" class="nested-trigger">AIML Engineering and MLOps <span');
        changed = true;
    }

    // AI Model Training
    const aiPattern = /<a href="javascript:void\(0\)" class="nested-trigger">AI Model Training <span/g;
    if (content.match(aiPattern)) {
        content = content.replace(aiPattern, '<a href="ai-model-training.html" class="nested-trigger">AI Model Training <span');
        changed = true;
    }

    // Enterprise Gen AI
    const entPattern = /<a href="javascript:void\(0\)" class="nested-trigger">Enterprise Gen AI <span/g;
    if (content.match(entPattern)) {
        content = content.replace(entPattern, '<a href="enterprise-ai-agents.html" class="nested-trigger">Enterprise Gen AI <span');
        changed = true;
    }

    if (changed) {
        fs.writeFileSync(fullPath, content);
        replaced++;
        console.log('Updated ' + file);
    }
}
console.log('Total files updated: ' + replaced);
