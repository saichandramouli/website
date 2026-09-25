const fs = require('fs');
const path = require('path');

const dir = 'c:/Users/Sai chandra Mouli/Desktop/Website';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

const oldTrigger = '<a href="javascript:void(0)" class="nested-trigger">AI/ML Talent Services <span class="sub-arrow">▶</span></a>';
const newTrigger = '<a href="ai-ml-talent-services.html" class="nested-trigger">AI/ML Talent Services <span class="sub-arrow">▶</span></a>';

const oldSub1 = '<a href="javascript:void(0)">Specialized AI/ML Talent</a>';
const newSub1 = '<a href="ai-ml-talent-services.html#specialized-aiml-talent-section">Specialized AI/ML Talent</a>';

const oldSub2 = '<a href="javascript:void(0)">Flexible Talent Access</a>';
const newSub2 = '<a href="ai-ml-talent-services.html#flexible-talent-access-section">Flexible Talent Access</a>';

const oldSub3 = '<a href="javascript:void(0)">Scalable AI/ML Teams</a>';
const newSub3 = '<a href="ai-ml-talent-services.html#scalable-aiml-teams-section">Scalable AI/ML Teams</a>';

const oldSub4 = '<a href="javascript:void(0)">Faster Project Delivery</a>';
const newSub4 = '<a href="ai-ml-talent-services.html#faster-project-delivery-section">Faster Project Delivery</a>';

let replaced = 0;

for (const file of files) {
    const fullPath = path.join(dir, file);
    let content = fs.readFileSync(fullPath, 'utf8');
    let changed = false;

    if (content.includes(oldTrigger)) {
        content = content.replace(new RegExp(oldTrigger.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'g'), newTrigger);
        changed = true;
    }
    if (content.includes(oldSub1)) {
        content = content.replace(new RegExp(oldSub1.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'g'), newSub1);
        changed = true;
    }
    if (content.includes(oldSub2)) {
        content = content.replace(new RegExp(oldSub2.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'g'), newSub2);
        changed = true;
    }
    if (content.includes(oldSub3)) {
        content = content.replace(new RegExp(oldSub3.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'g'), newSub3);
        changed = true;
    }
    if (content.includes(oldSub4)) {
        content = content.replace(new RegExp(oldSub4.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'g'), newSub4);
        changed = true;
    }

    if (changed) {
        fs.writeFileSync(fullPath, content);
        replaced++;
        console.log('Updated links in ' + file);
    }
}
console.log('Total files link-updated: ' + replaced);
