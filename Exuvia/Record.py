import wave
import string
import random
import pyaudio

CHUNK = 1024  # Record In Chunks of 1024 Samples
SAMPLE_FORMAT = pyaudio.paInt16 # 16 bits per sample
CHANNELS = 2
FS = 44100  # Record at 44100 samples per second
SECONDS = 300  # 10 Min


def record():
    # Create an interface to PortAudio
    p = pyaudio.PyAudio()

    stream = p.open(format=SAMPLE_FORMAT, channels=CHANNELS, rate=FS, frames_per_buffer=CHUNK, input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for _ in range(0, int(FS / CHUNK * SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Random Filename
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

    # Save the recorded data as a WAV file
    wf = wave.open("data/{}.wav".format(res), 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(SAMPLE_FORMAT))
    wf.setframerate(FS)
    wf.writeframes(b''.join(frames))
    wf.close()


while True:
    record()
