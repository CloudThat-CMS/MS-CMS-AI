#!/usr/bin/env python3
"""
Example content example demonstrating the module structure.
"""

# Learning Module: Web Development Fundamentals
# Module ID: module-001
# Status: Example

import json
from datetime import datetime

# Example module definition
example_module = {
    "id": "module-001",
    "title": "Web Development Fundamentals",
    "description": "Learn the complete basics of web development including HTML, CSS, and JavaScript fundamentals.",
    "version": "1.0.0",
    "status": "published",
    "createdDate": "2025-01-01T00:00:00Z",
    "lastModified": "2025-01-15T10:30:00Z",
    "author": "Content Team",
    "reviewedBy": "Senior Instructor",
    "learningPath": "path-001",
    "prerequisites": [],
    "learningOutcomes": [
        {
            "id": "lo-001",
            "statement": "Understand the structure and semantic meaning of HTML elements"
        },
        {
            "id": "lo-002",
            "statement": "Create styled web pages using CSS layouts and styling techniques"
        },
        {
            "id": "lo-003",
            "statement": "Implement interactive features using vanilla JavaScript"
        },
        {
            "id": "lo-004",
            "statement": "Debug and optimize web applications for performance"
        }
    ],
    "estimatedHours": 8,
    "units": [
        {
            "id": "unit-001",
            "title": "HTML Fundamentals",
            "sequence": 1,
            "topics": [
                {
                    "id": "topic-001",
                    "title": "Introduction to HTML",
                    "sequence": 1,
                    "contentFile": "units/unit-001/topic-001.md"
                },
                {
                    "id": "topic-002",
                    "title": "HTML Elements and Structure",
                    "sequence": 2,
                    "contentFile": "units/unit-001/topic-002.md"
                },
                {
                    "id": "topic-003",
                    "title": "Forms and Input Elements",
                    "sequence": 3,
                    "contentFile": "units/unit-001/topic-003.md"
                }
            ]
        },
        {
            "id": "unit-002",
            "title": "CSS Styling and Layouts",
            "sequence": 2,
            "topics": [
                {
                    "id": "topic-001",
                    "title": "CSS Selectors and Properties",
                    "sequence": 1,
                    "contentFile": "units/unit-002/topic-001.md"
                },
                {
                    "id": "topic-002",
                    "title": "CSS Box Model and Layouts",
                    "sequence": 2,
                    "contentFile": "units/unit-002/topic-002.md"
                }
            ]
        },
        {
            "id": "unit-003",
            "title": "JavaScript Basics",
            "sequence": 3,
            "topics": [
                {
                    "id": "topic-001",
                    "title": "JavaScript Fundamentals",
                    "sequence": 1,
                    "contentFile": "units/unit-003/topic-001.md"
                }
            ]
        }
    ],
    "assessments": [
        {
            "id": "assessment-001",
            "type": "quiz",
            "title": "HTML Fundamentals Quiz",
            "passingScore": 75,
            "questions": 10,
            "relatedUnit": "unit-001"
        },
        {
            "id": "assessment-002",
            "type": "project",
            "title": "Personal Portfolio Website",
            "description": "Build a responsive personal portfolio website using HTML, CSS, and JavaScript",
            "relatedUnit": "unit-003"
        }
    ],
    "resources": [
        {
            "id": "resource-001",
            "type": "external-link",
            "title": "MDN Web Docs - HTML",
            "url": "https://developer.mozilla.org/en-US/docs/Web/HTML"
        },
        {
            "id": "resource-002",
            "type": "external-link",
            "title": "CSS-Tricks",
            "url": "https://css-tricks.com"
        },
        {
            "id": "resource-003",
            "type": "download",
            "title": "HTML/CSS/JS Quick Reference",
            "url": "assets/web-dev-cheatsheet.pdf"
        }
    ],
    "tags": ["web-development", "html", "css", "javascript", "beginner"],
    "difficulty": "beginner",
    "relatedModules": ["module-002", "module-003"]
}

# Example learning path
example_learning_path = {
    "id": "path-001",
    "title": "Complete Web Development Bootcamp",
    "description": "A comprehensive learning path to master modern web development from fundamentals to advanced techniques.",
    "version": "1.0.0",
    "status": "published",
    "createdDate": "2025-01-01T00:00:00Z",
    "lastModified": "2025-01-15T10:30:00Z",
    "author": "Content Team",
    "targetAudience": "Beginners to Intermediate Developers",
    "estimatedHours": 40,
    "difficultyLevel": "beginner",
    "modules": [
        {
            "id": "module-001",
            "title": "Web Development Fundamentals",
            "sequence": 1,
            "required": True,
            "estimatedHours": 8
        },
        {
            "id": "module-002",
            "title": "Responsive Web Design",
            "sequence": 2,
            "required": True,
            "estimatedHours": 6
        },
        {
            "id": "module-003",
            "title": "JavaScript Advanced Concepts",
            "sequence": 3,
            "required": True,
            "estimatedHours": 8
        },
        {
            "id": "module-004",
            "title": "Frontend Frameworks",
            "sequence": 4,
            "required": False,
            "estimatedHours": 10
        },
        {
            "id": "module-005",
            "title": "Backend Basics",
            "sequence": 5,
            "required": False,
            "estimatedHours": 8
        }
    ],
    "prerequisites": [],
    "outcomes": [
        "Master HTML, CSS, and JavaScript fundamentals",
        "Create responsive and accessible web pages",
        "Implement interactive web applications",
        "Understand modern web development practices",
        "Deploy and maintain web applications"
    ],
    "capstone": {
        "id": "capstone-001",
        "title": "Full-Stack Web Application Project",
        "description": "Build and deploy a complete web application demonstrating mastery of frontend and backend concepts",
        "type": "project",
        "estimatedHours": 20
    }
}

if __name__ == "__main__":
    # This file serves as an example reference
    # Not intended to be executed directly
    print("Example Content Management Structures")
    print("=" * 50)
    print("\n1. Module Example:")
    print(json.dumps(example_module, indent=2))
    print("\n2. Learning Path Example:")
    print(json.dumps(example_learning_path, indent=2))
