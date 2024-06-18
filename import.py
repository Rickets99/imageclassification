import os

model_dirs = ["./models/food_model", "./models/another_model"]

for model_dir in model_dirs:
    for file_name in os.listdir(model_dir):
        if file_name not in ["config.json", "pytorch_model.bin", "preprocessor_config.json"]:
            os.remove(os.path.join(model_dir, file_name))
