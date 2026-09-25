const fs = require('fs');
const path = require('path');

const dir = 'c:/Users/Sai chandra Mouli/Desktop/Website';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

const originalText = `            <div class="nested-dropdown">
              <a href="javascript:void(0)" class="nested-trigger">AI/ML Talent Services <span class="sub-arrow">▶</span></a>
            </div>`;

const newText = `            <div class="nested-dropdown">
              <a href="javascript:void(0)" class="nested-trigger">AI/ML Talent Services <span class="sub-arrow">▶</span></a>
              <div class="nested-dropdown-menu">
                <a href="javascript:void(0)">Specialized AI/ML Talent</a>
                <a href="javascript:void(0)">Flexible Talent Access</a>
                <a href="javascript:void(0)">Scalable AI/ML Teams</a>
                <a href="javascript:void(0)">Faster Project Delivery</a>
              </div>
            </div>`;

let replaced = 0;

for (const file of files) {
    const fullPath = path.join(dir, file);
    let content = fs.readFileSync(fullPath, 'utf8');
    
    if (content.includes(originalText)) {
        content = content.replace(originalText, newText);
        fs.writeFileSync(fullPath, content);
        replaced++;
        console.log('Updated ' + file);
    } else {
        // Also try regex in case of slight whitespace variations
        const regex = /<div class="nested-dropdown">\s*<a href="javascript:void\(0\)" class="nested-trigger">AI\/ML Talent Services <span class="sub-arrow">▶<\/span><\/a>\s*<\/div>/g;
        if (content.match(regex)) {
            content = content.replace(regex, newText.trim()); // Just in case
            fs.writeFileSync(fullPath, content);
            replaced++;
            console.log('Updated ' + file + ' (regex match)');
        }
    }
}
console.log('Total files updated: ' + replaced);
