import numpy as np


def main():
    freqs = np.geomspace(125, 8000, 7)
    print(np.round(freqs))


if __name__ == "__main__":
    main()
