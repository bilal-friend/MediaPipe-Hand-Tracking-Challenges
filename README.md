# 🖐️ MediaPipe Hand Tracking Projects

A collection of **beginner-friendly computer vision projects** built using **Python**, **OpenCV**, and **MediaPipe Hand Landmarker**.

This repository documents my journey learning hand tracking step by step, starting from simple landmark detection and gradually building more interactive computer vision applications.

The goal is not simply to use MediaPipe, but to understand the data it provides and build my own logic on top of it.

---

## 🎯 Main Goal

Learn how to transform:

```text
Webcam
   ↓
MediaPipe
   ↓
Hand Landmarks
   ↓
Coordinates
   ↓
Logic
   ↓
Interaction
```

The projects start with simple landmark-based detection and progressively move toward more advanced hand-controlled applications.

---

## 🚀 Progress

```text
[████████████░░░░░░░░] 60%
```

### Completed

- ✅ Finger State Detection
- ✅ Circle Control by Finger
- ✅ Finger Direction Detection

### Planned

- ⬜ Finger Counting ✌️
- ⬜ Gesture Recognition 🤟
- ⬜ Virtual Mouse 🖱️
- ⬜ Air Drawing 🎨

---

# 📂 Projects

## 1️⃣ Finger State Detection

### 🎯 Goal

Detect whether the index finger is pointing **up** or **down**.

The project uses the four main landmarks of the index finger:

```text
5 = Index MCP
6 = Index PIP
7 = Index DIP
8 = Index TIP
```

The program compares their `y` coordinates:

```python
if landmark1.y > landmark2.y > landmark3.y > landmark4.y:
    # Finger is up

elif landmark1.y < landmark2.y < landmark3.y < landmark4.y:
    # Finger is down
```

### 🧠 Main Concepts

- Hand detection
- Accessing specific landmarks
- Landmark coordinates
- Comparing `y` coordinates
- Conditional statements
- OpenCV text display

### 💡 What I learned

MediaPipe gives the landmark coordinates, but the interpretation is created using Python logic.

```text
Landmarks
    ↓
Coordinates
    ↓
Comparison
    ↓
Condition
    ↓
Finger State
```

---

# 2️⃣ Circle Control by Finger

### 🎯 Goal

Control the position of a circle using the index fingertip.

The project uses:

```text
Landmark 8
     ↓
Index Finger TIP
```

The landmark coordinates are converted into OpenCV pixel coordinates:

```python
landmark = result.hand_landmarks[0][8]

x = int(landmark.x * frame.shape[1])
y = int(landmark.y * frame.shape[0])
```

Then OpenCV draws the circle at that position:

```python
cv2.circle(
    frame,
    (x, y),
    50,
    (255, 0, 0),
    -1
)
```

### 🧠 Main Concepts

- Accessing a specific landmark
- `result.hand_landmarks[0][8]`
- Normalized coordinates
- Pixel coordinates
- `frame.shape`
- OpenCV drawing
- Real-time tracking

### 💡 Main idea

```text
Index Finger
     ↓
Landmark 8
     ↓
x / y coordinates
     ↓
OpenCV coordinates
     ↓
Circle position
```

The circle follows the index fingertip in real time.

---

# 3️⃣ Finger Direction Detection

### 🎯 Goal

Detect the direction in which the index finger is pointing.

The project compares:

```text
5 = Index MCP
8 = Index TIP
```

The difference between their coordinates is calculated:

```python
dx = abs(tip.x - mcp.x)
dy = abs(tip.y - mcp.y)
```

Then we determine whether the finger is mainly horizontal or vertical:

```python
if dx > dy:
    # Horizontal

else:
    # Vertical
```

Finally, the direction can be determined:

```text
Horizontal
   ├── Left
   └── Right

Vertical
   ├── Up
   └── Down
```

### 🧠 Main Concepts

- Landmark comparison
- `x` coordinates
- `y` coordinates
- `dx`
- `dy`
- Horizontal vs vertical detection
- Direction classification
- Mathematical logic

### 💡 Main idea

Instead of asking MediaPipe:

```text
"What direction is the finger pointing?"
```

I use the landmark data to create my own logic:

```text
MCP + TIP
    ↓
dx / dy
    ↓
Horizontal / Vertical
    ↓
Left / Right / Up / Down
```

---

# 🔮 Planned Projects

The following projects are planned for the next stages of the repository.

---

## 4️⃣ Finger Counting ✌️

### 🎯 Goal

Detect how many fingers are raised.

Possible results:

```text
☝️ 1
✌️ 2
🤟 3
🖐️ 5
```

### Planned concepts

- Multiple finger detection
- Landmark relationships
- Boolean conditions
- Counting logic

---

## 5️⃣ Gesture Recognition 🤟

### 🎯 Goal

Recognize predefined hand gestures.

Possible gestures:

```text
✊ Fist
🖐️ Open Hand
☝️ One Finger
✌️ Two Fingers
👍 Thumbs Up
```

### Planned concepts

- Multiple landmarks
- Finger states
- Combining conditions
- Gesture classification

---

## 6️⃣ Virtual Mouse 🖱️

### 🎯 Goal

Control the computer mouse using hand movements.

Possible controls:

```text
☝️ Move finger
     ↓
Mouse movement

🤏 Pinch
     ↓
Mouse click

✋ Gesture
     ↓
Different actions
```

### Planned concepts

- Hand tracking
- Screen coordinates
- Mouse control
- Gesture-based interaction

---

## 7️⃣ Air Drawing 🎨

### 🎯 Goal

Draw in the air using the index finger.

Concept:

```text
Index Finger
      ↓
Landmark 8
      ↓
Track position
      ↓
Store previous position
      ↓
Draw line
```

Instead of controlling a circle, the movement of the finger will create a drawing.

### Planned concepts

- Previous vs current coordinates
- Drawing with OpenCV
- Lines
- Tracking movement
- Real-time interaction

---

# 🧠 Main Concepts Learned

Throughout these projects, the main ideas are:

```text
MediaPipe
    ↓
Hand Detection
    ↓
21 Landmarks
    ↓
Specific Landmark
    ↓
x / y / z
    ↓
Coordinate Conversion
    ↓
Mathematical Relationships
    ↓
Conditions
    ↓
Computer Vision Logic
    ↓
Interaction
```

---

# 🔢 The 21 Hand Landmarks

MediaPipe provides **21 landmarks for each detected hand**.

```text
0  = Wrist

1  = Thumb CMC
2  = Thumb MCP
3  = Thumb IP
4  = Thumb TIP

5  = Index MCP
6  = Index PIP
7  = Index DIP
8  = Index TIP

9  = Middle MCP
10 = Middle PIP
11 = Middle DIP
12 = Middle TIP

13 = Ring MCP
14 = Ring PIP
15 = Ring DIP
16 = Ring TIP

17 = Pinky MCP
18 = Pinky PIP
19 = Pinky DIP
20 = Pinky TIP
```

---

# 🔍 Important MediaPipe Concept

One of the most important things learned in this project is:

```python
result.hand_landmarks
```

This is a **list of detected hands**.

For example:

```text
result.hand_landmarks
        │
        ├── [0] → First detected hand
        │
        └── [1] → Second detected hand
```

To access the first hand:

```python
result.hand_landmarks[0]
```

To access a specific landmark:

```python
result.hand_landmarks[0][8]
```

This means:

```text
[0] → First detected hand
[8] → Index Finger TIP
```

So:

```python
result.hand_landmarks[0][8]
```

means:

> Get landmark 8 from the first detected hand.

---

# 🛠️ Requirements

## Python

Python 3.x

## Libraries

Install the required packages:

```bash
python -m pip install opencv-python mediapipe numpy
```

If MediaPipe installation takes a long time:

```bash
python -m pip install mediapipe --timeout 120
```

---

# 💻 Technologies

- 🐍 Python
- 👁️ OpenCV
- 🖐️ MediaPipe
- 🔢 NumPy

---

# 📁 Project Structure

```text
MediaPipe-Hand-Tracking/
│
├── README.md
├── hand_landmarker.task
│
├── 01_finger_state.py
├── 02_circle_control.py
├── 03_finger_direction.py
│
├── 04_finger_counting.py
├── 05_gesture_recognition.py
├── 06_virtual_mouse.py
└── 07_air_drawing.py
```

The last four files represent planned projects and will be added as development continues.

---

# 📈 Learning Progress

```text
Level 1
│
├── ✅ Finger State
├── ✅ Circle Control
└── ✅ Finger Direction
│
↓
Level 2
│
├── ⬜ Finger Counting
└── ⬜ Gesture Recognition
│
↓
Level 3
│
├── ⬜ Virtual Mouse
└── ⬜ Air Drawing
```

---

# 💭 Quote

> **"MediaPipe provides the data. I build the logic."**

Another principle behind this project:

> **"Understanding is more powerful than copying."**

---

# 👨‍💻 Author

**Bilal Elemrani**

Student at **ISPITS Tangier** 🎓

Currently learning and practicing:

- 🐍 Python
- 👁️ OpenCV
- 🖐️ MediaPipe
- 🤖 YOLO
- 🧠 Computer Vision

---

# 🏁 Status

🚧 **Work in Progress**

This repository will continue to evolve as new hand tracking challenges and projects are completed.

```text
Learn
  ↓
Experiment
  ↓
Make mistakes
  ↓
Debug
  ↓
Build
  ↓
Understand
  ↓
Repeat
```

---
