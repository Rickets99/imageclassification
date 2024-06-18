<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Food Classification App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: #fff;
        }
        h1, h2, h3 {
            color: #333;
        }
        pre {
            background: #f4f4f4;
            padding: 10px;
            border: 1px solid #ddd;
            overflow-x: auto;
        }
        code {
            background: #f4f4f4;
            padding: 2px 4px;
            border-radius: 3px;
        }
        .file-structure {
            font-family: monospace;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Food Classification App</h1>
        <p>This project is a Gradio-based web application that allows users to classify images using pre-trained models from Hugging Face. It includes models for classifying food images and detecting facial emotions.</p>

        <h2>Features</h2>
        <ul>
            <li>Upload an image and get the predicted class using various pre-trained models.</li>
            <li>Models included:
                <ul>
                    <li>Food Model</li>
                    <li>Another Model</li>
                    <li>Facial Emotions Image Detection</li>
                </ul>
            </li>
        </ul>

        <h2>Setup</h2>
        <h3>Prerequisites</h3>
        <ul>
            <li>Python 3.6 or higher</li>
            <li>pip (Python package installer)</li>
        </ul>

        <h3>Installation</h3>
        <ol>
            <li>Clone the repository:
                <pre><code>git clone https://github.com/YOUR_GITHUB_USERNAME/food-classification-app.git
cd food-classification-app</code></pre>
            </li>
            <li>Create and activate a virtual environment (optional but recommended):
                <pre><code>python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`</code></pre>
            </li>
            <li>Install the required packages:
                <pre><code>pip install -r requirements.txt</code></pre>
            </li>
            <li>Download the models:
                <pre><code>from transformers import AutoModelForImageClassification, AutoFeatureExtractor

# Food Model
model_name = "nateraw/food"
model = AutoModelForImageClassification.from_pretrained(model_name)
feature_extractor = AutoFeatureExtractor.from_pretrained(model_name)
model.save_pretrained("./models/food_model")
feature_extractor.save_pretrained("./models/food_model")

# Another Model (replace 'another_model_name' with the actual model name)
another_model_name = "another_model_name"
another_model = AutoModelForImageClassification.from_pretrained(another_model_name)
another_feature_extractor = AutoFeatureExtractor.from_pretrained(another_model_name)
another_model.save_pretrained("./models/another_model")
another_feature_extractor.save_pretrained("./models/another_model")

# Facial Emotions Image Detection Model
facial_model_name = "dima806/facial_emotions_image_detection"
facial_model = AutoModelForImageClassification.from_pretrained(facial_model_name)
facial_feature_extractor = AutoFeatureExtractor.from_pretrained(facial_model_name)
facial_model.save_pretrained("./models/facial_emotions_image_detection")
facial_feature_extractor.save_pretrained("./models/facial_emotions_image_detection")</code></pre>
            </li>
        </ol>

        <h2>Running the App</h2>
        <ol>
            <li>Run the application:
                <pre><code>python app.py</code></pre>
            </li>
            <li>Open your browser and go to <code>http://127.0.0.1:7860</code> to see the Gradio interface.</li>
        </ol>

        <h2>Usage</h2>
        <ol>
            <li>Upload an image.</li>
            <li>Select the desired model from the dropdown.</li>
            <li>Click "Submit" to get the predicted class for the image.</li>
        </ol>

        <h2>File Structure</h2>
        <pre class="file-structure"><code>food-classification-app/
├── app.py
├── requirements.txt
├── models/
│   ├── food_model/
│   │   ├── config.json
│   │   ├── pytorch_model.bin
│   │   ├── preprocessor_config.json
│   ├── another_model/
│   │   ├── config.json
│   │   ├── pytorch_model.bin
│   │   ├── preprocessor_config.json
│   ├── facial_emotions_image_detection/
│       ├── config.json
│       ├── pytorch_model.bin
│       ├── preprocessor_config.json
└── README.html</code></pre>

        <h2>Contributing</h2>
        <p>Contributions are welcome! Please open an issue or submit a pull request for any changes.</p>

        <h2>License</h2>
        <p>This project is licensed under the MIT License.</p>
    </div>
</body>
</html>
