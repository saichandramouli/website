const fs = require('fs');
const path = require('path');

const dir = 'c:/Users/Sai chandra Mouli/Desktop/Website';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

const buttonHtml = `\n        <button type="button" class="agent-header-nav-item" data-category="aiml-talent-services" onclick="window.location.href='ai-ml-talent-services.html'">AI/ML Talent Services</button>`;

let replaced = 0;

for (const file of files) {
    const fullPath = path.join(dir, file);
    let content = fs.readFileSync(fullPath, 'utf8');

    // Find where the Enterprise Gen AI button ends and add our new button
    const regex = /(<button[^>]*data-category="enterprise-gen-ai"[^>]*>Enterprise Gen\s*AI<\/button>)/;
    
    if (content.match(regex) && !content.includes('data-category="aiml-talent-services"')) {
        content = content.replace(regex, `$1${buttonHtml}`);
        
        // Let's also ensure the 'active' class is correctly set ONLY for the current page
        // Actually, if we are on ai-ml-talent-services.html, we should make IT active
        if (file === 'ai-ml-talent-services.html') {
            content = content.replace('class="agent-header-nav-item active" data-category="enterprise-gen-ai"', 'class="agent-header-nav-item" data-category="enterprise-gen-ai"');
            content = content.replace('class="agent-header-nav-item" data-category="aiml-talent-services"', 'class="agent-header-nav-item active" data-category="aiml-talent-services"');
        }
        
        fs.writeFileSync(fullPath, content);
        replaced++;
        console.log('Updated header nav in ' + file);
    }
}
console.log('Total files updated: ' + replaced);
