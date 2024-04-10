import sounddevice as sd
import wavio as wv

freq = 44100

duration = 10

recording = sd.rec(int(duration*freq), samplerate = freq, channels=2)
print("recording now for ", duration, " seconds.")
sd.wait()

wv.write("recording.wav", recording, freq, sampwidth = 2)
