import os
import shutil

# Paths to the model directories
model_dirs = ["./models/food_model", "./models/food_model_bin", "./models/another_model"]

# Rename the model files to the expected names
for model_dir in model_dirs:
    for file_name in os.listdir(model_dir):
        if "safetensors" in file_name:
            shutil.move(os.path.join(model_dir, file_name), os.path.join(model_dir, "pytorch_model.safetensors"))
        elif "bin" in file_name:
            shutil.move(os.path.join(model_dir, file_name), os.path.join(model_dir, "pytorch_model.bin"))
