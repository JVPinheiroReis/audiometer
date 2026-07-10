import numpy as np
import sounddevice as sd

from audiometer.tones import SAMPLE_RATE


def play(sine):
    stereo = np.column_stack((sine, sine))
    sd.play(stereo, SAMPLE_RATE)
    sd.wait()


def play_left(sine):
    stereo = np.column_stack((sine, np.zeros_like(sine)))
    sd.play(stereo, SAMPLE_RATE)
    sd.wait()


def play_right(sine):
    stereo = np.column_stack((np.zeros_like(sine), sine))
    sd.play(stereo, SAMPLE_RATE)
    sd.wait()
