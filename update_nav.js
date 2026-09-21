const fs = require('fs');
const path = require('path');

const dir = 'c:/Users/Sai chandra Mouli/Desktop/Website';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

let replaced = 0;

// Regular expression to match the "AI Model Training" nested dropdown block.
const targetPattern = /<div class="nested-dropdown">\s*<a href="javascript:void\(0\)" class="nested-trigger">AI Model Training <span class="sub-arrow">.*?<\/span><\/a>\s*<div class="nested-dropdown-menu">[\s\S]*?<\/div>\s*<\/div>/g;

const replacementText = `<div class="nested-dropdown">
              <a href="javascript:void(0)" class="nested-trigger">AI Model Training <span class="sub-arrow">▶</span></a>
              <div class="nested-dropdown-menu">
                <a href="ai-model-training.html#expert-data-creation-annotation-section">Expert Data Creation &amp; Annotation</a>
                <a href="ai-model-training.html#rlhf-human-feedback-section">RLHF / Human Feedback</a>
                <a href="ai-model-training.html#ai-model-evaluation-section">AI Model Evaluation</a>
                <a href="ai-model-training.html#benchmark-test-set-creation-section">Benchmark &amp; Test-Set Creation</a>
                <a href="ai-model-training.html#coding-expertise-ai-training-section">Coding Expertise for AI Training</a>
                <a href="ai-model-training.html#stem-reasoning-expertise-section">STEM &amp; Reasoning Expertise</a>
                <a href="ai-model-training.html#reinforcement-learning-environments-section">Reinforcement-Learning Environments</a>
              </div>
            </div>`;

for (const file of files) {
    const fullPath = path.join(dir, file);
    let content = fs.readFileSync(fullPath, 'utf8');
    if (content.match(targetPattern)) {
        content = content.replace(targetPattern, replacementText);
        fs.writeFileSync(fullPath, content);
        replaced++;
        console.log('Updated ' + file);
    }
}
console.log('Total files updated: ' + replaced);
