import numpy as np
import cv2
import dlib
import os


class LandmarkClassifier:

    cascade_path = "frontalface_default.xml"
    predictor_path = "shape_predictor_68_face_landmarks.dat"

    def __init__(self, image_dir):
        # Create the haar cascade
        self.faceCascade = cv2.CascadeClassifier(self.cascade_path)
        # create the landmark predictor
        self.predictor = dlib.shape_predictor(self.predictor_path)
        # set image directory
        self.image_dir = image_dir

    def face_detection(self, img):
        # convert the image to gray-scale
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = self.faceCascade.detectMultiScale(
            img_gray,
            scaleFactor=1.05,
            minNeighbors=5,
            minSize=(100, 100),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        return faces

    def classify(self):
        folder = self.image_dir
        images = []
        for filename in os.listdir(folder):
            if filename.endswith('.jpg'):
                print('Processing {}.'.format(filename))
                img_path = os.path.join(folder, filename)
                img = cv2.imread(img_path)
                landmarks = self.get_landmarks(img)
                if landmarks is not None:
                    self.write_to_file(landmarks, img_path)
                else:
                    print('{} has no faces'.format(filename))

        return images

    def get_landmarks(self, image):

        faces = self.face_detection(image)

        for (x, y, w, h) in faces:

            # Converting the OpenCV rectangle coordinates to Dlib rectangle
            dlib_rect = dlib.rectangle(int(x), int(y), int(x + w), int(y + h))
            detected_landmarks = self.predictor(image, dlib_rect).parts()
            landmarks = np.matrix([[p.x, p.y] for p in detected_landmarks])

            # should only have one face per image
            return landmarks

    def write_to_file(self, landmarks, img_path):

        # add txt to end of file to denote landmark representation of image
        file = open(img_path + '.txt', "w")

        for idx, point in enumerate(landmarks):

            file.write(str(point[0, 0]))
            file.write(" ")
            file.write(str(point[0, 1]))
            file.write("\n")

        file.close()

        return True

#image_path = "../cspeople/scraped/full"
#LC = LandmarkClassifier(image_path)
#(LC.classify())
