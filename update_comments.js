const fs = require('fs');
const path = require('path');

const dir = 'c:/Users/Sai chandra Mouli/Desktop/Website';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

let replacedNav = 0;
let replacedDrawer = 0;
let replacedHero = 0;

for (const file of files) {
    const fullPath = path.join(dir, file);
    let content = fs.readFileSync(fullPath, 'utf8');
    let original = content;

    // 1. Navbar Dropdown
    const navPattern = /<div class="nested-dropdown">(\s*<a[^>]*>\s*AIML Engineering and\s*MLOps.*?<\/div>\s*)<\/div>/g;
    content = content.replace(navPattern, (match) => {
        // Only comment if not already commented (just a safe-guard, but shouldn't be matched if inside comment if we're careful. Wait, regex matches everything.)
        return `<!-- ${match} -->`;
    });

    // 2. Drawer Dropdown
    const drawerPattern = /<div class="drawer-nested-dropdown">(\s*<button[^>]*>\s*AIML Engineering and\s*MLOps.*?<\/div>\s*)<\/div>/g;
    content = content.replace(drawerPattern, (match) => {
        return `<!-- ${match} -->`;
    });

    // 3. Hero Header Button
    const heroPattern = /<button[^>]*>\s*AIML Engineering and\s*MLOps\s*<\/button>/g;
    content = content.replace(heroPattern, (match) => {
        return `<!-- ${match} -->`;
    });

    if (content !== original) {
        fs.writeFileSync(fullPath, content);
        if (original.match(navPattern)) replacedNav++;
        if (original.match(drawerPattern)) replacedDrawer++;
        if (original.match(heroPattern)) replacedHero++;
        console.log('Updated ' + file);
    }
}
console.log(`Updated Nav: ${replacedNav} files`);
console.log(`Updated Drawer: ${replacedDrawer} files`);
console.log(`Updated Hero: ${replacedHero} files`);
