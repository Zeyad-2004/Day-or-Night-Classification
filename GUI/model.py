# model.py

from PIL import Image
import numpy as np
import tensorflow as tf

# Load your Keras model
model = tf.keras.models.load_model("../Model/day_night_model.keras")

def predict_day_night(image: Image.Image) -> str:
    # Resize to match model input: (128, 128, 3)
    img = image.convert("RGB").resize((128, 128))
    img_array = np.array(img) / 255.0  # Normalize to [0, 1]
    img_array = np.expand_dims(img_array, axis=0)  # Shape: (1, 128, 128, 3)

    # Predict
    prediction = model.predict(img_array)[0][0]  # Single sigmoid output
    label = "Day" if prediction < 0.5 else "Night"

    return label
