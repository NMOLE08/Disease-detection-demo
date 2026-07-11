"""
This module provides a simple interface for making predictions with the trained model.
"""
import os
import sys

# Add the project root directory to the Python path
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
    print(f"[DEBUG] Added to Python path: {project_root}")

# Add the Crop_Sensei directory to Python path
crop_sensei_dir = os.path.join(project_root, 'Crop_Sensei')
if os.path.exists(crop_sensei_dir) and crop_sensei_dir not in sys.path:
    sys.path.insert(0, crop_sensei_dir)
    print(f"[DEBUG] Added to Python path: {crop_sensei_dir}")

print("\n[DEBUG] Current Python path in predictor.py:")
for p in sys.path[:5]:  # Only print first 5 paths to avoid cluttering the output
    print(f"- {p}")
print("...")

try:
    # Now import the predictor
    from Crop_Sensei.scripts.predict import CropDiseasePredictor
    print("[DEBUG] Successfully imported CropDiseasePredictor")
except ImportError as e:
    print(f"[ERROR] Failed to import CropDiseasePredictor: {e}")
    import traceback
    traceback.print_exc()
    raise

# Initialize the predictor
predictor = None

def init_predictor(model_path):
    """Initialize the predictor with the given model path."""
    global predictor
    try:
        print("\n" + "="*50)
        print("INITIALIZING PREDICTOR")
        print("="*50)
        
        print(f"\n[INFO] Model path: {model_path}")
        print(f"[INFO] Current working directory: {os.getcwd()}")
        print(f"[INFO] Model file exists: {os.path.exists(model_path)}")
        
        if not os.path.exists(model_path):
            print(f"\n[ERROR] Model file not found at: {model_path}")
            print("Please check if the model file exists and the path is correct.")
            return False
        
        # Check CUDA availability
        print("\n[INFO] Checking CUDA availability...")
        cuda_available = torch.cuda.is_available()
        print(f"[INFO] CUDA available: {cuda_available}")
        
        if cuda_available:
            print(f"[INFO] CUDA device count: {torch.cuda.device_count()}")
            print(f"[INFO] Current CUDA device: {torch.cuda.current_device()}")
            print(f"[INFO] CUDA device name: {torch.cuda.get_device_name(0)}")
        
        # Initialize the predictor
        print("\n[INFO] Initializing CropDiseasePredictor...")
        try:
            predictor = CropDiseasePredictor(model_path)
            print(f"[SUCCESS] Model loaded successfully from {model_path}")
            print(f"[INFO] Predictor device: {predictor.device}")
            return True
        except Exception as e:
            print(f"\n[ERROR] Failed to initialize CropDiseasePredictor: {e}")
            print("Possible causes:")
            print("1. Model architecture mismatch with saved weights")
            print("2. Incompatible PyTorch version")
            print("3. Corrupted model file")
            import traceback
            traceback.print_exc()
            return False
            
    except Exception as e:
        print(f"\n[ERROR] Unexpected error in init_predictor: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        print("\n" + "="*50 + "\n")

def get_predictor():
    """Get the initialized predictor instance."""
    return predictor
