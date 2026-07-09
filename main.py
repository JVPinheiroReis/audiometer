from audiometer.player import play_left, play_right
from audiometer.tones import sine

left_sine = sine(1000, gain_db=0)
right_sine = sine(1000, gain_db=0)

play_left(left_sine)
play_right(right_sine)
