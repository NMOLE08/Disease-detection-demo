import os
import sys

def test_imports():
    print("Testing imports...")
    
    # Add the project root to Python path
    project_root = os.path.dirname(os.path.abspath(__file__))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    
    # Try to import the predictor module
    try:
        print("\nAttempting to import from scripts.predict...")
        from Crop_Sensei.scripts.predict import CropDiseasePredictor
        print("Successfully imported CropDiseasePredictor")
        return True
    except ImportError as e:
        print(f"Error importing CropDiseasePredictor: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_imports()
