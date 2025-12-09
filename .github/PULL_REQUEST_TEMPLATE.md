# Pull Request Template

## Description
Brief description of the changes made in this PR. What content is being added or modified?

**Type of Change**:
- [ ] New learning module(s)
- [ ] New learning path
- [ ] Module/content update
- [ ] Bug fix or correction
- [ ] Documentation update
- [ ] Metadata fix
- [ ] Structure/refactoring

## Related Issues
Closes #(issue number) if applicable.

## Checklist

### Content Quality
- [ ] Content is well-written and clear
- [ ] Learning outcomes are specific and measurable
- [ ] Code examples are complete and runnable
- [ ] No spelling or grammar errors
- [ ] Proper markdown formatting

### Metadata
- [ ] Metadata JSON is valid
- [ ] All required fields are present
- [ ] Module/path IDs follow naming conventions
- [ ] Version numbers are semantic
- [ ] Status field is appropriate

### Links & References
- [ ] All internal links are valid
- [ ] External links are current and relevant
- [ ] Image assets are properly referenced
- [ ] No broken file references

### Structure & Organization
- [ ] Files follow naming conventions
- [ ] Content is in correct directory hierarchy
- [ ] Learning path references exist
- [ ] Prerequisites are accurate and complete

### Validation
- [ ] Local validation scripts pass:
  - [ ] `validate-metadata.py` ✓
  - [ ] `validate-links.py` ✓
  - [ ] `validate-structure.py` ✓
- [ ] CI/CD validation will pass

### Documentation
- [ ] README updated if needed
- [ ] CONTRIBUTING guide referenced if needed
- [ ] Inline comments added for complex sections
- [ ] Changes documented in commit messages

## File Changes Summary

List the files that will be changed:

```
content/modules/metadata/module-001.json (new)
content/modules/units/unit-001/topic-001.md (new)
content/learning-paths/path-001.json (new)
```

## Testing Notes

Any special testing or validation performed:

```
- Verified code examples execute without errors
- Tested all links and references
- Checked rendering in markdown viewer
```

## Screenshots/Examples

If applicable, include examples of the content or changes:

<!-- Add screenshots or example outputs here -->

## Additional Notes

Any additional context or information reviewers should know:

---

## Reviewer Checklist

- [ ] Content quality is high
- [ ] Metadata is complete and valid
- [ ] No broken links or references
- [ ] Proper file organization
- [ ] Validation tests pass
- [ ] Learning outcomes are clear
- [ ] Code examples work correctly
- [ ] No merge conflicts
- [ ] Approval granted

---

**PR Title Format**: `feat(modules): add module title with X units`

**Examples**:
- `feat(modules): add JavaScript fundamentals module with 3 units`
- `fix(content): correct broken links in TypeScript module`
- `docs(readme): update content contribution guidelines`
- `refactor(structure): reorganize prerequisite hierarchy`
