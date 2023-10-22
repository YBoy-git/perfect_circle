import sys
import time
import math
import pyautogui


# constants

SCREEN_SIZE = pyautogui.size()
CENTER_POINT = pyautogui.Point(x=(SCREEN_SIZE[0]) / 2, y=(SCREEN_SIZE[1] - 40) / 2)
MIN_STEP = 1
DEFAULT_STEP = 6
MAX_STEP = 180
MIN_RADIUS = 130
MAX_RADIUS = min(CENTER_POINT.x, CENTER_POINT.y)
DEFAULT_WAITING_TIME = 3


def draw_circle(radius, step, center_point):
    pyautogui.moveTo(center_point.x + radius, center_point.y)

    pyautogui.mouseDown()
    for i in range(0, 360 + step, step):
        x = center_point.x + radius * math.cos(math.radians(i))
        y = center_point.y + radius * math.sin(math.radians(i))
        pyautogui.moveTo(x, y)
    pyautogui.mouseUp()


def main():
    if len(sys.argv) <= 1:
        print(
            f"""Usage: python draw_circle.py radius [waiting time] [step]
 radius - pixels ({MIN_RADIUS}-{MAX_RADIUS}), waiting time - seconds (>0), step - degrees ({MIN_STEP}-{MAX_STEP}))"""
        )
        return -1

    RADIUS = int(sys.argv[1])
    if RADIUS < MIN_RADIUS or RADIUS > MAX_RADIUS:
        print("Radius must be between {} and {}".format(MIN_RADIUS, MAX_RADIUS))
        return -1

    if len(sys.argv) >= 3:
        WAITING_TIME = int(sys.argv[2])
        if WAITING_TIME < 0:
            print("Waiting time must be positive")
            return -1
    else:
        WAITING_TIME = DEFAULT_WAITING_TIME

    if len(sys.argv) >= 4:
        STEP = int(sys.argv[3])
        if STEP < MIN_STEP or STEP > MAX_STEP:
            print("Step must be between {} and {}".format(MIN_STEP, MAX_STEP))
            return -1
    else:
        STEP = DEFAULT_STEP

    print("Ctrl + C to cancel")
    time.sleep(WAITING_TIME)
    draw_circle(RADIUS, STEP, CENTER_POINT)


if __name__ == "__main__":
    main()
