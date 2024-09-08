#!/usr/bin/env python3
"""
This script checks if all modules, classes, and functions in a Python file
have proper documentation (docstrings).
"""

import importlib
import sys
import inspect

def check_module(module_name):
    """
    Check if a module and its components (classes, functions) are documented.
    
    Args:
        module_name (str): The name of the module to check.

    Returns:
        bool: True if everything is documented, False if any docstrings are missing.
    """
    try:
        # Import the module dynamically
        module = importlib.import_module(module_name)

        print(f"Checking documentation for module: {module_name}")
        all_documented = True

        # Check if the module itself has a docstring
        if module.__doc__ is None:
            print(f"Missing module docstring: {module_name}")
            all_documented = False

        # Iterate over all classes and functions in the module
        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj):
                if obj.__doc__ is None:
                    print(f"Missing class docstring: {module_name}.{name}")
                    all_documented = False
                # Check methods inside the class
                for method_name, method in inspect.getmembers(obj, inspect.isfunction):
                    if method.__doc__ is None:
                        print(f"Missing method docstring: {module_name}.{name}.{method_name}")
                        all_documented = False
            elif inspect.isfunction(obj):
                if obj.__doc__ is None:
                    print(f"Missing function docstring: {module_name}.{name}")
                    all_documented = False
        
        if all_documented:
            print(f"All documentation is present for module: {module_name}")
        return all_documented

    except ModuleNotFoundError as e:
        print(f"Error importing module: {module_name}. {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./check_documentation.py <module_name>")
        sys.exit(1)

    module_name = sys.argv[1]
    if not check_module(module_name):
        sys.exit(1)
