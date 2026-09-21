const fs = require('fs');
const path = require('path');

const dir = 'c:/Users/Sai chandra Mouli/Desktop/Website';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

let replacedNav = 0;
let replacedDrawer = 0;

for (const file of files) {
    const fullPath = path.join(dir, file);
    let content = fs.readFileSync(fullPath, 'utf8');
    let original = content;

    // 1. Navbar Dropdown
    const navPattern = /<div class="nested-dropdown">\s*<a[^>]*>AIML Engineering and\s*MLOps[\s\S]*?<\/div>\s*<\/div>/g;
    content = content.replace(navPattern, (match) => {
        return `<!-- ${match} -->`;
    });

    // 2. Drawer Dropdown
    const drawerPattern = /<div class="drawer-nested-dropdown">\s*<button[^>]*>\s*AIML Engineering and\s*MLOps[\s\S]*?<\/div>\s*<\/div>/g;
    content = content.replace(drawerPattern, (match) => {
        return `<!-- ${match} -->`;
    });

    if (content !== original) {
        fs.writeFileSync(fullPath, content);
        if (original.match(navPattern)) replacedNav++;
        if (original.match(drawerPattern)) replacedDrawer++;
        console.log('Updated ' + file);
    }
}
console.log(`Updated Nav: ${replacedNav} files`);
console.log(`Updated Drawer: ${replacedDrawer} files`);
