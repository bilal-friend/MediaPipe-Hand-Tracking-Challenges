import cv2
import mediapipe as mp

from mediapipe.tasks import python
from mediapipe.tasks.python import vision


# 1. Create the model
base_options = python.BaseOptions(
    model_asset_path="hand_landmarker.task"
)

options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1
)

detector = vision.HandLandmarker.create_from_options(options)


# 2. Open webcam
cap = cv2.VideoCapture(0)


while True:

    success, frame = cap.read()

    if not success:
        break

    # 3. BGR → RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # 4. NumPy → MediaPipe Image
    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb_frame
    )

    # 5. Detect hands
    result = detector.detect(mp_image)

    if result.hand_landmarks:  
      landmark = result.hand_landmarks[0][8]
      ## folow my finger 
      x = int(landmark.x * frame.shape[1])  
      y = int(landmark.y * frame.shape[0])
      cv2.circle(
              frame,
              (x, y),
              50,
              (255, 0, 0),
              -1
      )

          
    # 6. Display webcam
    cv2.imshow("webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# 7. Release resources
cap.release()
detector.close()
cv2.destroyAllWindows()