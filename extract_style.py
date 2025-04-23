# extract_style.py
from styletts2.synthesizer import Synthesizer

synthesizer = Synthesizer(
    config_path="resources/model/styletts2/config.yml",
    ckpt_path="resources/model/styletts2/epochs_2nd_00020.pth"
)

style_embed = synthesizer.compute_style_embedding("parent.wav")