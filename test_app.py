import io
import os
import sys
import unittest
import tempfile
import shutil
from unittest.mock import patch, MagicMock

# Add the project root to the Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

class TestCropSensei(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up test environment."""
        # Create a temporary directory for test uploads
        cls.test_dir = tempfile.mkdtemp()
        
        # Mock the predictor to avoid loading the actual model during tests
        cls.predictor_patcher = patch('predictor.CropDiseasePredictor')
        cls.mock_predictor_class = cls.predictor_patcher.start()
        cls.mock_predictor = cls.mock_predictor_class.return_value
        cls.mock_predictor.predict.return_value = {
            'class': 'Healthy',
            'confidence': 0.95,
            'probabilities': {'Blight': 0.01, 'Common_Rust': 0.02, 'Gray_Leaf_Spot': 0.02, 'Healthy': 0.95}
        }

    @classmethod
    def tearDownClass(cls):
        """Clean up after tests."""
        # Clean up the temporary directory
        shutil.rmtree(cls.test_dir)
        # Stop all patches
        cls.predictor_patcher.stop()

    def setUp(self):
        """Set up test client for each test."""
        from app_factory import create_app
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['UPLOAD_FOLDER'] = self.test_dir
        self.client = self.app.test_client()

    def test_home_route(self):
        """Test the home route."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'CropSensei', response.data)  # Assuming 'CropSensei' is in your index.html

    def test_upload_page_route(self):
        """Test the upload page route."""
        response = self.client.get('/upload')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Upload Image', response.data)  # Assuming 'Upload Image' is in your upload_page.html

    def test_predict_route_no_file(self):
        """Test the predict route with no file."""
        response = self.client.post('/predict')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'No file part', response.data)

    def test_predict_route_empty_file(self):
        """Test the predict route with an empty file."""
        data = {'file': (None, '')}
        response = self.client.post('/predict', data=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'No selected file', response.data)

    def test_predict_route_invalid_file_type(self):
        """Test the predict route with an invalid file type."""
        data = {'file': (io.BytesIO(b'test'), 'test.txt')}
        response = self.client.post('/predict', data=data, content_type='multipart/form-data')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'File type not allowed', response.data)

    @patch('os.path.exists', return_value=True)
    def test_predict_route_success(self, mock_exists):
        """Test the predict route with a valid image file."""
        # Create a test image
        from PIL import Image
        import io
        
        # Create a simple image
        img = Image.new('RGB', (100, 100), color='green')
        img_io = io.BytesIO()
        img.save(img_io, 'JPEG')
        img_io.seek(0)
        
        # Test the predict route
        data = {'file': (img_io, 'test.jpg')}
        response = self.client.post(
            '/predict',
            data=data,
            content_type='multipart/form-data'
        )
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'success', response.data.lower())
        self.assertIn(b'prediction', response.data.lower())
        self.assertIn(b'confidence', response.data.lower())

    def test_predictor_initialization(self):
        """Test the predictor initialization."""
        from predictor import init_predictor, get_predictor
        
        # Test with a dummy model path
        test_model_path = os.path.join(project_root, 'test_model.pth')
        
        # Create a dummy model file
        with open(test_model_path, 'w') as f:
            f.write('dummy model data')
        
        # Test initialization
        result = init_predictor(test_model_path)
        self.assertTrue(result)
        
        # Test get_predictor
        predictor = get_predictor()
        self.assertIsNotNone(predictor)
        
        # Clean up
        os.remove(test_model_path)

if __name__ == '__main__':
    unittest.main()
