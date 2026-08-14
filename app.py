import cv2
import pyttsx3
import time
from ultralytics import YOLO

# Text-to-speech engine initialize karein
engine = pyttsx3.init()
engine.setProperty('rate', 160) 

def speak_async(text):
    print(f"AI Output: {text}")
    engine.say(text)
    engine.runAndWait()

def main():
    print("Loading AI Model (YOLOv8)...")
    model = YOLO('yolov8n.pt')
    
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Accessibility Assistant started. Press 'q' to exit.")
    
    last_spoken_time = 0
    cooldown_seconds = 5  
    
    while True:
        success, frame = cap.read()
        if not success:
            print("Camera error!")
            break
            
        results = model(frame, verbose=False)
        
        current_detected_objects = []
        
        for r in results:
            boxes = r.boxes
            for box in boxes:
                # Bounding box coordinates
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                conf = float(box.conf[0])
                cls = int(box.cls[0])
                class_name = model.names[cls]
                
                # Confidence threshold (> 50%)
                if conf > 0.5:
                    current_detected_objects.append(class_name)
                    
                    # Screen par box draw karein (Green color)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, f"{class_name} {conf:.2f}", (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Audio guidance (Cooldown check ke sath)
        if current_detected_objects:
            current_time = time.time()
            if current_time - last_spoken_time > cooldown_seconds:
                # Unique objects select karein taaki duplicate na bolein
                unique_objs = list(set(current_detected_objects))
                objects_str = ", ".join(unique_objs)
                speak_async(f"I see {objects_str}")
                last_spoken_time = current_time

        # Live feed display karein
        cv2.imshow("AI-Powered Accessibility Assistant", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
