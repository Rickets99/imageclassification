import gradio as gr
from transformers import AutoModelForImageClassification, AutoFeatureExtractor
from PIL import Image
import torch
import json
import os

# Define available models
MODELS = {
    "Food Model": "food_model",
    "Another Model": "another_model",
    "Face Model": "face_model"
}

def load_model_and_feature_extractor(model_key):
    model_path = os.path.join("./models", MODELS[model_key])
    config_path = os.path.join(model_path, "config.json")
    
    # Load model and feature extractor
    model = AutoModelForImageClassification.from_pretrained(model_path, local_files_only=True)
    feature_extractor = AutoFeatureExtractor.from_pretrained(model_path, local_files_only=True)
    
    # Load class labels from config.json
    with open(config_path, "r") as f:
        config = json.load(f)
        labels = config.get("id2label", {})
    
    return model, feature_extractor, labels

# Initialize the first model by default
current_model_name = "Food Model"
model, feature_extractor, labels = load_model_and_feature_extractor(current_model_name)

# Define the prediction function
def predict(image, model_name):
    global model, feature_extractor, labels, current_model_name
    if model_name not in MODELS:
        return "Invalid model selection"
    
    # Load the selected model if it's not already loaded
    if model_name != current_model_name:
        model, feature_extractor, labels = load_model_and_feature_extractor(model_name)
        current_model_name = model_name
    
    inputs = feature_extractor(images=image, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    predicted_class_idx = logits.argmax(-1).item()
    predicted_class_label = labels.get(str(predicted_class_idx), "Unknown label")
    return predicted_class_label

# Create the Gradio interface
interface = gr.Interface(
    fn=predict,
    inputs=[
        gr.components.Image(type="pil", label="Upload Image"),
        gr.components.Dropdown(choices=list(MODELS.keys()), value="Food Model", label="Model")
    ],
    outputs="text",
    title="Image Classification",
    description="Upload an image and select a model to get the predicted class."
)

# Launch the app
if __name__ == "__main__":
    interface.launch()
