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
