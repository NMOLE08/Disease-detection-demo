import os
import sys

def debug_imports():
    print("=== DEBUGGING IMPORTS ===\n")
    
    # Print current working directory
    print(f"Current working directory: {os.getcwd()}")
    
    # Print Python version
    print(f"\nPython version: {sys.version}")
    
    # Print Python path
    print("\nPython path:")
    for i, path in enumerate(sys.path):
        print(f"{i+1}. {path}")
    
    # Try to import required modules
    print("\n=== TESTING IMPORTS ===\n")
    
    modules = [
        'torch',
        'torchvision',
        'albumentations',
        'numpy',
        'PIL',
        'flask',
        'werkzeug',
        'Crop_Sensei.scripts.predict',
        'Crop_Sensei.scripts.model'
    ]
    
    for module in modules:
        try:
            print(f"Importing {module}...")
            if module == 'PIL':
                __import__('PIL')
            else:
                __import__(module)
            print(f"✅ Successfully imported {module}\n")
        except ImportError as e:
            print(f"❌ Failed to import {module}: {e}")
            import traceback
            traceback.print_exc()
            print()
        except Exception as e:
            print(f"❌ Error importing {module}: {e}")
            import traceback
            traceback.print_exc()
            print()

if __name__ == "__main__":
    debug_imports()
