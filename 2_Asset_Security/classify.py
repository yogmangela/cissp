import joblib
import numpy as np
from tensorflow.keras.preprocessing import image
import tensorflow as tf
from sklearn.feature_extraction.text import TfidfVectorizer

# Load pre-trained models
classifier = joblib.load('models/text_classifier.pkl')
vectorizer = joblib.load('models/tfidf_vectorizer.pkl')
model = tf.keras.applications.ResNet50(weights='imagenet')

# Text classification function
def classify_text(text):
    text_tfidf = vectorizer.transform([text])
    prediction = classifier.predict(text_tfidf)
    return prediction[0]

# Image classification function
def classify_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))  # Resize image to fit model
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = tf.keras.applications.resnet50.preprocess_input(img_array)

    preds = model.predict(img_array)
    decoded_preds = tf.keras.applications.resnet50.decode_predictions(preds, top=1)[0]
    return decoded_preds[0][1]  # Predicted label