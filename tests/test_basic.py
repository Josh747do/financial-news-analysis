"""
Basic tests for the financial analysis project
"""
import pandas as pd
import numpy as np
import os

def test_imports():
    """Test that all required packages can be imported"""
    try:
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt
        import seaborn as sns
        assert True
    except ImportError as e:
        assert False, f"Import error: {e}"

def test_data_structure():
    """Test that project structure exists"""
    assert os.path.exists('data'), "Data directory should exist"
    assert os.path.exists('notebooks'), "Notebooks directory should exist"
    assert os.path.exists('src'), "Source directory should exist"
    assert os.path.exists('requirements.txt'), "Requirements file should exist"

def test_requirements():
    """Test that requirements file exists and has content"""
    if os.path.exists('requirements.txt'):
        with open('requirements.txt', 'r') as f:
            content = f.read()
            assert len(content) > 0, "Requirements file should not be empty"
            assert 'pandas' in content, "Requirements should include pandas"
    else:
        assert False, "requirements.txt should exist"

if __name__ == "__main__":
    test_imports()
    test_data_structure()
    test_requirements()
    print("✅ All basic tests passed!")