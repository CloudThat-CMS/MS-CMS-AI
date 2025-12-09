#!/usr/bin/env python3
"""
Metadata Validation Script

Validates all metadata JSON files against defined schemas.
"""

import json
import os
import sys
from pathlib import Path
from jsonschema import validate, ValidationError

# Schema definitions
MODULE_SCHEMA = {
    "type": "object",
    "required": ["id", "title", "description", "version", "status", "learningOutcomes"],
    "properties": {
        "id": {"type": "string", "pattern": "^module-[0-9]{3,}$"},
        "title": {"type": "string", "minLength": 5, "maxLength": 200},
        "description": {"type": "string", "minLength": 10},
        "version": {"type": "string", "pattern": "^[0-9]+\\.[0-9]+\\.[0-9]+$"},
        "status": {"enum": ["draft", "review", "published", "archived"]},
        "createdDate": {"type": "string", "format": "date-time"},
        "lastModified": {"type": "string", "format": "date-time"},
        "author": {"type": "string"},
        "reviewedBy": {"type": "string"},
        "learningPath": {"type": "string"},
        "prerequisites": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["moduleId"],
                "properties": {
                    "moduleId": {"type": "string"},
                    "title": {"type": "string"}
                }
            }
        },
        "learningOutcomes": {
            "type": "array",
            "minItems": 1,
            "items": {
                "type": "object",
                "required": ["id", "statement"],
                "properties": {
                    "id": {"type": "string"},
                    "statement": {"type": "string"}
                }
            }
        },
        "estimatedHours": {"type": "number", "minimum": 0},
        "units": {
            "type": "array",
            "items": {"type": "object"}
        },
        "tags": {"type": "array", "items": {"type": "string"}},
        "difficulty": {"enum": ["beginner", "intermediate", "advanced"]}
    }
}

LEARNING_PATH_SCHEMA = {
    "type": "object",
    "required": ["id", "title", "description", "version", "status", "modules"],
    "properties": {
        "id": {"type": "string", "pattern": "^path-[0-9]{3,}$"},
        "title": {"type": "string", "minLength": 5},
        "description": {"type": "string", "minLength": 10},
        "version": {"type": "string", "pattern": "^[0-9]+\\.[0-9]+\\.[0-9]+$"},
        "status": {"enum": ["draft", "review", "published", "archived"]},
        "modules": {"type": "array", "minItems": 1},
        "estimatedHours": {"type": "number", "minimum": 0},
        "difficultyLevel": {"enum": ["beginner", "intermediate", "advanced"]},
        "outcomes": {"type": "array", "items": {"type": "string"}}
    }
}


def validate_metadata(file_path, schema):
    """Validate a single metadata file against schema."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        validate(instance=data, schema=schema)
        return True, "Valid"
    except json.JSONDecodeError as e:
        return False, f"JSON parsing error: {str(e)}"
    except ValidationError as e:
        return False, f"Schema validation failed: {e.message}"
    except Exception as e:
        return False, f"Error: {str(e)}"


def main():
    """Run metadata validation for all files."""
    errors = []
    warnings = []
    success_count = 0

    # Validate module metadata
    modules_dir = Path("content/modules/metadata")
    if modules_dir.exists():
        for file_path in modules_dir.glob("*.json"):
            if "template" in file_path.name:
                continue
            
            valid, message = validate_metadata(str(file_path), MODULE_SCHEMA)
            if valid:
                success_count += 1
                print(f"✅ {file_path.name}")
            else:
                errors.append(f"❌ {file_path.name}: {message}")

    # Validate learning path metadata
    paths_dir = Path("content/learning-paths")
    if paths_dir.exists():
        for file_path in paths_dir.glob("*.json"):
            if "template" in file_path.name:
                continue
            
            valid, message = validate_metadata(str(file_path), LEARNING_PATH_SCHEMA)
            if valid:
                success_count += 1
                print(f"✅ {file_path.name}")
            else:
                errors.append(f"❌ {file_path.name}: {message}")

    # Report results
    print("\n" + "="*50)
    print(f"Validation Summary: {success_count} passed")
    
    if errors:
        print(f"\nErrors found ({len(errors)}):")
        for error in errors:
            print(f"  {error}")
        return 1
    
    if warnings:
        print(f"\nWarnings ({len(warnings)}):")
        for warning in warnings:
            print(f"  {warning}")
    
    print("\n✅ All metadata validation passed!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
