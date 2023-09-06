import pyaudio
import wave
import pygame

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 15
FILE_NAME = "ses_kaydi.wav"

audio = pyaudio.PyAudio()

try:
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=1024)

    print("Ses kaydı başlıyor...")

    frames = []
    RECORD_FRAMES = int(RATE * RECORD_SECONDS / 1024)

    for i in range(RECORD_FRAMES):
        data = stream.read(1024)
        frames.append(data)

    print("Ses kaydı tamamlandı.")

    stream.stop_stream()
    stream.close()

    with wave.open(FILE_NAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(2)
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    print(f"Ses kaydı '{FILE_NAME}' dosyasına kaydedildi.")

    pygame.mixer.init()
    pygame.mixer.music.load(FILE_NAME)
    pygame.mixer.music.play()
    pygame.time.wait(15000)
finally:
    audio.terminate()
    pygame.mixer.quit()