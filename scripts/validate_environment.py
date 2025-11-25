#!/usr/bin/env python3
"""
Environment validation script for CI/CD
"""
import sys
import importlib

def check_import(package_name):
    """Check if a package can be imported"""
    try:
        importlib.import_module(package_name)
        print(f"✅ {package_name}")
        return True
    except ImportError:
        print(f"❌ {package_name}")
        return False

def main():
    print("🔍 Validating Project Environment...")
    
    # Required packages
    required_packages = [
        'pandas',
        'numpy', 
        'matplotlib',
        'seaborn',
        'jupyter',
        'textblob'
    ]
    
    print("\n📦 Checking required packages:")
    all_imported = True
    for package in required_packages:
        if not check_import(package):
            all_imported = False
    
    # Check project structure
    print("\n📁 Checking project structure:")
    import os
    required_dirs = ['data', 'notebooks', 'src', 'tests', 'scripts']
    for dir_name in required_dirs:
        if os.path.exists(dir_name):
            print(f"✅ {dir_name}/")
        else:
            print(f"❌ {dir_name}/")
            all_imported = False
    
    # Check for notebooks
    notebooks = [f for f in os.listdir('notebooks') if f.endswith('.ipynb')]
    if notebooks:
        print(f"✅ Found {len(notebooks)} notebooks")
    else:
        print("❌ No notebooks found")
        all_imported = False
    
    if all_imported:
        print("\n🎉 All checks passed! Environment is ready.")
        sys.exit(0)
    else:
        print("\n⚠️ Some checks failed. Please review the setup.")
        sys.exit(1)

if __name__ == "__main__":
    main()