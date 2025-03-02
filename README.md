# Pediatric Pneumonia Classification Using CNN on Chest X-Rays

## Overview
Pneumonia is a serious lung infection that is a leading cause of illness and death in children worldwide. This project leverages **Convolutional Neural Networks (CNNs)** to develop an automated classification system for detecting pneumonia using pediatric chest X-ray images. The goal is to provide an **accurate, accessible, and efficient** diagnostic tool to aid healthcare professionals.

## Features
- ✅ **Preprocessed Chest X-ray Dataset** (Normalization & Augmentation)
- ✅ **CNN Architectures** (VGG16, ResNet, EfficientNet)
- ✅ **Transfer Learning & Hyperparameter Optimization**
- ✅ **Performance Evaluation** (Accuracy, Precision, Recall, AUC-ROC)
- ✅ **Streamlit Web App** for Real-Time X-ray Classification

## Dataset
- The dataset used in this project consists of **pediatric chest X-ray images** labeled as **Normal** or **Pneumonia**.
- Due to size constraints, the dataset is not included in this repository. It can be downloaded from **[Kaggle](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia)**.

## Project Structure
```
Pediatric-Pneumonia-CNN/
│── data/                  # Dataset (not included due to size)
│── notebooks/             # Jupyter notebooks for EDA, training, and evaluation
│── models/                # Trained CNN models
│── app/                   # Streamlit-based web app
│── requirements.txt       # Dependencies
│── README.md              # Project documentation
```

## Installation & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/Pediatric-Pneumonia-CNN.git
cd Pediatric-Pneumonia-CNN
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Web App
```bash
streamlit run app/app.py
```

### 4. Upload a chest X-ray image
The web app will process the image and provide a classification result (**Normal** or **Pneumonia**).

## Model Performance
- Trained **CNN-based models** achieved **high classification accuracy**.
- Performance evaluated using **precision, recall, F1-score, and AUC-ROC**.
- Error analysis conducted to improve predictions.

## Future Enhancements
- 📌 Expand dataset for better generalization.
- 📌 Integrate explainability techniques (e.g., **Grad-CAM**) for model transparency.
- 📌 Deploy as a **cloud-based API** for wider accessibility.

## Contributing
🚀 **Contributions are welcome!** Feel free to fork the repo, submit pull requests, or suggest improvements.

## License
This project is licensed under the **MIT License**.

---
**🌟 If you find this project useful, don't forget to star the repository!** ⭐
# Pediatric-Pneumonia-Classification-with-Convolutional-Neural-Networks-Models-on-Chest-X-Rays
