#!/usr/bin/env python3
"""
README for validation and deployment scripts.
"""

# Validation Scripts
# ==================

## validate-metadata.py
Validates all module and learning path metadata JSON files against defined JSON schemas.

### Features:
- Validates module metadata schema compliance
- Validates learning path metadata schema compliance
- Checks required fields
- Validates field formats (IDs, versions, dates)
- Reports validation errors and warnings

### Usage:
```bash
python scripts/validation/validate-metadata.py
```

### What it checks:
- Module ID format: module-XXX
- Learning path ID format: path-XXX
- Title length: 5-200 characters
- Version format: X.Y.Z (semantic versioning)
- Status values: draft, review, published, archived
- Learning outcomes: minimum 1, with id and statement
- Difficulty levels: beginner, intermediate, advanced
- Numeric fields: estimatedHours >= 0

---

## validate-links.py
Validates all links and references in markdown content files.

### Features:
- Extracts links from markdown files
- Validates internal file references
- Checks external URL format
- Identifies broken local file links
- Supports both markdown and HTML link formats

### Usage:
```bash
python scripts/validation/validate-links.py
```

### What it checks:
- Internal links to existing files
- Anchor links (#section-id)
- External URLs (format validation)
- Path references are relative to file location
- Image and asset references

---

## validate-structure.py
Validates the hierarchical content structure.

### Features:
- Checks directory structure compliance
- Validates learning path module references
- Confirms module existence
- Identifies orphaned content
- Reports structure consistency

### Usage:
```bash
python scripts/validation/validate-structure.py
```

### What it checks:
- Required directories exist
- Learning paths reference valid modules
- Modules reference valid units
- Units have proper structure
- No orphaned content files

---

# Deployment Scripts
# ==================

## deploy-to-cdn.py
Builds and deploys content to CDN/web server.

### Features:
- Compiles content artifacts
- Generates deployment manifest
- Uploads to staging and production
- Invalidates CDN cache
- Creates release information

### Usage:
```bash
python scripts/deployment/deploy-to-cdn.py --environment staging
python scripts/deployment/deploy-to-cdn.py --environment production
```

### Environment Variables:
- `STAGING_DEPLOY_KEY`: API key for staging deployment
- `STAGING_ENDPOINT`: CDN endpoint for staging
- `PROD_DEPLOY_KEY`: API key for production deployment
- `PROD_ENDPOINT`: CDN endpoint for production
- `CDN_DISTRIBUTION_ID`: CloudFront distribution ID for cache invalidation
- `GITHUB_RUN_NUMBER`: GitHub Actions run number
- `GITHUB_SHA`: Git commit SHA

### Build Output:
- `build/learning-paths/`: Compiled learning paths
- `build/modules/`: Compiled modules and units
- `build/assets/`: Static assets (images, videos)
- `build/manifest.json`: Deployment manifest with file list

---

# CI/CD Workflows
# ================

## content-validation.yml
Runs on pull requests to validate content quality.

### Jobs:
1. **markdown-validation**: Lints markdown files
2. **metadata-validation**: Validates JSON schemas
3. **link-validation**: Checks all links
4. **spelling-check**: Detects spelling errors
5. **content-structure**: Validates hierarchy

### Triggered on:
- Pull requests to `develop`, `main`, or `release/*` branches
- Changes to `content/**` or `.github/workflows/**`

---

## content-deployment.yml
Deploys validated content to staging and production.

### Jobs:
1. **staging-deployment**: Deploy to staging CDN
2. **production-deployment**: Deploy to production
3. **notify**: Send notifications to stakeholders

### Deployment Process:
1. Build content artifacts
2. Deploy to staging environment
3. Run smoke tests
4. Deploy to production (if staging passes)
5. Invalidate CDN cache
6. Create GitHub release

### Triggered on:
- Pushes to `main` branch
- Changes to `content/**`

---

# Local Testing
# ==============

### Run all validation:
```bash
cd githubpoc2
python scripts/validation/validate-metadata.py
python scripts/validation/validate-links.py
python scripts/validation/validate-structure.py
```

### Run specific validation:
```bash
# Metadata only
python scripts/validation/validate-metadata.py

# Links only
python scripts/validation/validate-links.py

# Structure only
python scripts/validation/validate-structure.py
```

### Test deployment locally:
```bash
python scripts/deployment/deploy-to-cdn.py --environment staging
```

---

# Troubleshooting
# ================

### JSON validation fails
- Check JSON syntax (use online JSON validator)
- Verify all required fields are present
- Ensure ID format matches pattern (module-XXX, path-XXX)
- Check version format is semantic (X.Y.Z)

### Link validation fails
- Verify file paths are relative to markdown location
- Check for typos in file references
- Ensure referenced files exist
- Use forward slashes (/) in paths

### Structure validation fails
- Ensure directory structure exists
- Check module references in learning paths
- Verify metadata file naming conventions
- Look for orphaned content files

### Deployment fails
- Verify environment variables are set
- Check CDN credentials and endpoints
- Ensure build directory exists
- Review deployment logs for details

---

Last Updated: 2025-01-01
