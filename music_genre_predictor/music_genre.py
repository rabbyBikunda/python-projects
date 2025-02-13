import librosa
import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

DATASET_PATH = "genres"

def extract_features(file_path):
    """Extracts features like MFCCs, chroma, and spectral contrast from an audio file."""
    try:
        # Load the audio file
        y, sr = librosa.load(file_path, duration=30, sr=22050)

        # Extract features
        mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13), axis=1)
        chroma = np.mean(librosa.feature.chroma_stft(y=y, sr=sr), axis=1)
        spectral_contrast = np.mean(librosa.feature.spectral_contrast(y=y, sr=sr), axis=1)
        zero_crossing_rate = np.mean(librosa.feature.zero_crossing_rate(y=y))
        
        # Combine all features into a single vector
        features = np.hstack([mfcc, chroma, spectral_contrast, zero_crossing_rate])
        return features
    except Exception as e:
        print(f"Error extracting features from {file_path}: {e}")
        return None

# Function to load dataset and extract features
def load_data(dataset_path):
    """Loads the dataset and extracts features from all audio files."""
    features = []
    labels = []
    for genre in os.listdir(dataset_path):
        genre_folder = os.path.join(dataset_path, genre)
        if os.path.isdir(genre_folder):
            for song_file in os.listdir(genre_folder):
                song_path = os.path.join(genre_folder, song_file)
                feature_vector = extract_features(song_path)
                if feature_vector is not None:
                    features.append(feature_vector)
                    labels.append(genre)
    
    return np.array(features), np.array(labels)

def train_model(features, labels):
    """Trains a machine learning model to predict song genres."""
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")
    
    return model

def predict_genre(model, song_path):
    """Predicts the genre of a new song."""
    features = extract_features(song_path)
    if features is not None:
        prediction = model.predict([features])
        print(f"The predicted genre for the song is: {prediction[0]}")
    else:
        print("Error in feature extraction. Unable to predict genre.")

def main():
    print("Loading dataset...")
    features, labels = load_data(DATASET_PATH)

    print("Training model...")
    model = train_model(features, labels)

    print("Testing model on a new song...")
    predict_genre(model, new_song_path)

if __name__ == "__main__":
    main()