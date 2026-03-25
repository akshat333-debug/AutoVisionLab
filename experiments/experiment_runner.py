import subprocess

models = ["vgg16", "resnet50", "efficientnet"]

for model in models:

    print("Running experiment:", model)

    subprocess.run([
        "python",
        "training/train.py",
        "--model",
        model
    ])