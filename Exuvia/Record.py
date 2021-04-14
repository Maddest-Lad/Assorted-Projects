import wave
import os
import time
import pyaudio

CHUNK = 1024  # Record In Chunks of 1024 Samples
SAMPLE_FORMAT = pyaudio.paInt16  # 16 bits per sample
CHANNELS = 2
FS = 44100  # Record at 44100 samples per second
SECONDS = 3
FILENAME = "output.wav"


def record(length: int):
    # Create an interface to PortAudio
    p = pyaudio.PyAudio()

    stream = p.open(format=SAMPLE_FORMAT, channels=CHANNELS, rate=FS, frames_per_buffer=CHUNK, input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(FS / CHUNK * SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Only Keep So Much Data
    files = [file for file in os.listdir(os.path.join(os.getcwd(), "data"))]
    files.sort(key=os.path.getmtime)

    print(files)

    # Save the recorded data as a WAV file
    wf = wave.open("output.wav", 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(SAMPLE_FORMAT))
    wf.setframerate(FS)
    wf.writeframes(b''.join(frames))
    wf.close()

