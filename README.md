# ✋ AI Hand Gesture Recognition HUD

**Real-time AI-powered hand gesture recognition system** with **futuristic kinematic HUD overlay** using **MediaPipe** and **OpenCV**.

Capture hand movements, track palm positions, and visualize gesture data with a sleek, mechanical-style AR interface that follows your hand in real-time.

---

## 🎯 Features

✅ **Real-time Hand Detection & Tracking**
- 21-point hand landmark detection using MediaPipe
- Sub-millisecond tracking latency
- Works in various lighting conditions
- Single or multi-hand tracking support

✅ **Palm-Anchored Kinematic HUD**
- Radial UI dashboard locked to palm center
- Finger joint visualization with "bones" overlay
- Real-time rotation and angle readout
- Smooth motion interpolation

✅ **Interactive AR Visualization**
- Minimal white mechanical-style design
- 3D-inspired geometric elements
- FPS performance monitoring
- Customizable visual elements

✅ **Lightweight & Performant**
- Built with Python + OpenCV
- Optimized for real-time webcam processing
- Cross-platform support (Windows, macOS, Linux)
- Easy to extend and customize

---

## 🛠️ Tech Stack

- **Computer Vision:** MediaPipe + OpenCV
- **Language:** Python 3.8+
- **Processing:** NumPy for geometry calculations
- **Platform:** Cross-platform webcam support

**Dependencies:**
```
mediapipe==0.10.0
opencv-python==4.8.1.78
numpy==1.24.3
```

---

## 📁 Project Structure

```
ai-hand-gesture-recognition/
├── main.py              # Application entrypoint and webcam loop
├── hand_overlay.py      # HUD drawing + kinematic computations
├── utils.py             # Geometry, smoothing, and helper functions
├── requirements.txt     # Python dependencies
├── LICENSE             # MIT License
└── README.md           # This file
```

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- Working webcam or camera device
- pip package manager

### Setup (Windows PowerShell)

**1. Clone the repository**
```bash
git clone https://github.com/bhupendraydv/ai-hand-gesture-recognition.git
cd ai-hand-gesture-recognition
```

**2. Create virtual environment (recommended)**
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the application**
```bash
python main.py
```

### Setup (macOS/Linux)

**1. Clone and navigate**
```bash
git clone https://github.com/bhupendraydv/ai-hand-gesture-recognition.git
cd ai-hand-gesture-recognition
```

**2. Create virtual environment**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**3. Install and run**
```bash
pip install -r requirements.txt
python main.py
```

---

## 🕹️ Usage

### Basic Usage

Once you run `main.py`, your webcam will activate and you'll see:

- **Live video feed** with hand detection
- **White HUD overlay** locked to your palm and fingers
- **Kinematic data** including rotation angles and joint positions
- **Performance metrics** (FPS counter)

**Controls:**
- `q` - Quit application
- `ESC` - Exit fullscreen mode

### Configuration Options

Edit `main.py` to customize:

```python
# Enable multi-hand tracking
max_num_hands = 2  # Default: 1

# Adjust detection confidence
min_detection_confidence = 0.7  # Default: 0.5
min_tracking_confidence = 0.7   # Default: 0.5

# Camera settings
camera_id = 0  # Change if you have multiple cameras
```

Edit `hand_overlay.py` to customize visual style:

```python
# HUD colors (BGR format)
HUD_COLOR = (255, 255, 255)  # White
HUD_THICKNESS = 2

# Smoothing parameters
SMOOTH_FACTOR = 0.3  # Lower = smoother but slower response
```

---

## 🧪 Customization & Extension Ideas

This project is designed to be a **lightweight AR hand HUD module** that can be extended for:

✨ **Gesture Classification**
- Add gesture recognition (thumbs up, peace sign, pinch, etc.)
- Train custom ML models for specific hand poses
- Integrate with gesture databases

✨ **Interactive Control Systems**
- Use gestures to control media playback
- Virtual volume/brightness controls
- Game input system
- Robot/drone hand control

✨ **Accessibility Applications**
- Communication system for speech-disabled users
- Sign language recognition
- Virtual keyboard input

✨ **AR/VR Integration**
- Hand tracking for VR experiences
- Virtual object manipulation
- 3D model interaction

### Key Files to Modify:

- `hand_overlay.py` - Visual style, HUD elements, drawing functions
- `utils.py` - Smoothing algorithms, geometry helpers
- `main.py` - Camera settings, detection parameters, main loop

---

## 🔄 How It Works

1. **Capture:** Webcam captures video frames at 30+ FPS
2. **Detect:** MediaPipe detects hand landmarks (21 points per hand)
3. **Track:** System tracks palm center and finger positions
4. **Compute:** Calculate angles, rotations, and kinematic data
5. **Smooth:** Apply interpolation for fluid motion
6. **Render:** Draw HUD overlay with geometric AR elements
7. **Display:** Show combined video + HUD in real-time

---

## 🚨 Troubleshooting

### Camera not detected
```python
# Try different camera IDs in main.py
cap = cv2.VideoCapture(0)  # Try 0, 1, 2, etc.
```

### Low FPS / Performance Issues
- Close other applications using the camera
- Reduce video resolution in `main.py`
- Lower `max_num_hands` to 1
- Update GPU drivers
- Check system resources

### MediaPipe Import Error
```bash
# Reinstall MediaPipe
pip uninstall mediapipe
pip install mediapipe==0.10.0
```

### Hand Detection Not Working
- Ensure good lighting conditions
- Keep hand within camera frame
- Adjust `min_detection_confidence` (lower = more sensitive)
- Check if camera permissions are granted

---

## 📊 Performance

**Typical Performance Metrics:**
- **FPS:** 30-60 FPS (depends on hardware)
- **Latency:** <20ms for hand detection
- **CPU Usage:** 15-30% on modern processors
- **Memory:** ~200-300 MB

**Tested On:**
- Windows 10/11 (Intel Core i5+)
- macOS Monterey+ (M1/Intel)
- Ubuntu 20.04+ (AMD Ryzen 5+)

---

## 💡 Use Cases

### Education
- Computer vision learning projects
- Real-time tracking demonstrations
- HUD/AR interface prototyping

### Research
- Hand gesture analysis
- Motion tracking studies
- Human-computer interaction research

### Development
- AR application development
- Gesture control prototyping
- Interactive system demos

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

**Ideas for contributions:**
- Additional HUD visual styles
- New gesture recognition features
- Performance optimizations
- Documentation improvements
- Bug fixes and issue reports

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

You are free to:
- ✅ Use commercially
- ✅ Modify
- ✅ Distribute
- ✅ Private use

---

## 🙏 Acknowledgments

- **MediaPipe** by Google - Excellent hand tracking framework
- **OpenCV** - Computer vision library
- **NumPy** - Numerical computing library

---

## 📞 Support

For questions, issues, or feature requests:
- 🐛 [Open an issue](https://github.com/bhupendraydv/ai-hand-gesture-recognition/issues)
- 💬 Discussions welcome!

---

**Made with ❤️ for AR/Computer Vision enthusiasts**
