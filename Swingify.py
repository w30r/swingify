import librosa
from pydub import AudioSegment
from pydub.utils import mediainfo

swingThisSongFileThing = "NJcookie157"
tempoOfTheSong = 157

# Load the audio file
audio_file = "./" + swingThisSongFileThing + ".wav"
audio_data, sample_rate = librosa.load(audio_file, sr=44100)
print("Loaded Files.")

# Calculate the duration of one half beat in samples
half_beat_duration = (60 / tempoOfTheSong) / 2
half_beat_duration_samples = int(half_beat_duration * sample_rate)
print("Calculating..")

# Slice the audio on every half beat
slices = []
for i in range(0, len(audio_data), half_beat_duration_samples):
    slice = audio_data[i:i+half_beat_duration_samples]
    slices.append(slice)

print("Slicing the audio on every half beat")
# Modify every other half beat to be 1.5x faster
for i in range(1, len(slices), 2):
    slices[i] = librosa.effects.time_stretch(slices[i], rate=2)
print("Modifying every other half beat to be 2.5x faster")

# Concatenate the modified slices back into a single audio array
modified_audio = []
for slice in slices:
    modified_audio.extend(slice)
print("Concatenating slices.")

# Export the modified audio file
print("Exporting...")
modified_audio = librosa.util.normalize(modified_audio)  # Normalize the audio
# Scale to 16-bit integer
modified_audio = (modified_audio * 32767).astype("int16")
audio_segment = AudioSegment(modified_audio.tobytes(
), frame_rate=sample_rate, sample_width=2, channels=1)
output_file = "./exports/"+swingThisSongFileThing+" (swing edit).wav"
print("Exporting...")
audio_segment.export(output_file, format="wav")

print("DONE ✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅")
