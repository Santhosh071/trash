from ultralytics import YOLO

model=YOLO('models/best5.pt')
results= model.predict('input_videos/input_video_4.mp4',save=True)
print(results[0])
print("===============================")
for box in results[0].boxes:
    print(box)
