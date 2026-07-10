from audiometer.calibrator import calibrate

FREQUENCIES = [
    125,
    250,
    500,
    1000,
    2000,
    4000,
    8000,
]

print("The worst ear:")
print("1) Left")
print("2) Right")

r = input("> ")

curve = {f: calibrate(f, r) for f in FREQUENCIES}
print(curve)
