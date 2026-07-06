from ultralytics import YOLO

model = YOLO(r"D:\Formwork_Detection_Project\models\best.pt")

results = model.predict(
    source=r"D:\Formwork_Detection_Project\unlabeled_images",
    conf=0.10,
    save=False,
    save_txt=False,
    verbose=False
)

detected = 0
undetected = 0

for r in results:
    if len(r.boxes) > 0:
        detected += 1
    else:
        undetected += 1

print(f"Detected Images   : {detected}")
print(f"Undetected Images : {undetected}")