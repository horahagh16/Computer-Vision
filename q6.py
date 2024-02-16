'''import cv2
import face_recognition
def find_face_encodings(image_path):
    # reading image
    image = cv2.imread(image_path)    # get face encodings from the image
    face_enc = face_recognition.face_encodings(image)    # return face encodings
    return face_enc[0]

# getting face encodings for first image
image_1 = find_face_encodings("face1.jpg")# getting face encodings for second image
image_2  = find_face_encodings("face2.jpg")

# checking both images are same
is_same = face_recognition.compare_faces([image_1], image_2)[0]
print(f"Is Same: {is_same}")

if is_same:
    # finding the distance level between images
    distance = face_recognition.face_distance([image_1], image_2)
    distance = round(distance[0] * 100)
    
    # calcuating accuracy level between images
    accuracy = 100 - round(distance)    
    print("The images are same")
    print(f"Accuracy Level: {accuracy}%")
else:
    print("The images are not same")'''
from deepface import DeepFace

f1 = "face1.jpg"
f2 = "face2.jpg"
backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface', 'mediapipe']
result = DeepFace.verify(img1_path=f1, img2_path=f2, detector_backend=backends[1])