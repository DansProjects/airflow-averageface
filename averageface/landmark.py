import numpy as np
import cv2
import dlib

image_path = "images/barak-obama.jpg"
cascade_path = "frontalface_default.xml"
predictor_path = "shape_predictor_68_face_landmarks.dat"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascade_path)

# create the landmark predictor
predictor = dlib.shape_predictor(predictor_path)

# Read the image
image = cv2.imread(image_path)

# convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.05,
    minNeighbors=5,
    minSize=(100, 100),
    flags=cv2.CASCADE_SCALE_IMAGE
)

print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Converting the OpenCV rectangle coordinates to Dlib rectangle
    dlib_rect = dlib.rectangle(int(x), int(y), int(x + w), int(y + h))
    print(dlib_rect)

    detected_landmarks = predictor(image, dlib_rect).parts()

    landmarks = np.matrix([[p.x, p.y] for p in detected_landmarks])

    # copying the image so we can see side-by-side
    image_copy = image.copy()

    for idx, point in enumerate(landmarks):
        pos = (point[0, 0], point[0, 1])

        # annotate the positions
        cv2.putText(image_copy, str(idx), pos,
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.4,
                    color=(0, 0, 255))

        # draw points on the landmark positions
        cv2.circle(image_copy, pos, 3, color=(0, 255, 255))

cv2.imshow("Landmarks found", image_copy)
cv2.waitKey(0)
