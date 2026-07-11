"""
WSGI config for CropSensei project.

This module contains the WSGI application used by the Flask development server and any production WSGI deployments.
"""
import os
import sys

# Add the project directory to the Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

# Import the Flask app from the factory
from app_factory import create_app

# Create the Flask application
application = create_app()

if __name__ == "__main__":
    print("Starting Flask development server...")
    application.run(debug=True, port=5000)
