# 🎭 Emotion-Based Movie Recommender

This project captures images from your webcam, detects your facial emotions using the Face++ API, and recommends movies from TMDB based on your emotional state. The final emotion and results are displayed in a simple GUI.

## 📸 Features

- Captures 5 images with a 2-second delay between each.
- Analyzes facial emotions using the Face++ API.
- Averages base emotions to create a personal emotional baseline.
- Captures one final image to detect your *current* emotional deviation.
- Recommends personalized movies from TMDB based on your mood.
- Displays the final detected emotion in a GUI window.

## 🧠 Emotion to Genre Mapping

| Emotion     | TMDB Genre IDs                  |
|-------------|---------------------------------|
| Happy       | 35, 12, 16, 10402               |
| Sad         | 35, 16, 10751, 10402            |
| Angry       | 28, 99, 12                      |
| Surprised   | 9648, 12, 878                   |
| Fearful     | 14, 18, 12                      |
| Disgusted   | 35, 878, 99                     |
| Neutral     | 18, 10749, 99                   |

> These mappings are defined in the `EMO` dictionary in the script and can be modified.

---

## 🚀 Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/emotion-recommender.git
cd emotion-recommender
```

### 2. Install dependencies
```bash
pip install requests opencv-python
```

### 3. Get API keys
- **Face++ API**: https://www.faceplusplus.com/
- **TMDB API**: https://www.themoviedb.org/documentation/api

Replace the placeholder keys in the script:
```python
API_KEY = 'your_tmdb_api_key'
API_KEY2 = 'your_face++_api_key'
API_SECRET = 'your_face++_api_secret'
```

---

## 📂 Project Structure

```
emotion-recommender/
│
├── main.py             # Main script
├── captured_images/    # Automatically created for storing webcam images
└── README.md           # This file
```

---

## 🖥️ How to Run

```bash
python main.py
```

- The script will open your webcam, take images, analyze emotions, recommend movies, and finally display the detected emotion in a GUI.

---

## ⚠️ Notes

- Requires a working webcam.
- Internet connection is necessary for API requests.
- API limits (especially for Face++) may apply on free plans.
- Ensure your webcam is properly configured or use dummy images for testing.

---

## 💡 Future Improvements

- Support for live video emotion tracking
- Store emotion history and trends
- Integrate with more streaming platforms (e.g., Netflix, Prime)
- Enhance GUI with movie posters and UI styling

---

## 🧠 Created By

**Sagnik Sengupta**  
Class 12 Student | Aspiring neuroscientist & AI builder | Passionate about tech and mental health
