#!/usr/bin/env python3
"""
Content Structure Validation Script

Validates the hierarchical structure of content:
Learning Path → Modules → Units → Topics
"""

import json
import sys
from pathlib import Path
from collections import defaultdict


def validate_structure():
    """Validate content directory structure."""
    errors = []
    warnings = []
    
    # Expected directory structure
    required_dirs = [
        'content/learning-paths',
        'content/modules/metadata',
        'content/modules/units',
        'content/assets/images',
        'content/assets/videos'
    ]
    
    content_root = Path('content')
    
    if not content_root.exists():
        print("❌ Content directory does not exist")
        return 1
    
    # Check required directories
    for dir_path in required_dirs:
        if not Path(dir_path).exists():
            errors.append(f"Missing required directory: {dir_path}")
    
    # Validate learning paths
    paths_dir = Path('content/learning-paths')
    if paths_dir.exists():
        for path_file in paths_dir.glob('*.json'):
            if 'template' in path_file.name:
                continue
            
            try:
                with open(path_file, 'r', encoding='utf-8') as f:
                    path_data = json.load(f)
                
                # Check for required fields
                required_fields = ['id', 'title', 'modules']
                for field in required_fields:
                    if field not in path_data:
                        errors.append(f"Learning path {path_file.name}: missing field '{field}'")
                
                # Validate module references
                referenced_modules = []
                for module in path_data.get('modules', []):
                    if 'id' in module:
                        referenced_modules.append(module['id'])
                
                # Check that referenced modules exist
                modules_dir = Path('content/modules/metadata')
                existing_modules = set()
                if modules_dir.exists():
                    for module_file in modules_dir.glob('*.json'):
                        if 'template' not in module_file.name:
                            try:
                                with open(module_file) as f:
                                    module_data = json.load(f)
                                    existing_modules.add(module_data.get('id'))
                            except:
                                pass
                
                for module_id in referenced_modules:
                    if module_id not in existing_modules and existing_modules:
                        warnings.append(
                            f"Learning path {path_file.name}: "
                            f"references non-existent module '{module_id}'"
                        )
                
                print(f"✅ {path_file.name}")
            
            except json.JSONDecodeError as e:
                errors.append(f"Learning path {path_file.name}: invalid JSON - {e}")
    
    # Validate modules
    modules_dir = Path('content/modules/metadata')
    if modules_dir.exists():
        for module_file in modules_dir.glob('*.json'):
            if 'template' in module_file.name:
                continue
            
            try:
                with open(module_file, 'r', encoding='utf-8') as f:
                    module_data = json.load(f)
                
                # Check for required fields
                required_fields = ['id', 'title', 'learningOutcomes']
                for field in required_fields:
                    if field not in module_data:
                        errors.append(f"Module {module_file.name}: missing field '{field}'")
                
                # Validate units reference
                units = module_data.get('units', [])
                for unit in units:
                    if 'id' not in unit:
                        warnings.append(f"Module {module_file.name}: unit missing 'id' field")
                
                print(f"✅ {module_file.name}")
            
            except json.JSONDecodeError as e:
                errors.append(f"Module {module_file.name}: invalid JSON - {e}")
    
    # Check for orphaned content
    units_dir = Path('content/modules/units')
    if units_dir.exists():
        unit_files = list(units_dir.glob('**/*.md'))
        if unit_files:
            print(f"✅ Found {len(unit_files)} unit content files")
    
    # Report results
    print("\n" + "="*50)
    print("Content Structure Validation")
    
    if errors:
        print(f"\n❌ Errors ({len(errors)}):")
        for error in errors:
            print(f"  {error}")
    
    if warnings:
        print(f"\n⚠️  Warnings ({len(warnings)}):")
        for warning in warnings:
            print(f"  {warning}")
    
    if not errors:
        print("\n✅ Content structure validation passed!")
        return 0
    else:
        return 1


if __name__ == "__main__":
    sys.exit(validate_structure())
