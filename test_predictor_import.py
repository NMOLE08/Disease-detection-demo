import os
import sys

def test_imports():
    print("=== TESTING PREDICTOR IMPORTS ===\n")
    
    # Add project root to Python path
    project_root = os.path.dirname(os.path.abspath(__file__))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    
    # Print Python path
    print("Python path:")
    for i, path in enumerate(sys.path[:10]):
        print(f"{i+1}. {path}")
    if len(sys.path) > 10:
        print(f"... and {len(sys.path) - 10} more paths")
    print()
    
    # Try to import the predictor module
    print("Attempting to import predictor module...")
    try:
        from predictor import init_predictor, get_predictor
        print("✅ Successfully imported predictor module directly")
        return True
    except ImportError as e:
        print(f"❌ Direct import failed: {e}")
        print("\nTrying alternative import paths...")
    
    # Try alternative import paths
    import_paths = [
        'Crop_Sensei.predictor',
        'scripts.predictor',
        'Crop_Sensei.scripts.predictor'
    ]
    
    for path in import_paths:
        try:
            module = __import__(path, fromlist=['init_predictor', 'get_predictor'])
            print(f"✅ Successfully imported using path: {path}")
            return True
        except ImportError as e:
            print(f"❌ Failed to import using {path}: {e}")
    
    print("\nAll import attempts failed. Please check the following:")
    print("1. The predictor.py file exists in the correct location")
    print("2. The Python path includes the project directories")
    print("3. All required dependencies are installed")
    return False

if __name__ == "__main__":
    test_imports()
