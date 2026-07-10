from audiometer.player import play_left, play_right
from audiometer.tones import sine


def ask(frequency, gain):
    r = ""

    while r not in ["1", "2", "3", "4"]:
        print(f"\n{frequency} Hz")
        print(f"Testing: {gain:.1f} dB")
        print()
        print("1) Left is lower")
        print("2) Right is lower")
        print("3) Repeat")
        print("4) Equal")

        r = input("> ")

    return r


def calibrate(frequency: int, ear: str) -> float:
    low = 0.0
    high = 20.0
    gain = 0

    while high - low > 0.5:
        gain = (low + high) / 2

        if ear == "1":
            left = sine(frequency, gain_db=gain)
            right = sine(frequency, gain_db=0)

        else:
            left = sine(frequency, gain_db=0)
            right = sine(frequency, gain_db=gain)

        play_left(left)
        play_right(right)

        match ask(frequency, gain):
            case "1":
                low = gain

            case "2":
                high = gain

            case "3":
                continue

            case "4":
                break

    return gain
