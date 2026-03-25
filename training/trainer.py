import torch
from torchvision import models

class Trainer:

    def __init__(self, config):
        self.config = config

    def load_model(self, name):

        if name == "vgg16":
            return models.vgg16(pretrained=True)

        if name == "resnet50":
            return models.resnet50(pretrained=True)

    def run(self):

        for model_name in self.config["models"]:

            model = self.load_model(model_name)

            print("Training:", model_name)

            # training logic here