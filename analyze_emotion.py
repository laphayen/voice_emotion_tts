# analyze_emotion.py
from kobert_emotion import analyze_emotion  # KoBERT 감정 분석 모듈화했다고 가정

text = "깊은 숲 속에 귀여운 토끼가 살았어요."
emotion = analyze_emotion(text)
print(f"감정 결과: {emotion}")  # e.g., "joy", "sad", "surprise"