import os
import cv2

def analyze_dataset(dataset_path):
    classes = os.listdir(dataset_path)

    stats = {}

    for c in classes:
        folder = os.path.join(dataset_path, c)
        images = os.listdir(folder)

        stats[c] = len(images)

    return stats


if __name__ == "__main__":
    stats = analyze_dataset("datasets/raw")
    print(stats)