# Face Recognition Attendance System

## 📌 Problem Statement

In schools and colleges, attendance is usually taken manually, which is time-consuming and can lead to errors or proxy attendance.

## 💡 Solution

This project uses face recognition technology to automatically mark attendance. It captures faces through a camera, recognizes the person, and records attendance without manual effort.

## 🎯 Objective

* To automate attendance system
* To reduce time and manual work
* To avoid proxy attendance

## 🛠️ Technologies Used

* Python
* OpenCV
* Face Recognition Library
* NumPy
* CSV / Excel (for storing attendance)

## ⚙️ How It Works

1. The system captures images through a webcam
2. It detects faces in the frame
3. It compares detected faces with stored images
4. If a match is found, attendance is marked
5. Attendance is saved with date and time

## ▶️ How to Run the Project

1. Install required libraries:
   pip install opencv-python face-recognition numpy

2. Run the main file:
   python main.py

3. Make sure:

   * Camera is connected
   * Student images are stored in the dataset folder

## 📁 Project Structure

* dataset/ → contains student images
* attendance.csv → stores attendance records
* main.py → main program file

## 👤 Developer

* E.Jessysusan

## ✅ Advantages

* Saves time
* Accurate attendance
* No proxy attendance
* Easy to use

## 🚀 Future Scope

* Can be integrated with mobile apps
* Can be used in offices and organizations
* Can store data in cloud
