import numpy as np
import sounddevice as sd

from .tones import SAMPLE_RATE


def play_left(signal):
    stereo = np.column_stack((signal, np.zeros_like(signal)))
    sd.play(stereo, SAMPLE_RATE)
    sd.wait()


def play_right(signal):
    stereo = np.column_stack((np.zeros_like(signal), signal))
    sd.play(stereo, SAMPLE_RATE)
    sd.wait()
