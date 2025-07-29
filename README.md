# YOLOv8 Drone Detection 🛰️

A real-time drone detection system built using **YOLOv8** and deployed with **Streamlit**.

## 🔍 Overview
This project uses a custom-trained YOLOv8 object detection model to identify drones in real-time. It can be used in surveillance, no-fly zones, and other security-critical environments.

## 📁 Dataset
- Custom drone dataset
- Labeled using YOLO format (`.txt` files)
- Split into `train/` and `valid/` folders with respective `images/` and `labels/`

## 🧠 Model
- YOLOv8n (Ultralytics)
- Trained using Ultralytics library
- `.pt` model stored and used for inference

## 🛠 Tech Stack
- Python
- YOLOv8 (Ultralytics)
- Streamlit (for web app UI)
- Pillow (image support)

## 🚀 Deployment
Run the Streamlit app locally:
```bash
pip install -r requirements.txt
streamlit run app.py
