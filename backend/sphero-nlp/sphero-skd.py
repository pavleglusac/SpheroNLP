import time
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color

toy = scanner.find_toy()

with SpheroEduAPI(toy) as droid:

    droid.set_main_led(Color(r=255, g=0, b=0))
    droid.set_heading(0)
    droid.set_speed(30)

    droid.roll(0, 30, 3)

    time.sleep(3)
    droid.roll(0, 0, 1)
    # disconnect
