# Multi-Class-Formwork-Detection-Using-YOLO11s


## 📌 Project Summary

This project focuses on building a **multi-class formwork detection system** using the YOLO11 object detection model. The goal is to automatically identify different types of construction formwork materials from images, which is highly useful in construction monitoring, safety inspection, and automation tasks.

### 🧠 Problem Statement
Manual identification of formwork types in construction sites is time-consuming and error-prone. This project automates the detection process using deep learning.

### 📊 Dataset
The dataset contains labeled images of 6 classes:
- Wood Formwork  
- Plywood Formwork  
- Steel Formwork  
- Aluminium Formwork  
- Plastic Formwork  
- Coffor Formwork  

The dataset was manually annotated using LabelImg and structured into train, validation, and test sets.

## 📁 Project Structure

```text
Formwork-Detection-Using-YOLO11/

├── datasets/
│   ├── images/
│   │   ├── train/              # Training images
│   │   ├── val/                # Validation images
│   │   └── test/               # Test images
│   │
│   ├── labels/
│   │   ├── train/              # YOLO training labels
│   │   ├── val/                # YOLO validation labels
│   │   └── test/               # YOLO test labels
│   │
│   ├── classes.txt             # List of formwork classes
│   └── data.yaml               # Dataset configuration
│
├── demo/
│   ├── aluminum_024.jpg        # Aluminium formwork prediction
│   ├── coffor_003.jpg          # Coffor formwork prediction
│   ├── plastic_045.jpg         # Plastic formwork prediction
│   ├── steel_012.jpg           # Steel formwork prediction
│   └── wood_080.jpg            # Wood formwork prediction
│
├── models/
│   └── best.pt                 # Trained YOLO11 model weights
│
├── notebooks/
│   └── formwork-detection.ipynb # Complete training notebook
│
├── results/
│   ├── results.png             # Training metrics visualization
│   ├── results.csv             # Training log
│   ├── confusion_matrix.png    # Confusion matrix
│   ├── BoxF1_curve.png         # F1 score curve
│   ├── BoxPR_curve.png         # Precision–Recall curve
│   ├── BoxP_curve.png          # Precision curve
│   └── BoxR_curve.png          # Recall curve
│
├── scripts/
│   ├── inference.py            # Run inference on images/folders
│   ├── merge_dataset.py        # Merge labeled datasets
│   ├── find_missing_labels.py  # Detect missing annotations
│   └── check_predictions.py    # Visualize prediction results
│
├── README.md                   # Project documentation
├── requirements.txt            # Python dependencies
└── LICENSE                     # Project license (optional)
```
### ⚙️ Methodology
- Model: YOLO11s (Ultralytics)
- Training: 200 epochs with AdamW optimizer
- Image size: 640x640
- Augmentation: Auto YOLO augmentations
- Evaluation: Precision, Recall, mAP@50, mAP@50-95

### 📈 Results
- Precision: ~0.88  
- Recall: ~0.52  
- mAP@50: ~0.59  
- mAP@50-95: ~0.51  

### 🔍 Key Features
- Real-time object detection capability
- High-confidence filtering for better predictions
- Visual evaluation using PR curves and confusion matrix
- Custom dataset pipeline with YOLO format

- ### ▶️ Demo Images

<div style="display:flex; flex-wrap:wrap; gap:10px; justify-content:center;">

  <img src="https://github.com/user-attachments/assets/afd5c1fb-ee23-49ba-9676-b0b327098ace" width="48%" />
  <img src="https://github.com/user-attachments/assets/d795f13b-9002-42b6-bb1d-51a35f338308" width="48%" />

  <img src="https://github.com/user-attachments/assets/e9b4aa96-e545-40bf-b2d6-6aeb16933f37" width="48%" />
  <img src="https://github.com/user-attachments/assets/38d90c9d-1716-45e4-819d-37d0be02b95d" width="48%" />

</div>


### 🏁 Outcome
The model successfully detects multiple types of formwork with good accuracy and can be extended for real-world construction site automation systems.
