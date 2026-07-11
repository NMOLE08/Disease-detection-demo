import os
import sys

# Set up the Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

# Print debug information
print("=" * 80)
print(f"Current working directory: {os.getcwd()}")
print(f"Project root: {project_root}")
print("\nPython path:")
for i, path in enumerate(sys.path[:10]):
    print(f"{i+1}. {path}")
if len(sys.path) > 10:
    print(f"... and {len(sys.path) - 10} more paths")
print("\n")

# Try to import the Flask app
try:
    print("Attempting to import Flask app...")
    from Crop_Sensei.app import app
    print("✅ Successfully imported Flask app")
    
    # Run the Flask app
    if __name__ == "__main__":
        print("\nStarting Flask development server...")
        app.run(debug=True, port=5000)
        
except Exception as e:
    print("\n❌ ERROR: Failed to import or run Flask app")
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
    print("\nPlease check the following:")
    print("1. The app.py file exists in the Crop_Sensei directory")
    print("2. All required dependencies are installed")
    print("3. The Python path includes the project directories")
    print("=" * 80)
