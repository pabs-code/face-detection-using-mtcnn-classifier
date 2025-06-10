import os
import cv2
import numpy as np
from mtcnn import MTCNN
import streamlit as st


class FaceDetectionApp:
    """
    A class that encapsulates the functionality of a face detection application using Streamlit.

    Attributes:
        detector (MTCNN): The MTCNN object used for detecting faces in images.

    Methods:
        __init__: Initializes the MTCNN detector.
        detect_faces: Detects and draws rectangles around faces in an image or list of images.
        load_images: Loads multiple images from files uploaded by the user via Streamlit.
        display_image: Displays an image with detected faces on the web page.
        run: Main method to control the flow of the application.
    """

    def __init__(self):
        """Initialize the MTCNN face detector."""
        self.detector = MTCNN()

    def detect_faces(self, images):
        """
        Detects and draws rectangles around faces in an image or list of images.

        Args:
            images (list): List of input images to process.

        Returns:
            list: List of images with detected faces.
        """
        if isinstance(images, np.ndarray):
            # Single image processing
            return [self.detect_faces_single_image(image) for image in images]

        elif isinstance(images, list):
            # Multiple images processing
            return [self.detect_faces_single_image(image.copy()) for image in images]

    def detect_faces_single_image(self, image):
        """
        Detects and draws rectangles around faces in a single image.

        Args:
            image (numpy.ndarray): The input image to process.

        Returns:
            numpy.ndarray: The image with detected faces.
        """
        # Detect faces using MTCNN
        faces = self.detector.detect_faces(image)

        if not faces:
            return image  # No faces detected

        # Draw rectangles around the detected faces
        for face in faces:
            box = face['box']
            x, y, width, height = box[0], box[1], box[2], box[3]
            x2, y2 = x + width, y + height  # Calculate the bottom-right corner
            cv2.rectangle(image, (x, y), (x2, y2), (0, 255, 0), 2)

        return image

    def load_images(self):
        """
        Loads multiple images from files uploaded by the user via Streamlit.

        Returns:
            list or None: List of loaded images as NumPy arrays if successful; otherwise, `None`.
        """
        # Load the uploaded images from Streamlit
        uploaded_files = st.file_uploader(
            "Upload Images",
            type=["jpg", "jpeg", "png"],
            accept_multiple_files=True,
            key="face-detection-uploader"
        )

        if uploaded_files is not None:
            try:
                img_arrays = []
                for file in uploaded_files:
                    img_bytes = file.read()
                    img_array = np.frombuffer(img_bytes, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

                    if img is not None:
                        img_arrays.append(img)
                    else:
                        st.error(f"Failed to decode the image: {file.name}")
                return img_arrays
            except Exception as e:
                st.error(f"An error occurred: {e}")

        return None

    def display_image(self, images):
        """
        Displays multiple images with detected faces on the web page.

        Args:
            images (list): List of input images.
        """
        for i, image in enumerate(images):
            # Convert BGR to RGB for Streamlit compatibility
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            st.image(rgb_image, channels="RGB",
                     caption=f"Detected Faces - Image {i+1}", use_container_width=True)

    def run(self):
        """Main method to control the flow of the application."""

        st.title("Face Detection - MTCNN Classifier")

        # User instructions
        st.markdown(
            """
            # 📸 Upload an Image for Face Detection

            1. Click the **"Browse files"** button.
            2. Choose a photo or photos in `.jpg`, `.jpeg`, or `.png` format.
            3. The app will detect faces from the photo and display the result in a rectangle.

            You can also drag and drop more than one image at a time into this area.
            """
        )

        images = self.load_images()

        if images is not None:
            detected_images = self.detect_faces(images)
            self.display_image(detected_images)
        else:
            st.write("Upload one or more images to see face detection in action!")


# Run the app
if __name__ == "__main__":
    app = FaceDetectionApp()
    app.run()
