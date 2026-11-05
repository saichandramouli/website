files_to_update = [
    'ai-ml-model-development.html',
    'ai-ml-talent-services.html',
    'ai-model-training.html',
    'aiml-engineering-mlops.html',
    'aiml-tech-services.html',
    'enterprise-ai-agents.html',
    'update_experience_center.py'
]

for filename in files_to_update:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content.replace('ai-newsletter-issue-05.html', 'ai-newsletter-issue-06.html')
    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"No changes in {filename}")

