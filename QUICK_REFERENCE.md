# Content Management System - Quick Reference

## 📚 File Organization

```
Create Module Content:
1. content/modules/metadata/module-XXX.json    ← Module definition
2. content/modules/units/unit-XXX/topic-YYY.md ← Unit content
3. Add to learning path: content/learning-paths/path-XXX.json

Create Assets:
- Images: content/assets/images/
- Videos: content/assets/videos/
```

## 🔄 Workflow (Git Commands)

```bash
# 1. Create feature branch
git checkout -b feature/module-topic-name

# 2. Create content files
# Edit: content/modules/metadata/module-XXX.json
# Create: content/modules/units/unit-XXX/topic-YYY.md

# 3. Validate locally
python scripts/validation/validate-metadata.py
python scripts/validation/validate-links.py
python scripts/validation/validate-structure.py

# 4. Commit changes
git add content/
git commit -m "feat(modules): add module title with X units"

# 5. Push and create PR
git push origin feature/module-topic-name
# Create PR on GitHub

# 6. After approval, merge to develop
# (Automatic tests run)

# 7. Release: merge develop to main
# (Automatic production deployment)
```

## 📋 Module Metadata Template

```json
{
  "id": "module-XXX",
  "title": "Module Title (5-200 chars)",
  "description": "Clear description",
  "version": "1.0.0",
  "status": "draft|review|published|archived",
  "author": "Your Name",
  "learningOutcomes": [
    {
      "id": "lo-001",
      "statement": "Clear, measurable outcome"
    }
  ],
  "estimatedHours": 3,
  "difficulty": "beginner|intermediate|advanced",
  "units": [
    {
      "id": "unit-001",
      "title": "Unit Title",
      "sequence": 1,
      "topics": [
        {
          "id": "topic-001",
          "title": "Topic Title",
          "sequence": 1,
          "contentFile": "units/unit-001/topic-001.md"
        }
      ]
    }
  ]
}
```

## 📄 Unit Content Template (Markdown)

```markdown
# Topic Title

## Learning Outcomes
- Outcome 1
- Outcome 2

## Key Concepts

### Concept 1
Explanation with examples

\`\`\`javascript
// Code example
const example = "runnable code";
\`\`\`

## Practice Exercise
Instructions for hands-on practice

## Summary
Key takeaways

## Resources
- [Link](url)
```

## 🧪 Validation Commands

```bash
# Check all content
python scripts/validation/validate-metadata.py   # JSON schemas
python scripts/validation/validate-links.py      # Link integrity
python scripts/validation/validate-structure.py  # Hierarchy

# Each returns: ✅ or ❌
```

## 📤 Deployment

```bash
# Local testing (staging)
python scripts/deployment/deploy-to-cdn.py --environment staging

# Production (automatic on main push)
# OR manual:
python scripts/deployment/deploy-to-cdn.py --environment production
```

## 🌿 Branch Naming

```
feature/module-topic-name        ← New modules
feature/add-units-to-module      ← Content updates
hotfix/broken-link               ← Production fixes
release/v2.0.0                   ← Release prep
```

## 💾 Commit Message Format

```
<type>(<scope>): <subject>

<body>

Types: feat, fix, docs, refactor, test, chore, style

Examples:
- feat(modules): add web fundamentals module
- fix(content): correct link in typescript module
- docs(readme): update contribution guidelines
```

## 🔑 Key File Locations

```
README.md                          ← Main documentation
CONTRIBUTING.md                    ← How to contribute
GITFLOW.md                         ← Git strategy
SETUP_SUMMARY.md                   ← Setup overview
.github/PULL_REQUEST_TEMPLATE.md   ← PR template
docs/SCRIPTS_README.md             ← Script documentation
content/modules/metadata/          ← Module definitions
content/modules/units/             ← Unit content files
content/learning-paths/            ← Path definitions
scripts/validation/                ← Validation scripts
scripts/deployment/                ← Deployment scripts
```

## ❓ Common Commands

```bash
# Add new module
cp content/modules/metadata/module-template.json \
   content/modules/metadata/module-XXX.json

# Add new unit
mkdir content/modules/units/unit-XXX
cp content/modules/units/unit-template.md \
   content/modules/units/unit-XXX/topic-001.md

# View recent commits
git log --oneline -10

# Check branch status
git branch -a

# See changes before commit
git diff content/

# Undo last commit (not pushed)
git reset --soft HEAD~1
```

## 🚨 Troubleshooting

| Issue | Solution |
|-------|----------|
| JSON validation fails | Check JSON syntax, verify required fields |
| Link validation fails | Verify file paths are correct |
| Structure validation fails | Check directory structure |
| Metadata required field missing | Review template for required fields |
| PR won't merge | Wait for all CI checks to pass |

## 📞 Getting Help

1. **Check Documentation**
   - README.md - Overview
   - CONTRIBUTING.md - Content creation
   - GITFLOW.md - Git workflow
   - docs/SCRIPTS_README.md - Scripts

2. **Validate Locally**
   - Run validation scripts
   - Check error messages
   - Review template files

3. **Review Examples**
   - module-001-web-fundamentals.json
   - path-001-complete-bootcamp.json
   - unit-template.md

---

**Quick Links:**
- [Main README](../README.md)
- [Contributing Guide](../CONTRIBUTING.md)
- [Git Workflow](../GITFLOW.md)
- [Setup Summary](../SETUP_SUMMARY.md)

Last Updated: 2025-01-01
