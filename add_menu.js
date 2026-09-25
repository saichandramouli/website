const fs = require('fs');
const path = require('path');

const dir = 'c:/Users/Sai chandra Mouli/Desktop/Website';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

const insertText = `
            <div class="nested-dropdown">
              <a href="javascript:void(0)" class="nested-trigger">AI/ML Talent Services <span class="sub-arrow">▶</span></a>
            </div>`;

let replaced = 0;

for (const file of files) {
    const fullPath = path.join(dir, file);
    let content = fs.readFileSync(fullPath, 'utf8');
    
    // We want to append this new nested-dropdown after the Enterprise Gen AI nested dropdown.
    // Let's use a regex that safely matches the Enterprise Gen AI nested dropdown and its closing tags.
    const regex = /(<a href="enterprise-ai-agents\.html" class="nested-trigger">Enterprise Gen AI.*?<\/div>\s*<\/div>)/s;
    if (content.match(regex) && !content.includes('AI/ML Talent Services')) {
        content = content.replace(regex, `$1${insertText}`);
        fs.writeFileSync(fullPath, content);
        replaced++;
        console.log('Updated ' + file);
    }
}
console.log('Total files updated: ' + replaced);
