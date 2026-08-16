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
      hand =  result.hand_landmarks[0]
      mcp = hand[5]
      tip = hand[8]
      
      x5 = int(tip.x * frame.shape[1])
      y5 = int(tip.y * frame.shape[0])
      x8 = int(mcp.x * frame.shape[1])
      y8 = int(mcp.y * frame.shape[0])

      # circle on 
      cv2.circle(frame,(x5,y5), 10, (0, 255, 0), -1)

      ## detect if horizontal or vertical
      dx = abs(x5 - x8)
      dy = abs(y5 - y8)
      if (dx > dy):
          cv2.putText(frame, "Horizontal", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2
          )
          cv2.putText(frame, "Left" if x5 < x8 else "Right", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
      else:
          cv2.putText(frame, "Vertical", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2
          )
          cv2.putText(frame, "Up" if y5 < y8 else "Down", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # 6. Display webcam
    cv2.imshow("webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# 7. Release resources
cap.release()
detector.close()
cv2.destroyAllWindows()