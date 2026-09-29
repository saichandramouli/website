const fs = require('fs');
const path = require('path');

function getAllHtml(dir) {
  let results = [];
  const list = fs.readdirSync(dir);
  list.forEach(file => {
    const fullPath = path.join(dir, file);
    const stat = fs.statSync(fullPath);
    if (stat && stat.isDirectory()) {
      if (file !== '.git' && file !== 'node_modules') {
        results = results.concat(getAllHtml(fullPath));
      }
    } else if (file.endsWith('.html')) {
      results.push(fullPath);
    }
  });
  return results;
}

const apolloSnippet = `  <script>function initApollo(){var n=Math.random().toString(36).substring(7),o=document.createElement("script");
o.src="https://assets.apollo.io/micro/website-tracker/tracker.iife.js?nocache="+n,o.async=!0,o.defer=!0,
o.onload=function(){window.trackingFunctions.onLoad({appId:"6a9f8fbd28060b00149b77be"})},
document.head.appendChild(o)}initApollo();</script>`;

const files = getAllHtml('.');
console.log(`Found ${files.length} HTML files.`);

let updatedCount = 0;
let alreadyPresent = 0;
let missingGtag = 0;

files.forEach(file => {
  let content = fs.readFileSync(file, 'utf8');

  if (content.includes('initApollo')) {
    alreadyPresent++;
    return;
  }

  // Find closing tag of gtag script block
  const gtagRegex = /(gtag\('config'[^;]+;\s*<\/script>)/;
  if (gtagRegex.test(content)) {
    const eol = content.includes('\r\n') ? '\r\n' : '\n';
    content = content.replace(gtagRegex, `$1${eol}${apolloSnippet}`);
    fs.writeFileSync(file, content, 'utf8');
    updatedCount++;
  } else {
    // If gtag not found, fallback to before </head>
    const headRegex = /(<\/head>)/i;
    if (headRegex.test(content)) {
      const eol = content.includes('\r\n') ? '\r\n' : '\n';
      content = content.replace(headRegex, `${apolloSnippet}${eol}$1`);
      fs.writeFileSync(file, content, 'utf8');
      updatedCount++;
    } else {
      console.warn(`Could not find insertion point in: ${file}`);
      missingGtag++;
    }
  }
});

console.log(`Successfully updated: ${updatedCount}`);
console.log(`Already present: ${alreadyPresent}`);
console.log(`Failed/Skipped: ${missingGtag}`);
