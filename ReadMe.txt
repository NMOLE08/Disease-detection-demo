The image data is contained under static/leaf_images/*
These are the high resolution, original images. Feel free to resize them as you please.

Accompanying these image files is a CSV titled "Database2020.csv" which contains the class labels for the dataset. 
It follows the following format:
image_id, image_file_path, image_class_label.

A single image can contain multiple labels and this is reflected in the csv through multiple rows for the same image. For example:
1220,/static/leaf_images/2009-03-24 Maize GLS images (Baynesfield KZN)/110_CIMG3846_1-109-1.JPG,1
1220,/static/leaf_images/2009-03-24 Maize GLS images (Baynesfield KZN)/110_CIMG3846_1-109-1.JPG,2

Classes are identified using numerical values and these correspond to diseases/other features in the following way:
1,'Grey Leaf Spot'
2,'Northern Corn Leaf Blight'
3,'Phaeosphaeria Leaf Spot'
4,'Common Rust'
5,'Southern Rust'
6,'Healthy'
7,'Other'
8,'Unknown'

Classes 7 and 8 may require additional clarification. 'Other' refers to an additional feature that is not listed here. This may refer to excessive leaf tearing, presence of insects and insect damage. 'Unknown' refers to the case where a maize leaf is believed to have a disease that does not belong to those listed.

# CropSensei - Plant Disease Classification

## Project Summary

### Dataset
- **Total Images**: [Total number of images]
- **Classes**:
  - Blight: [count] images
  - Common_Rust: [count] images
  - Gray_Leaf_Spot: [count] images
  - Healthy: [count] images

### Model Performance

#### EfficientNetB3 (Main Model)
- **Mean Validation Accuracy**: [mean] ± [std]
- **Mean Validation F1-Score**: [mean] ± [std]

#### ResNet50 (Baseline)
- **Mean Validation Accuracy**: [mean] ± [std]
- **Mean Validation F1-Score**: [mean] ± [std]

#### Ensemble Performance
- **EfficientNetB3 Ensemble**:
  - Accuracy: [accuracy]
  - F1-Score: [f1_score]
- **Combined Ensemble (EfficientNetB3 + ResNet50)**:
  - Accuracy: [accuracy]
  - F1-Score: [f1_score]
- **Ensemble Improvement**: [improvement]%

### Key Visualizations
1. Class Distribution
   ![Class Distribution](outputs/plots/class_distribution.png)

2. Model Comparison
   ![Model Comparison](outputs/plots/model_comparison.png)

3. Confusion Matrices
   - [EfficientNetB3 Ensemble](outputs/plots/efficientnet_ensemble_cm.png)
   - [Combined Ensemble](outputs/plots/combined_ensemble_cm.png)

### System Information
- **CUDA Available**: [Yes/No]
- **GPU**: [GPU Name] (if available)
- **CUDA Version**: [Version] (if available)

## How to Reproduce Results

1. **Setup Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r scripts/requirements.txt