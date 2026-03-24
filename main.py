import cv2
import os
import numpy as np
from datetime import datetime

# Path to dataset
data_path = 'images'

faces = []
labels = []
names = {}
label_id = 0

# Load dataset
for person_name in os.listdir(data_path):
    person_folder = os.path.join(data_path, person_name)

    if os.path.isdir(person_folder):
        names[label_id] = person_name

        for image_name in os.listdir(person_folder):
            image_path = os.path.join(person_folder, image_name)
            img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (200, 200))

            faces.append(img)
            labels.append(label_id)

        label_id += 1

# Convert to numpy array

labels = np.array(labels)

# Train LBPH recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(faces, labels)

print("Training Complete ✅")

# Start webcam
marked_attendance = set()

def mark_attendance(name):
    if name not in marked_attendance:
        now = datetime.now()
        date_string = now.strftime("%d-%m-%Y")
        time_string = now.strftime("%H:%M:%S")

        with open("attendance.csv", "a") as f:
            f.write(f"{name},{date_string},{time_string}\n")

        marked_attendance.add(name)
        print(f"Attendance marked for {name}")
cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    detected_faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(detected_faces) > 0:
    
        x, y, w, h = max(detected_faces, key=lambda rect: rect[2]*rect[3])
        face = gray[y:y+h, x:x+w]
        face = cv2.resize(face, (200, 200))

        label, confidence = recognizer.predict(face)

        if confidence < 80:
          name = names[label]
          mark_attendance(name)

          now = datetime.now()
          date_string = now.strftime("%d-%m-%Y")
          time_string = now.strftime("%H:%M:%S")

        else:
           name = "Unknown"
           date_string = ""
           time_string = ""
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        cv2.putText(frame, name, (x,y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9, (0,255,0), 2)

        cv2.putText(frame, date_string, (x,y+h+20),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6, (255,255,0), 2)

        cv2.putText(frame, time_string, (x,y+h+45),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6, (255,255,0), 2) 
    cv2.imshow("Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == 27:   
        break

cap.release()
cv2.destroyAllWindows()