# synthesize.py
from styletts2.synthesizer import Synthesizer

synthesizer = Synthesizer(
    config_path="resources/model/styletts2/config.yml",
    ckpt_path="resources/model/styletts2/epochs_2nd_00020.pth"
)

text = "깊은 숲 속에 귀여운 토끼가 살았어요."
style = synthesizer.compute_style_embedding("parent.wav")

# 감정: "joy"
output_path = "storybook_output.wav"
synthesizer.tts(text, style_vector=style, emotion="joy", output_path=output_path)