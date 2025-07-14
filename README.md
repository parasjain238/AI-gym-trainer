AI GYM TRAINER
Overview
AI Gym Trainer is an innovative fitness application that leverages AI-powered computer vision to enhance your workout experience. The system detects body parts in real-time, analyzes joint angles to ensure proper exercise form, and tracks repetition counts for various exercises. Whether you're a beginner or an advanced athlete, AI Gym Trainer provides personalized feedback to optimize your workouts.
Features

Body Part Detection: Utilizes computer vision to identify key body parts and joints during exercises.

Angle Analysis: Calculates joint angles to provide real-time feedback on exercise form, ensuring correct posture and movement.
Repetition Counting: Automatically tracks and counts exercise repetitions with high accuracy.
Real-Time Feedback: Offers visual or auditory cues to correct form and improve performance.
User-Friendly Interface: Simple and intuitive design for seamless interaction during workouts.

How It Works

Setup: Use a camera-enabled device (webcam, smartphone, etc.) to capture your movements.
Body Tracking: The AI model processes video input to detect body landmarks (e.g., shoulders, elbows, knees).
Angle Calculation: The system computes joint angles to verify if they align with the correct form for the selected exercise.
Rep Counting: Tracks movement patterns to count repetitions accurately.
Feedback: Provides real-time suggestions to adjust posture or movement for optimal results.

Installation

Clone the repository:
git clone https://github.com/parasjain238/AI-gym-trainer


Navigate to the project directory:

cd ai-gym-trainer


Install dependencies:

pip install -r requirements.txt


Run the application:

python main.py



Requirements

Python 3.8+
OpenCV
MediaPipe (for body part detection)
NumPy
A camera-enabled device

Usage

Launch the application with a connected camera.
Select an exercise from the available list (e.g., squats, push-ups).
Follow the on-screen instructions to position yourself within the camera frame.
Perform the exercise while the AI tracks your movements, provides angle feedback, and counts reps.
Review your performance summary after completing the session.

Contributing

Contributions are welcome! To contribute:

Fork the repository.

Create a new branch (git checkout -b feature-branch).
Make your changes and commit (git commit -m "Add new feature").
Push to the branch (git push origin feature-branch).
Open a pull request.

images after complete working for pull-up 

![output pull-up](https://github.com/user-attachments/assets/7df4ec1a-e8e7-4af3-96ea-944ee9f0e476)


License
This project is licensed under the MIT License. See the LICENSE file for details.
Contact

For questions or feedback, reach out via email - jainparas0987.com or open an issue on GitHub.
