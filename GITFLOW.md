# Gitflow Configuration for Content Management

## Branch Strategy

### Main Branches
- **main**: Production-ready content. Only receives merges from release branches and hotfix branches.
- **develop**: Development branch where features are integrated. Serves as the base for feature branches.

### Supporting Branches
- **feature/\***: Feature branches for new content modules or significant updates. Branch from `develop`.
  - Example: `feature/module-advanced-typescript`
  - Example: `feature/learning-path-aws-basics`

- **hotfix/\***: Critical bug fixes and corrections for production content. Branch from `main`.
  - Example: `hotfix/broken-link-in-module-001`
  - Example: `hotfix/incorrect-prerequisites`

- **release/\***: Release preparation branches. Branch from `develop` when ready for release.
  - Example: `release/v2.0.0`

## Branch Protection Rules

### main Branch
- Require pull request reviews (minimum 2 approvals)
- Require status checks to pass (CI/CD pipeline)
- Require branches to be up to date before merging
- Include administrators in restrictions

### develop Branch
- Require pull request reviews (minimum 1 approval)
- Require status checks to pass
- Require branches to be up to date before merging

## Commit Message Convention

Follow conventional commits format:

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types
- **feat**: New learning module or feature
- **docs**: Documentation or content updates
- **fix**: Bug fixes or content corrections
- **refactor**: Restructuring content or metadata
- **test**: Adding or updating tests
- **chore**: Maintenance tasks (dependencies, tooling)
- **style**: Formatting changes (no functional changes)

### Examples
```
feat(modules): add advanced TypeScript module with 5 units

This module covers advanced TypeScript patterns including:
- Generics and type constraints
- Decorators and metadata
- Utility types
- Advanced type narrowing

Closes #123

chore(metadata): update module prerequisites for clarity

fix(content): correct broken link in unit 2 of foundations module

docs(README): add content contribution guidelines
```

## Pull Request Template

See PULL_REQUEST_TEMPLATE.md for the standard PR template.

## Tagging Convention

Version tags follow semantic versioning:

```
v<major>.<minor>.<patch>[-prerelease][+build]
```

Examples:
- v1.0.0 - Initial release
- v1.1.0 - New modules added
- v1.1.1 - Bug fix
- v2.0.0 - Major content reorganization
- v2.0.0-beta.1 - Beta release

## Merge Strategy

- **Feature branches** → `develop` (squash commits for cleaner history)
- **Develop** → `main` (create merge commit for traceability)
- **Hotfix** → `main` (create merge commit) and back-merge to `develop`

## Guidelines

1. Create feature branches early in the content development process
2. Keep branches focused on single content modules or features
3. Sync branches regularly with their base branches
4. Delete branches after merging
5. Use descriptive branch names that reference content modules or issues

