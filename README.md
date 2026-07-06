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
- <img width="735" height="588" alt="plastic_045 (1)" src="https://github.com/user-attachments/assets/e22eec41-0f30-47cb-9257-6e81b9f1d1d4" />
  <img width="500" height="333" alt="wood_080" src="https://github.com/user-attachments/assets/fa07a1e6-4925-4bc0-93e9-cb1f73e55100" />
  <img width="447" height="447" alt="aluminum_024" src="https://github.com/user-attachments/assets/c2c8f905-bdb3-4841-ad7b-a2b825c6cf01" />
  <img width="505" height="380" alt="steel_012" src="https://github.com/user-attachments/assets/8ddc2abf-6763-4ff4-a016-22655ec32a6f" />


### 🏁 Outcome
The model successfully detects multiple types of formwork with good accuracy and can be extended for real-world construction site automation systems.
