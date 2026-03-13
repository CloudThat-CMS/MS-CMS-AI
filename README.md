# Content Management System

A comprehensive, Git-based learning content management system with  a structured organization, automated validation, and continuous deployment.

## 📋 Overview

This repository manages educational content organized in a hierarchical structure:

```
Learning Path
├── Module 1
│   ├── Unit 1
│   │   ├── Topic 1.1
│   │   └── Topic 1.2
│   ├── Unit 2
│   └── ...
├── Module 2
└── ...
```

### Key Features

✅ **Structured Content Organization** - Hierarchical learning paths with modules, units, and topics  
✅ **Metadata Management** - JSON-based module and path definitions with prerequisites and outcomes  
✅ **Version Control** - Git-based workflows with clear branching strategies  
✅ **Automated Validation** - Content structure, markdown, link, and metadata validation  
✅ **CI/CD Pipeline** - Automated testing and deployment to staging and production  
✅ **CDN Integration** - Content delivery with cache invalidation  

## 📁 Directory Structure

```
content/
├── learning-paths/              # Learning path definitions (JSON)
├── modules/
│   ├── metadata/                # Module metadata files (JSON)
│   └── units/                   # Unit content files (Markdown)
└── assets/
    ├── images/                  # Upload images,static assest and videos to blob storage (Script)
    └── videos/                  

.github/
└── workflows/                   # GitHub Actions workflows
    ├── content-validation.yml   # Automated content validation
    └── content-deployment.yml   # Content deployment pipeline

scripts/
├── validation/                  # Content validation scripts
│   ├── validate-metadata.py
│   ├── validate-links.py
│   └── validate-structure.py
└── deployment/                  # Deployment scripts
    └── deploy-to-cdn.py

docs/                            # Documentation
tests/                           # Automated tests
```
## 🔄 Content Update Workflow

Follow this workflow to contribute changes:

```
1. Create Feature Branch
   └─ git checkout -b feature/module-advanced-typescript

2. Author Content
   └─ Write/update markdown files and metadata

3. Commit Changes
   └─ git commit -m "feat(modules): add advanced TypeScript module"

4. Push & Create Pull Request
   └─ Triggers: Content Validation

5. Review & Approval
   └─ Minimum 1 approval required

6. Merge to develop
   └─ Merge PR (squash commits)
   └─ Triggers: Automated tests

7. Merge to main (Release)
   └─ Merge develop → main
   └─ Triggers: Staging deployment

8. Production Deployment
   └─ Merge main → Triggers: Production deployment
   └─ CDN cache invalidation
   └─ Release creation
```
## 🚀 Quick Start

### 1. Create a Learning Module

Create a new module metadata file in `content/modules/metadata/`:

```bash
# Copy and modify the template
cp content/modules/metadata/module-template.json \
   content/modules/metadata/module-web-basics.json
```

Edit the JSON file with your module details:
- Module ID: `module-001`
- Title, description, and version
- Learning outcomes (required)
- Prerequisites (optional)
- Units and topics structure

### 2. Add Module Content

Create markdown content files in `content/modules/units/`:

```bash
mkdir content/modules/units/unit-001
cp content/modules/units/unit-template.md \
   content/modules/units/unit-001/topic-001.md
```

Edit the markdown file with:
- Learning outcomes for each topic
- Content and explanations
- Code examples
- Resources and references
- Assessment questions

### 3. Create a Learning Path

Create a learning path definition in `content/learning-paths/`:

```bash
cp content/learning-paths/learning-path-template.json \
   content/learning-paths/path-web-development.json
```

Define:
- Path ID and title
- Sequence of modules
- Prerequisites (optional)
- Learning outcomes
- Capstone project (optional)



## 🌿 Git Workflow

### Branch Naming Convention

```
feature/<feature-name>          # New modules or features
  example: feature/module-react-fundamentals

hotfix/<issue-description>      # Critical fixes for production
  example: hotfix/broken-link-module-001

release/v<version>              # Release preparation
  example: release/v2.0.0
```

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat` - New module or feature
- `fix` - Content corrections
- `docs` - Documentation updates
- `refactor` - Content restructuring
- `test` - Test additions
- `chore` - Maintenance tasks

**Examples:**
```bash
git commit -m "feat(modules): add React fundamentals module with 6 units"

git commit -m "fix(content): correct broken links in TypeScript module
- Updated resource URLs
- Verified all links in unit 3

Closes #45"
```

## ✅ Content Validation

Automated validation runs on pull requests to ensure quality:

### Markdown Validation
- Checks markdown syntax
- Verifies proper formatting
- Lints for consistency

### Metadata Validation
- Validates JSON schema compliance
- Checks required fields
- Verifies ID formats
- Validates version numbering

### Link Validation
- Checks internal links and file references
- Verifies external URLs
- Reports broken references

### Structure Validation
- Ensures proper hierarchy
- Validates module/path references
- Checks for orphaned content

### Spelling Check
- Detects spelling errors
- Flags potential typos

### Run Locally
```bash
python scripts/validation/validate-metadata.py
python scripts/validation/validate-links.py
python scripts/validation/validate-structure.py
```

## 📦 Content Deployment

### Environments

**Staging Environment**
- URL: staging-cdn.example.com
- Purpose: Pre-production validation
- Triggered by: Merge to develop

**Production Environment**
- URL: cdn.example.com
- Purpose: Live content delivery
- Triggered by: Merge to main
- CDN cache invalidation: Automatic

### Deployment Process

1. **Build Artifacts**
   - Compile and optimize content
   - Generate deployment manifest
   - Create version information

2. **Staging Deployment**
   - Upload to staging CDN
   - Run smoke tests
   - Validate content delivery

3. **Production Deployment**
   - Upload to production CDN
   - Invalidate cache
   - Create GitHub release
   - Notify stakeholders

### Manual Deployment
```bash
python scripts/deployment/deploy-to-cdn.py --environment staging
python scripts/deployment/deploy-to-cdn.py --environment production
```

## 🧪 Testing

### Automated Tests

Tests run automatically on:
- Pull requests to `develop` or `main`
- Pushes to `develop` or `main`

### Manual Testing
```bash
# Run validation tests
python scripts/validation/validate-metadata.py
python scripts/validation/validate-links.py
python scripts/validation/validate-structure.py

# Run smoke tests (after deployment)
python scripts/validation/smoke-tests.py --environment staging
```

## 📊 Metadata Schemas

### Module Metadata Fields

```json
{
  "id": "module-001",
  "title": "Module Title",
  "description": "Description",
  "version": "1.0.0",
  "status": "published|draft|review|archived",
  "learningOutcomes": [
    {
      "id": "lo-001",
      "statement": "By the end of this module, students will..."
    }
  ],
  "prerequisites": [
    {
      "moduleId": "module-000",
      "title": "Prerequisite Module"
    }
  ],
  "estimatedHours": 2,
  "difficulty": "beginner|intermediate|advanced",
  "tags": ["tag1", "tag2"]
}
```

### Learning Path Metadata Fields

```json
{
  "id": "path-001",
  "title": "Path Title",
  "description": "Description",
  "version": "1.0.0",
  "status": "published|draft|review|archived",
  "modules": [
    {
      "id": "module-001",
      "title": "Module Title",
      "sequence": 1,
      "required": true
    }
  ],
  "estimatedHours": 20,
  "outcomes": ["Outcome 1", "Outcome 2"]
}
```

## 📖 Content Guidelines

### Markdown Standards

- Use clear, concise language
- Use proper heading hierarchy (h1 → h6)
- Include code examples where applicable
- Link to related content
- Add learning outcomes to each topic

### File Naming

- **Module files**: `module-[id].json`
- **Learning path files**: `path-[id].json`
- **Unit files**: `unit-[id]/topic-[id].md`
- **Use hyphens** for multi-word names
- **Use lowercase** for all filenames

### Content Organization

1. Learning Path → Multiple Modules
2. Module → Multiple Units
3. Unit → Multiple Topics
4. Topic → Content with outcomes and assessments

## 🤝 Contributing

### Requirements

- GitHub account with write access
- Git installed and configured
- Text editor for content creation
- Familiarity with markdown and JSON

### Steps to Contribute

1. **Clone Repository**
   ```bash
   git clone <repository-url>
   cd githubpoc2
   ```

2. **Create Feature Branch**
   ```bash
   git checkout -b feature/module-your-topic
   ```

3. **Add/Edit Content**
   - Create metadata files
   - Write markdown content
   - Add assets as needed

4. **Test Locally**
   ```bash
   python scripts/validation/validate-metadata.py
   python scripts/validation/validate-links.py
   python scripts/validation/validate-structure.py
   ```

5. **Commit Changes**
   ```bash
   git add content/
   git commit -m "feat(modules): add new module with clear description"
   ```

6. **Push and Create PR**
   ```bash
   git push origin feature/module-your-topic
   ```

7. **Review Process**
   - Address reviewer feedback
   - Update PR as requested
   - Wait for approval

8. **Merge**
   - PR merged squashes commits
   - Closes related issues

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 📋 Pull Request Template

See [PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md) for the standard PR template.

## 🔐 Security & Access

### Repository Access

- **Admin**: Full access, merge authority
- **Maintainer**: Review, approve, and merge PRs
- **Contributor**: Create branches and PRs
- **Public**: Read-only access

### Branch Protection

- `main`: Requires 2 approvals, CI passing
- `develop`: Requires 1 approval, CI passing

## 📞 Support & Issues

### Report Issues

- Create a GitHub issue with clear description
- Include steps to reproduce
- Attach relevant files or screenshots

### Common Issues

**Q: Link validation fails**  
A: Check file paths are relative to the markdown file location

**Q: Metadata validation fails**  
A: Ensure JSON is valid and matches schema requirements

**Q: Deployment fails**  
A: Verify environment variables are set and CDN is accessible

## 📝 License

This repository and all content is licensed under [LICENSE](LICENSE).

## 🙏 Acknowledgments

- Content authors and contributors
- Reviewers and maintainers
- CDN and hosting infrastructure

---

**Last Updated**: 2025-01-01  
**Maintained By**: Content Management Team
