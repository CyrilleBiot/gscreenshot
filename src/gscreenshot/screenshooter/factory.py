from gscreenshot.screenshooter.scrot import Scrot
from gscreenshot.screenshooter.imlib_2 import Imlib2

class ScreenshooterFactory(object):

    def __init__(self, screenshooter=None):
        self.screenshooter = screenshooter
        self.screenshooters = [
                Scrot,
                Imlib2
                ]

    def create(self):
        if (self.screenshooter is not None):
            return self.screenshooter

        for shooter in self.screenshooters:
            if shooter.can_run():
                return shooter()

