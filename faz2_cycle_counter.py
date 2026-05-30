from ultralytics import YOLO
import cv2
import pandas as pd

MODEL_PATH = "runs/detect/train/weights/best.pt"
VIDEO_PATH = "faz2_gozlemsiz.mp4"

CONF_THRES = 0.15
DEVICE = 0

MIN_CYCLE_SEC = 8.0
MIN_EMPTY_FRAMES = 12
MIN_DETECT_FRAMES = 2

model = YOLO(MODEL_PATH)

cap = cv2.VideoCapture(VIDEO_PATH)
fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
min_cycle_frames = int(MIN_CYCLE_SEC * fps)

ret, first_frame = cap.read()
if not ret:
    raise Exception("Video okunamadı.")

roi = cv2.selectROI("ROI sec - Faz 2 cikis bolgesi", first_frame, False)
cv2.destroyAllWindows()

rx1, ry1, rw, rh = roi
rx2, ry2 = rx1 + rw, ry1 + rh

cycle_frames = []
roi_occupied = False
empty_count = 0
detect_count = 0

cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
frame_no = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, conf=CONF_THRES, verbose=False, device=DEVICE)[0]

    detected_in_roi = False

    for box in results.boxes:
        cls_id = int(box.cls[0])
        cls_name = model.names[cls_id]

        if cls_name != "finished_package":
            continue

        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cx = int((x1 + x2) / 2)
        cy = int((y1 + y2) / 2)

        if rx1 <= cx <= rx2 and ry1 <= cy <= ry2:
            detected_in_roi = True
            break

    if detected_in_roi:
        detect_count += 1
        empty_count = 0

        if not roi_occupied and detect_count >= MIN_DETECT_FRAMES:
            if len(cycle_frames) == 0 or (frame_no - cycle_frames[-1]) >= min_cycle_frames:
                cycle_frames.append(frame_no)
                roi_occupied = True
                print(f"Cycle {len(cycle_frames)} detected at frame {frame_no}")

    else:
        detect_count = 0
        empty_count += 1

        if empty_count >= MIN_EMPTY_FRAMES:
            roi_occupied = False

    frame_no += 1

cap.release()

rows = []
for i, f in enumerate(cycle_frames):
    time_sec = f / fps
    cycle_time = None if i == 0 else (cycle_frames[i] - cycle_frames[i - 1]) / fps

    rows.append({
        "cycle_no": i + 1,
        "frame": f,
        "time_sec": round(time_sec, 3),
        "cycle_time_sec": None if cycle_time is None else round(cycle_time, 3)
    })

df = pd.DataFrame(rows)
df.to_csv("faz2_cycle_results_clean.csv", index=False, encoding="utf-8-sig")

print("\nBitti.")
print(f"FPS: {fps}")
print(f"Toplam frame: {total_frames}")
print(f"Minimum cycle araligi: {MIN_CYCLE_SEC} sn")
print(f"Bulunan cycle sayisi: {len(cycle_frames)}")
print("CSV kaydedildi: faz2_cycle_results_clean.csv")