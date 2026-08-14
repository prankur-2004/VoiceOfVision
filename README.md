🚀 VoiceOfVision: AI-Powered Accessibility Assistant
An intelligent, real-time computer vision application built with Python, YOLOv8, OpenCV, and Text-to-Speech (pyttsx3) designed to assist visually impaired individuals by detecting objects through a live webcam feed and speaking out their names.

🌟 Key Features
Real-Time Object Detection: Powered by Ultralytics YOLOv8 for fast and accurate identification of everyday objects.

Audio Feedback (Text-to-Speech): Automatically announces detected objects using pyttsx3.

Smart Cooldown Mechanism: Prevents audio spam by implementing a configurable time gap (default: 5 seconds) between announcements.

Duplicate Removal: Filters out duplicate detections in the same frame to speak a clean, concise list of objects (e.g., "I see chair, person").

Visual Overlays: Draws bounding boxes and displays confidence scores directly on the live OpenCV video stream.

🛠️ Tech Stack
Language: Python 3.8+

Computer Vision: OpenCV (cv2)

AI Model: YOLOv8 (Ultralytics)

Speech Synthesis: pyttsx3

📦 Prerequisites & Installation
Follow these steps to set up and run the project locally on your machine.

1. Clone the Repository
Bash
git clone https://github.com/your-username/VoiceOfVision.git
cd VoiceOfVision
2. Create a Virtual Environment (Recommended)
Bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
3. Install Dependencies
Bash
pip install opencv-python pyttsx3 ultralytics
🚀 Usage
Run the main script to start the assistant:

Bash
python main.py
How it works: Point your webcam toward your surroundings. The AI will detect objects with a confidence level greater than 50% (0.5), box them in green, and voice out the names.

Exit: Press the q key on your keyboard while the video window is active to close the application.

⚙️ Configuration
You can easily customize settings inside the script:

Confidence Threshold: Change if conf > 0.5: to a higher value for stricter accuracy or lower value for more detections.

Speech Cooldown: Modify cooldown_seconds = 5 to make the voice announcements faster or slower.

Speech Rate: Adjust engine.setProperty('rate', 160) to speed up or slow down the speech voice.
