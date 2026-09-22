const fs = require('fs');
const path = require('path');

const dir = 'c:/Users/Sai chandra Mouli/Desktop/Website';
const files = ['ai-model-training.html', 'aiml-tech-services.html', 'enterprise-ai-agents.html'];

for (const file of files) {
    const fullPath = path.join(dir, file);
    let content = fs.readFileSync(fullPath, 'utf8');
    let original = content;

    // Update HTML links
    if (file === 'enterprise-ai-agents.html') {
        content = content.replace(
            /<a href="conversational-ai-customer-service\.html">/g,
            '<a href="#conversational-ai-customer-service-section">'
        );
        content = content.replace(
            /<li><a href="conversational-ai-customer-service\.html">/g,
            '<li><a href="#conversational-ai-customer-service-section">'
        );
        // Also update JS array
        content = content.replace(
            '{ name: "Conversational AI / Customer Service AI", url: "conversational-ai-customer-service.html" }',
            '{ name: "Conversational AI / Customer Service AI", url: "#conversational-ai-customer-service-section" }'
        );
    } else {
        content = content.replace(
            /<a href="conversational-ai-customer-service\.html">/g,
            '<a href="enterprise-ai-agents.html#conversational-ai-customer-service-section">'
        );
        // Also update JS array
        content = content.replace(
            '{ name: "Conversational AI / Customer Service AI", url: "conversational-ai-customer-service.html" }',
            '{ name: "Conversational AI / Customer Service AI", url: "enterprise-ai-agents.html#conversational-ai-customer-service-section" }'
        );
    }

    if (content !== original) {
        fs.writeFileSync(fullPath, content);
        console.log('Updated links in ' + file);
    }
}
