import cv2

# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize video capture from the default webcam
cap = cv2.VideoCapture(0)

# Define the codec and create a VideoWriter object to save the output video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# Initialize the tracker to None
tracker = None
tracking = False

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        break

    if not tracking:
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        if len(faces) > 0:
            # Use the first detected face
            (x, y, w, h) = faces[0]

            # Initialize the tracker with the face bounding box
            tracker = cv2.TrackerKCF_create()
            bbox = (x, y, w, h)
            tracker.init(frame, bbox)
            tracking = True

    else:
        # Update the tracker
        ret, bbox = tracker.update(frame)

        if ret:
            (x, y, w, h) = [int(v) for v in bbox]
            center_x, center_y = x + w // 2, y + h // 5  # Place the dot at the forehead
            cv2.circle(frame, (center_x, center_y), 5, (0, 255, 0), -1)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        else:
            tracking = False

    # Write the frame into the file 'output.avi'
    out.write(frame)

    # Display the resulting frame
    cv2.imshow('Headshot Tracking', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and writer objects, and close all OpenCV windows
cap.release()
out.release()
cv2.destroyAllWindows()
