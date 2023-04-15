from sklearn.linear_model import LogisticRegression
import torch 
import torchvision


import torch
import torchvision

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"DEVICE: {torch.cuda.get_device_name()}")
print(f"GPU AVAILABLE : {torch.cuda.is_available()}")
print(f"RUNNING ON : {device}")


