# Headshot Tracking

This project demonstrates a simple headshot tracking system using OpenCV. The system captures video from the webcam, detects faces using a Haar Cascade classifier, and tracks the detected face using the KCF tracker. A green dot is placed on the forehead of the tracked face.

## Features

- Real-time face detection using Haar Cascade classifier.
- Face tracking using KCF (Kernelized Correlation Filters) tracker.
- Displays a green dot on the forehead of the tracked face.
- Saves the output video to a file.

## Requirements

- Python 3.x
- OpenCV

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/vedikasharma2801/headshot-tracking.git
    cd headshot-tracking
    ```

2. Install the required dependencies:

    ```bash
    pip install opencv-python
    ```

## Usage

1. Run the script:

    ```bash
    python headshot_tracking.py
    ```

2. The script will start capturing video from the default webcam. It will detect faces, track the first detected face, and display a green dot on the forehead of the tracked face.

3. Press the 'q' key to stop the script and close all windows.
