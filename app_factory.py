import os
import sys
from flask import Flask, request, jsonify, render_template, redirect, url_for
from werkzeug.utils import secure_filename

def create_app():
    # Add the project root to the Python path
    project_root = os.path.dirname(os.path.abspath(__file__))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    
    print("=" * 80)
    print(f"Project root: {project_root}")
    print("Python path:")
    for i, path in enumerate(sys.path[:10]):
        print(f"{i+1}. {path}")
    if len(sys.path) > 10:
        print(f"... and {len(sys.path) - 10} more paths")
    print("=" * 80)

    # Now import the predictor module
    try:
        print("\nAttempting to import predictor module...")
        print("✅ Successfully imported predictor module")
    except ImportError as e:
        print(f"❌ Failed to import predictor module: {e}")
        import traceback
        traceback.print_exc()
        # Don't raise here, as we might want to run the app without the predictor in development

    # Create the Flask app with correct template and static folders
    app = Flask(__name__, 
                template_folder=os.path.join(project_root, 'frontend', 'html'),
                static_folder=os.path.join(project_root, 'static'))
                
    # Add a custom template loader to also look in the root directory
    from jinja2 import FileSystemLoader
    my_loader = FileSystemLoader([
        os.path.join(project_root, 'frontend', 'html'),
        project_root  # Add root directory as a fallback
    ])
    app.jinja_loader = my_loader
    
    # Ensure the upload folder exists
    upload_folder = os.path.join(project_root, 'static', 'uploads')
    os.makedirs(upload_folder, exist_ok=True)
    
    # Configure the app
    app.config['UPLOAD_FOLDER'] = upload_folder
    app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
    # Import and register blueprints or routes here if needed
    from flask import render_template
    
    @app.route('/')
    def home():
        return render_template('index.html')
        
    @app.route('/upload')
    def upload_page():
        return render_template('upload_page.html')
    
    def allowed_file(filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

    @app.route('/predict', methods=['POST'])
    def predict():
        # Check if the post request has the file part
        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400
        
        file = request.files['file']
        
        # If user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        
        if file and allowed_file(file.filename):
            # Save the uploaded file
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Here you would typically call your prediction function
            # For now, we'll just return a success message with the file path
            return jsonify({
                "status": "success",
                "message": "File uploaded successfully",
                "filename": filename,
                "filepath": filepath
            })
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000)
