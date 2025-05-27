import requests
import tkinter as tk
import cv2
import time
import os

BASE_URL = 'https://api.themoviedb.org/3'
urll = "https://api-us.faceplusplus.com/facepp/v3/detect"
API_KEY = os.getenv("TMDB_API_KEY")
API_KEY2 = os.getenv("FACEPP_API_KEY")
API_SECRET = os.getenv("FACEPP_API_SECRET")
EMO = {
  "happiness": [35, 12, 16, 10402],      
  "sadness": [35, 16, 10751, 10402],    
  "anger": [28, 99, 12],             
  "surprise": [9648, 12, 878],    
  "fear": [14, 18, 12],           
  "disgust": [35, 878, 99],      
  "neutral": [18, 10749, 99],        
}

#Initialize
root = tk.Tk()
root.withdraw()  
save_dir = "captured_images"
os.makedirs(save_dir, exist_ok=True)

#Functions
def gui(result):
    root = tk.Tk()
    root.title("Recommend")

    label = tk.Label(root, text=result)
    label.pack(padx=20, pady=20)

    root.mainloop()
def get_movies_by_genres(genre_ids):  
	genre_str = ','.join(str(g) for g in genre_ids)
	url = f'{BASE_URL}/discover/movie'
	params = {
		'api_key': API_KEY,
		'with_genres': genre_str,
		'language': 'en-US',
		'sort_by': 'popularity.desc',
		'page': 1,
		'include_adult': True
	}
	response = requests.get(url, params=params)
	if response.status_code == 200:
		movies = response.json().get('results', [])
		s=''
		for movie in movies[:6]:  
			s+=movie['title']+'\n'
		gui(s)
	else:
		print(f"Error: {response.status_code}")
def detect(img):
	params = {
	    "api_key": API_KEY2,
	    "api_secret": API_SECRET,
	    "return_attributes": "emotion"
	}	
	image_path = str(img)
	files = {"image_file": open(image_path, "rb")}	
	response = requests.post(urll, data=params, files=files)
	data = response.json()	
	if data.get("faces"):
		emotions = data["faces"][0]["attributes"]["emotion"]
		return emotions
	else:
	    print("No face detected.")


#Capturing image
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()
print("Capturing 5 images...")

for _ in range(2):
    ret, frame = cap.read()
    time.sleep(0.1)  

for i in range(5):
    ret, frame = cap.read()
    if not ret:
        print(f"Failed to capture image {i+1}")
        continue
    filename = os.path.join(save_dir, f"image_{i+1}.jpg")
    cv2.imwrite(filename, frame)
    print(f"Saved: {filename}")
    time.sleep(2)  

cap.release()

#base reference
direct = os.listdir(save_dir)
direct = [os.path.join(save_dir, f) for f in direct if f.endswith('.jpg')]

#print("directory: ", direct)

all_set=[]
for i in direct:
    emo = detect(i)
    if emo:
        all_set.append(emo)

#print("directory: ", all_set)
        
base={
	"anger":0.000,
	"disgust":0.000,
	"fear":0.000,
	"happiness":0.002,
	"neutral":99.998,
	"sadness":0.000,
	"surprise":0.000
}

for a,b in enumerate(all_set):
    for i,j in b.items():
        base[i] += j/(len(b))
        
#print("base: ", base,end='\n')

#analyse
cap1 = cv2.VideoCapture(0)
if not cap1.isOpened():
    print("Error: Could not open webcam.")
    exit()
print("Capturing final")

for _ in range(2):
    ret1, frame1 = cap1.read()
    time.sleep(0.1)  
    
ret1, frame1 = cap1.read()
if not ret1:
    print("Failed to capture image")
filename1 = os.path.join(save_dir, "image_f.jpg")
cv2.imwrite(filename1, frame1)
print(f"Saved: {filename1}")
time.sleep(2)  
cap1.release()

#Final Image analysis
predicted=detect(filename1)

for i,j in predicted.items():
    predicted[i]-=base[i]
    predicted[i]=round(predicted[i],3)

#sorting by emotions density
sorted_p = dict(sorted(predicted.items(), key=lambda item: item[1], reverse=True))

final_e=[]
z=4
for k, v in list(sorted_p.items())[:3]:
    z-=1
    for i in EMO[k][:z]:
      final_e.append(i)

get_movies_by_genres(final_e)
