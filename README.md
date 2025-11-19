# Hand Gesture Recognition System

## Overview

AI-powered hand gesture recognition system using MediaPipe for real-time palm tracking and interactive kinematic HUD visualization. This project captures webcam input, detects hands using MediaPipe, and draws a white, mechanical-style kinematic HUD over the hand with palm-centered radial UI, finger bones, rotation readout, and 3D elements.

## Features

- Real-time hand detection and tracking
- Palm-anchored kinematic dashboard
- Interactive HUD visualization
- MediaPipe integration
- OpenCV-based computer vision

## Files

- `requirements.txt` — Python dependencies
- `main.py` — Application entrypoint and webcam loop
- `hand_overlay.py` — Functions for drawing the HUD and computing kinematics
- `utils.py` — Helper functions (smoothing, geometry)

## Installation

### Requirements
- Python 3.8+
- Webcam

### Setup (Windows PowerShell)

1. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python main.py
```

## Usage Notes

- Works with a single hand in frame by default
- For multi-hand tracking, toggle the flag in `main.py`
- Adjust smoothing and drawing constants in `hand_overlay.py`

## License

MIT License - See LICENSE file for details
