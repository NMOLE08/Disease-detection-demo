# CropSensei 🌿

**CropSensei** is an end-to-end deep learning web application designed to automatically detect and classify plant diseases from leaf images. By leveraging state-of-the-art convolutional neural networks (EfficientNetB3 and ResNet50), it helps farmers and agricultural professionals quickly identify crop health issues and take actionable steps.

## ✨ Features
- **Accurate Disease Detection**: Classifies leaf images into specific disease categories like Grey Leaf Spot, Common Rust, Blight, etc.
- **Deep Learning Engine**: Built with PyTorch, utilizing an ensemble of EfficientNetB3 and ResNet50 for high accuracy.
- **Interactive Web Interface**: A user-friendly Flask-based web application to upload images and get instant predictions.
- **Detailed Analytics**: Generates performance plots, confusion matrices, and class distribution insights.

## 🗂️ Dataset Information
The dataset consists of high-resolution images of crop leaves located under `static/leaf_images/`. The class labels are stored in `Database.csv` with the format:
`image_id, image_file_path, image_class_label`

### Supported Classes
| ID | Class Name | Description |
|---|---|---|
| 1 | Grey Leaf Spot | Fungal disease affecting leaves |
| 2 | Northern Corn Leaf Blight | Fungal disease causing lesions |
| 3 | Phaeosphaeria Leaf Spot | Fungal leaf spot |
| 4 | Common Rust | Rust fungus |
| 5 | Southern Rust | Rust fungus |
| 6 | Healthy | No diseases detected |
| 7 | Other | Excessive tearing, insect damage, etc. |
| 8 | Unknown | Unidentified leaf disease |

*Note: A single image can contain multiple labels.*

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit) (optional, for GPU acceleration)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/CropSensei.git
   cd CropSensei
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r Crop_Sensei/scripts/requirements.txt
   ```

### Running the Application

Start the Flask web server by running the entry point script:

```bash
python run_app.py
```
Then, open your web browser and navigate to `http://127.0.0.1:5000` to access the Dr. Crop dashboard.

## 🧠 Model Architecture & Training

The machine learning pipeline is located under `Crop_Sensei/scripts/`.

- **Main Model:** EfficientNetB3
- **Baseline Model:** ResNet50
- **Ensemble:** Predictions can be combined for improved robust accuracy.

To train or evaluate the models from scratch:
```bash
# Evaluate models
python Crop_Sensei/scripts/evaluate_models.py

# Evaluate ensemble performance
python Crop_Sensei/scripts/evaluate_ensembles.py
```

Performance metrics and visual plots (confusion matrices, dataset distributions) are automatically saved to the `outputs/plots/` directory.

## 📁 Repository Structure

```text
CropSensei/
├── Crop_Sensei/          # PyTorch ML Engine
│   ├── scripts/          # Training, inference, and evaluation scripts
│   ├── models/           # Saved model weights (.pth)
│   └── data/             # Dataset processing files
├── frontend/             # Frontend HTML/CSS templates
├── static/               # Uploaded images, CSS, and dataset images
├── outputs/              # Model performance plots and analytics
├── app_factory.py        # Flask application factory
├── run_app.py            # Main entry script to run the web server
└── predictor.py          # PyTorch inference wrapper
```

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
