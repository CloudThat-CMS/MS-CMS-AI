# Contributing to Learning Content

Thank you for contributing to our learning platform! This guide will help you understand the content creation process and best practices.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Content Structure](#content-structure)
3. [Creating New Content](#creating-new-content)
4. [Content Guidelines](#content-guidelines)
5. [Review Process](#review-process)
6. [Common Patterns](#common-patterns)

## Getting Started

### Prerequisites

- GitHub account with write access
- Git installed (`git --version`)
- Text editor (VS Code recommended)
- Basic markdown knowledge
- Familiarity with JSON format

### Initial Setup

```bash
# Clone the repository
git clone <repository-url>
cd githubpoc2

# Create your feature branch
git checkout -b feature/module-topic-name

# You're ready to start contributing!
```

## Content Structure

### Hierarchical Organization

Content is organized in a clear hierarchy:

```
Learning Path (learning-paths/*.json)
└── Module (modules/metadata/*.json)
    └── Unit (modules/units/unit-*/topic-*.md)
        └── Topic Content
```

### Directory Layout

```
content/
├── learning-paths/
│   ├── learning-path-template.json
│   └── path-web-development.json
├── modules/
│   ├── metadata/
│   │   ├── module-template.json
│   │   ├── module-001-fundamentals.json
│   │   └── module-002-advanced.json
│   └── units/
│       ├── unit-001/
│       │   ├── topic-001.md
│       │   └── topic-002.md
│       └── unit-002/
│           └── topic-001.md
└── assets/
    ├── images/
    └── videos/
```

## Creating New Content

### Step 1: Create Module Metadata

Create a new module definition file:

**File**: `content/modules/metadata/module-basics.json`

```json
{
  "id": "module-001",
  "title": "Web Development Fundamentals",
  "description": "Learn the basics of web development including HTML, CSS, and JavaScript",
  "version": "1.0.0",
  "status": "draft",
  "createdDate": "2025-01-01T00:00:00Z",
  "lastModified": "2025-01-01T00:00:00Z",
  "author": "Your Name",
  "learningOutcomes": [
    {
      "id": "lo-001",
      "statement": "Understand the structure of HTML documents"
    },
    {
      "id": "lo-002",
      "statement": "Create styled web pages using CSS"
    }
  ],
  "prerequisites": [],
  "estimatedHours": 3,
  "units": [
    {
      "id": "unit-001",
      "title": "HTML Basics",
      "sequence": 1,
      "topics": [
        {
          "id": "topic-001",
          "title": "Introduction to HTML",
          "sequence": 1,
          "contentFile": "units/unit-001/topic-001.md"
        }
      ]
    }
  ],
  "tags": ["web", "html", "css", "javascript"],
  "difficulty": "beginner",
  "relatedModules": []
}
```

**Key Fields**:
- `id`: Unique identifier (module-XXX format)
- `title`: Clear, descriptive title
- `learningOutcomes`: What students will learn (required, minimum 1)
- `estimatedHours`: Realistic time estimate
- `status`: draft, review, published, or archived
- `difficulty`: beginner, intermediate, or advanced

### Step 2: Create Unit Content

Create markdown files for your units:

**File**: `content/modules/units/unit-001/topic-001.md`

```markdown
# Topic Title

## Metadata
- **Unit ID**: unit-001
- **Module ID**: module-001
- **Sequence**: 1
- **Estimated Time**: 20 minutes

## Learning Outcomes
- Identify key concepts
- Apply knowledge in practice

## Introduction

Start with an engaging introduction that explains why this topic matters.

## Key Concepts

### Concept 1: Explain This Concept

Provide clear explanation with real-world examples.

```javascript
// Code examples help understanding
const example = "Always include practical code samples";
```

### Concept 2: Another Important Idea

Continue with additional concepts and examples.

## Practical Applications

1. **Application 1**: How this applies in real scenarios
2. **Application 2**: Another practical use case
3. **Application 3**: Real-world implementation

## Common Mistakes

- Mistake 1: What students often get wrong
- Mistake 2: Common misunderstandings

## Practice Exercise

> **Activity**: Try implementing a simple example based on what you learned.
> 
> **Instructions**:
> 1. Create a file called `example.js`
> 2. Implement the following function
> 3. Test with provided samples

## Summary

Recap the key points covered in this topic.

## Next Steps

- Proceed to the next topic
- Complete the practice exercise
- Review supplementary materials

## Additional Resources

- [Resource Title](https://example.com)
- [Another Resource](https://example.com)

---

*Last Updated: 2025-01-01*
```

### Step 3: Create Learning Path (Optional)

If organizing multiple modules into a path:

**File**: `content/learning-paths/path-web-development.json`

```json
{
  "id": "path-001",
  "title": "Complete Web Development",
  "description": "Master web development from basics to advanced",
  "version": "1.0.0",
  "status": "draft",
  "createdDate": "2025-01-01T00:00:00Z",
  "lastModified": "2025-01-01T00:00:00Z",
  "author": "Your Name",
  "modules": [
    {
      "id": "module-001",
      "title": "HTML Fundamentals",
      "sequence": 1,
      "required": true,
      "estimatedHours": 3
    },
    {
      "id": "module-002",
      "title": "CSS Styling",
      "sequence": 2,
      "required": true,
      "estimatedHours": 4
    },
    {
      "id": "module-003",
      "title": "JavaScript Basics",
      "sequence": 3,
      "required": true,
      "estimatedHours": 5
    }
  ],
  "prerequisites": [],
  "outcomes": [
    "Build functional websites",
    "Create responsive designs",
    "Implement interactive features"
  ],
  "estimatedHours": 12,
  "difficultyLevel": "beginner"
}
```

## Content Guidelines

### Writing Style

✅ **DO**:
- Use clear, simple language
- Break concepts into small chunks
- Include practical examples
- Add learning outcomes to each topic
- Link to related content

❌ **DON'T**:
- Use overly technical jargon without explanation
- Create huge blocks of text
- Skip examples and practical application
- Include outdated information
- Write without clear structure

### Markdown Best Practices

```markdown
# Heading 1 (Page title - use once per file)

## Heading 2 (Main sections)

### Heading 3 (Subsections)

#### Heading 4 (Detail sections)

**Bold** for emphasis
*Italic* for additional emphasis

- Bullet lists for unordered items
  - Nested items for sub-points

1. Numbered lists for sequences
2. Always use proper ordering
3. Include explanatory text

> Blockquotes for important notes and tips

| Header 1 | Header 2 |
|----------|----------|
| Cell     | Cell     |

[Link text](https://example.com)

\`\`\`javascript
// Code blocks with language specified
const example = "preferred format";
\`\`\`
```

### Code Examples

Always include runnable code examples:

```javascript
// GOOD: Complete, runnable example
function calculateTotal(items) {
  return items.reduce((sum, item) => sum + item.price, 0);
}

const cart = [
  { name: "Book", price: 15 },
  { name: "Pen", price: 2 }
];

console.log(calculateTotal(cart)); // Output: 17
```

```javascript
// BAD: Incomplete or unclear
const calc = x => {
  // some logic
};
```

### Learning Outcomes

Write clear, measurable outcomes:

✅ **Good learning outcomes**:
- "Understand the difference between let and const in JavaScript"
- "Create responsive layouts using CSS Grid"
- "Implement form validation using JavaScript"

❌ **Poor learning outcomes**:
- "Learn JavaScript"
- "Know about CSS"
- "Understand web development"

### Metadata Requirements

**Module Metadata**:
- ✅ Unique ID following `module-XXX` format
- ✅ Clear, descriptive title (5-200 characters)
- ✅ Meaningful description
- ✅ Learning outcomes (minimum 1)
- ✅ Estimated hours
- ✅ Status (draft/review/published/archived)

**Content Files**:
- ✅ Proper markdown formatting
- ✅ Clear heading hierarchy
- ✅ Learning outcomes section
- ✅ Code examples where applicable
- ✅ Summary section

## Review Process

### Before Submitting

1. **Validate Locally**
   ```bash
   python scripts/validation/validate-metadata.py
   python scripts/validation/validate-links.py
   python scripts/validation/validate-structure.py
   ```

2. **Check Formatting**
   - Verify markdown renders correctly
   - Check all links work
   - Ensure code examples run

3. **Review Guidelines**
   - Follow writing style
   - Check for typos and grammar
   - Verify metadata completeness

4. **Self-Review Checklist**
   - [ ] All required metadata fields present
   - [ ] Learning outcomes are clear and measurable
   - [ ] Content is well-organized and easy to follow
   - [ ] Code examples are complete and runnable
   - [ ] All links are functional
   - [ ] No spelling or grammar errors
   - [ ] Images and assets properly referenced
   - [ ] Estimated hours are realistic

### Submitting a Pull Request

1. **Push Your Branch**
   ```bash
   git push origin feature/module-your-topic
   ```

2. **Create Pull Request**
   - Title: `feat(modules): add module title`
   - Description: Include what you added
   - Reference related issues: `Closes #123`

3. **PR Template** (automatically applied):
   ```markdown
   ## Description
   Brief description of the changes

   ## Type of Change
   - [ ] New module
   - [ ] Module update
   - [ ] Bug fix
   - [ ] Documentation

   ## Checklist
   - [ ] Metadata validation passes
   - [ ] Content is well-structured
   - [ ] All links are valid
   - [ ] Learning outcomes are clear
   - [ ] Code examples are complete
   ```

### Review Feedback

- **Requested Changes**: Fix issues and push updates
- **Approved**: Your PR will be merged
- **Commented**: Address feedback in new commits

## Common Patterns

### Module with Prerequisites

```json
{
  "id": "module-advanced-js",
  "title": "Advanced JavaScript",
  "prerequisites": [
    {
      "moduleId": "module-basics-js",
      "title": "JavaScript Fundamentals"
    }
  ],
  "learningOutcomes": [...]
}
```

### Multi-Unit Module

```json
{
  "id": "module-003",
  "units": [
    {
      "id": "unit-001",
      "title": "Unit 1: Introduction",
      "sequence": 1,
      "topics": [...]
    },
    {
      "id": "unit-002",
      "title": "Unit 2: Core Concepts",
      "sequence": 2,
      "topics": [...]
    }
  ]
}
```

### Markdown with Interactive Elements

```markdown
> **Key Point**: This is important to remember

> **Note**: Additional information that helps

> **Warning**: Common mistake to avoid

> **Tip**: Helpful hint for learners
```

## Naming Conventions

**Modules**:
- File: `module-NNN-descriptive-name.json`
- ID: `module-NNN` (where NNN is numeric)
- Example: `module-001-web-basics.json`

**Units**:
- Directory: `unit-NNN/`
- ID: `unit-NNN`
- Example: `unit-001/`

**Topics**:
- File: `topic-NNN.md`
- ID: `topic-NNN`
- Example: `topic-001.md`

**Learning Paths**:
- File: `path-descriptive-name.json`
- ID: `path-NNN`
- Example: `path-web-development.json`

## Questions?

- Check the [README](README.md)
- Review [GITFLOW](GITFLOW.md)
- Open an issue for questions
- Contact the content team

---

Thank you for contributing to making great learning content!
