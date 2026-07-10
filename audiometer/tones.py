import numpy as np

SAMPLE_RATE = 48000
AMPLITUDE = 0.5


def sine(
    frequency: float,
    duration: float = 1,
    gain_db: float = 0.0,
):
    t = np.linspace(
        0,
        duration,
        int(SAMPLE_RATE * duration),
        endpoint=False,
    )

    wave = AMPLITUDE * np.sin(2 * np.pi * frequency * t)

    gain = 10 ** (gain_db / 20)

    return wave * gain
