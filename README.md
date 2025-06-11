# Face Detection App using MTCNN Classifer

A simple Streamlit-based application for detecting faces in images using the **MTCNN (Multi-task Cascaded Convolutional Neural Network)** algorithm.

## Table of Contents

  - [About the Project](#about-the-project)
    - [What is the MTCNN Classifier?](#what-is-the-mtcnn-classifier)
    - [How It Works:](#how-it-works)
  - [Features](#features)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Folder Structure](#folder-structure)
  - [Installation](#installation)
  - [Running Script](#running-script)
  - [Expectations When Running This App](#expectations-when-running-this-app)
  - [Demo](#demo)
  - [Acknowledgments](#acknowledgments)
  - [License](#license)
  - [Notes](#notes)

---

## About the Project

### What is the MTCNN Classifier?

**MTCNN (Multi-task Cascaded Convolutional Neural Network)** is a deep learning algorithm designed for **face detection and alignment**. It's widely used in computer vision applications such as face recognition, emotion analysis, and more.

### How It Works:

MTCNN uses a **cascade of three stages**:
1. **Proposal Network (PNet)**: Detects potential face regions.
2. **Refining Network (RPN)**: Refines the initial detection by improving accuracy and reducing false positives.
3. **Output Network (ONet)**: Finalizes face detection with precise bounding boxes and facial landmarks.

This project uses the MTCNN model to detect faces in uploaded images using **Streamlit**, a popular Python framework for building web apps.

---

## Features

- Detects faces in images using MTCNN.
- Supports multiple image uploads (JPG, JPEG, PNG).
- Displays the results directly in a web interface.
- Simple and user-friendly UI using Streamlit.

---

## Getting Started

### Prerequisites

Before you start, ensure you have the following installed:

| Dependency | Version | Description                                |
| ---------- | ------- | ------------------------------------------ |
| Python     | 3.8+    | Required for running the app               |
| Streamlit  | ≥1.20   | For building the web interface             |
| MTCNN      | 0.1.8+  | Face detection model (via `mtcnn` package) |
| OpenCV     | ≥4.5    | For image processing and display           |

You can install the required packages using:

```bash
pip install streamlit mtcnn opencv-python-headless
```

### Folder Structure

The project has the following structure:

```
face-detection-using-mtcnn-classifier/
├── README.md
├── app.py
```

> ✅ `app.py` contains the main application logic.  

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/face-detection-using-mtcnn-classifier.git
cd face-detection-using-mtcnn-classifier
```

2. Install the dependencies:

```bash
pip install streamlit mtcnn opencv-python-headless
```

---

## Running Script

To run the application, use:

```bash
streamlit run app.py
```

This will start a local development server, and you can view the web interface in your browser at `http://localhost:8501`.

---

## Expectations When Running This App

- You can upload **one or more images** in `.jpg`, `.jpeg`, or `.png` format.
- The app will detect faces and draw **green rectangles** around them.
- If an image fails to load or decode, the app will show an error message.

> ✅ The output images are displayed in RGB format for compatibility with Streamlit.

---

## Demo

You can test the app by following these steps:

1. Run `streamlit run app.py`.
2. Go to the web interface.
3. Click **"Upload Images"** and select a few images.
4. Watch as the app detects faces in real-time!


https://github.com/user-attachments/assets/f68a26a7-b080-45ee-93d0-3ca78c97c64a



---

## Acknowledgments

- [MTCNN GitHub](https://github.com/ip3520/mtcnn) – Original MTCNN implementation.
- [Streamlit Documentation](https://docs.streamlit.io/) – Streamlit framework used for the web interface.
- OpenCV library for image processing and visualization.

---

## License

This project is licensed under the **MIT License**. You can find a copy of the license in the [LICENSE](LICENSE) file.

---

## Notes

- This project is for **educational and demonstration purposes**.
- MTCNN may not perform optimally on images with very low resolution or extreme lighting conditions.

---
