import os

img_dir = r"D:\Formwork_Detection_Project\datasets\auto_labels_v2"
lbl_dir = os.path.join(img_dir, "labels")

images = {
    os.path.splitext(f)[0]
    for f in os.listdir(img_dir)
    if f.lower().endswith((".jpg", ".jpeg", ".png"))
}

labels = {
    os.path.splitext(f)[0]
    for f in os.listdir(lbl_dir)
    if f.lower().endswith(".txt") and f.lower() != "classes.txt"
}

missing = sorted(images - labels)

print(f"Images : {len(images)}")
print(f"Labels : {len(labels)}")
print(f"Missing: {len(missing)}")
print()

print("First 30 missing files:")
for name in missing[:30]:
    print(name)