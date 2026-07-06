import os
import random
import shutil

random.seed(42)

project = r"D:\Formwork_Detection_Project"

source_images = os.path.join(project, "datasets", "auto_labels_v2")
source_labels = os.path.join(source_images, "labels")

dest_images = os.path.join(project, "datasets", "images")
dest_labels = os.path.join(project, "datasets", "labels")

# ----------------------------------------------------

images = []

for f in os.listdir(source_images):
    if f.lower().endswith((".jpg", ".jpeg", ".png")):
        label = os.path.join(source_labels, os.path.splitext(f)[0] + ".txt")
        if os.path.exists(label):
            images.append(f)

print(f"Found {len(images)} image-label pairs.")

random.shuffle(images)

n = len(images)

train = images[:int(0.8*n)]
val = images[int(0.8*n):int(0.9*n)]
test = images[int(0.9*n):]

print()
print("Train:", len(train))
print("Val  :", len(val))
print("Test :", len(test))
print()

def copy_set(file_list, split):

    img_dst = os.path.join(dest_images, split)
    lbl_dst = os.path.join(dest_labels, split)

    os.makedirs(img_dst, exist_ok=True)
    os.makedirs(lbl_dst, exist_ok=True)

    for img in file_list:

        shutil.copy2(
            os.path.join(source_images, img),
            os.path.join(img_dst, img)
        )

        txt = os.path.splitext(img)[0] + ".txt"

        shutil.copy2(
            os.path.join(source_labels, txt),
            os.path.join(lbl_dst, txt)
        )

copy_set(train, "train")
copy_set(val, "val")
copy_set(test, "test")

print("--------------------------------")
print("Dataset merged successfully!")
print("--------------------------------")