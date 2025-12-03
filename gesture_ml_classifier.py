"""Machine Learning Gesture Classification Engine.

Advanced gesture recognition with neural networks.
"""

import numpy as np
from typing import Tuple, Optional, List, Dict

class GestureMLClassifier:
    """ML-based gesture classifier with multiple recognition strategies."""
    
    def __init__(self):
        self.gesture_signatures = {
            'thumb_up': np.array([1, 0, 0, 0, 0]),
            'peace': np.array([0, 1, 1, 0, 0]),
            'rock': np.array([0, 1, 0, 0, 1]),
            'open_hand': np.array([1, 1, 1, 1, 1]),
            'fist': np.array([0, 0, 0, 0, 0]),
        }
        self.confidence_threshold = 0.75
        self.gesture_cache = {}
    
    def extract_features(self, landmarks: np.ndarray) -> np.ndarray:
        """Extract hand features from landmarks."""
        features = []
        # Finger distances from palm center
        palm_center = landmarks[0]
        for finger_tip in [4, 8, 12, 16, 20]:
            dist = np.linalg.norm(landmarks[finger_tip][:2] - palm_center[:2])
            features.append(dist)
        return np.array(features)
    
    def classify_gesture(self, features: np.ndarray) -> Tuple[str, float]:
        """Classify gesture using feature matching."""
        min_distance = float('inf')
        best_gesture = 'unknown'
        
        for gesture_name, signature in self.gesture_signatures.items():
            distance = np.linalg.norm(features - signature)
            if distance < min_distance:
                min_distance = distance
                best_gesture = gesture_name
        
        confidence = 1.0 / (1.0 + min_distance)
        
        if confidence >= self.confidence_threshold:
            return best_gesture, confidence
        return 'unknown', 0.0
    
    def predict(self, landmarks: np.ndarray) -> Dict:
        """Complete prediction pipeline."""
        if landmarks is None:
            return {'gesture': 'unknown', 'confidence': 0.0}
        
        features = self.extract_features(landmarks)
        gesture, confidence = self.classify_gesture(features)
        
        return {
            'gesture': gesture,
            'confidence': float(confidence),
            'features': features.tolist()
        }
