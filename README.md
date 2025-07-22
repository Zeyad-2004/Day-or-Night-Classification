
# 🌓 Day-or-Night Classification

A deep learning project that classifies images as **Day** or **Night** using a Convolutional Neural Network (CNN). The project also includes a **Streamlit**-based web interface that allows users to upload an image and get a real-time prediction.

---

## 📌 Project Overview

The goal of this project is to build a binary image classifier that distinguishes between daytime and nighttime images. It includes:

- A CNN model built with TensorFlow/Keras.
- A Streamlit GUI for easy interaction.
- Tools to retrain the model with your own dataset.
- Visualizations like confusion matrix and training curves.

---

## 🚀 Features

- Binary image classification (Day/Night)
- Trained with real-world images
- Simple and intuitive Streamlit interface
- Easily extendable for further experimentation

---

## 🧠 Technologies Used

- Python 3.x  
- TensorFlow & Keras  
- scikit-learn  
- NumPy, Matplotlib  
- Streamlit (for GUI)

---

## 📁 Project Structure

```
Day-or-Night-Classification/
│
├── Dataset/
│   └── day_night_images/
│       ├── training/
│       │   ├── day/
│       │   └── night/
│       └── test/
│           ├── day/
│           └── night/
│
├── Model/
│   └── day_night_model.keras        # Saved trained model
│
├── Code/
│   └── Day&NIght.ipynb              # Notebook with model training and evaluation
│
├── GUI/
│   ├── app.py                       # Streamlit GUI
│   └── model.py                     # Helper functions to load model and predict
├── Presentation/
│   └── Day-or-.....pdf              # Presentation of Project PDF
│
├── requirements.txt                 # Project dependencies
└── README.md                        # Project documentation
```

---

## 📦 Installation

1. **Clone the repository**  
```bash
git clone https://github.com/Zeyad-2004/Day-or-Night-Classification.git
cd Day-or-Night-Classification
```

2. **Install dependencies**  
```bash
pip install -r requirements.txt
```

---

## 🛠️ How to Use

### 📷 1. Use the Streamlit GUI

Run the web app locally:

```bash
cd GUI
streamlit run app.py
```

- A browser window will open where you can upload an image.
- The model will predict whether it’s **Day** or **Night**.

---

## 🏋️‍♂️ Retrain the Model

To retrain the model, open the Jupyter Notebook:

```bash
cd Code
jupyter notebook Day&NIght.ipynb
```

- Make sure your dataset is located in `Dataset/day_night_images/`.
- Modify the training paths inside the notebook if needed.
- The final model will be saved in the `Model/` folder as `day_night_model.keras`.

---

## 📊 Model Summary

Your model is a Convolutional Neural Network with the following architecture:

```python
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)),
    MaxPooling2D(2, 2),

    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),

    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),

    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),

    Flatten(),
    Dense(64, activation='relu'),
    Dropout(0.3),
    Dense(1, activation='sigmoid')  # Output layer for binary classification
])
```

---

## 🧪 Evaluation

- Accuracy: 🔥 **99% 🔥**
- Confusion Matrix and training/validation graphs are displayed in the notebook.

---
## ⚡GUI
 ![Streamlit - Made with Clipchamp](https://github.com/user-attachments/assets/f9488400-35c1-4ad5-9fa6-b01947a745bc)
---

## 🎬 Presentation
- Visit this [Website to see presentation](https://day-or-night-unveiling-t-5b7cn1t.gamma.site/)
- See [PDF File](https://github.com/Zeyad-2004/Day-or-Night-Classification/blob/main/Presentation/Day-or-Night-Unveiling-the-Vision-of-AI.pdf)
---
## 📃 LinkedIn Post
-- [Visit Post at LinkedIn](https://www.linkedin.com/posts/zeyad2004_day-or-night-classification-activity-7353517666780741632-5CXg?utm_source=share&utm_medium=member_desktop&rcm=ACoAAD7KaHkBU_FUML0hnuWGigIQaZobblv5gz8)
---

## 🙋‍♂️ Author

**Zeyad**
[GitHub](https://github.com/Zeyad-2004)
<br>
**Youssef**
[GitHub](https://github.com/Youssef-Mahmoud-Youssef)
