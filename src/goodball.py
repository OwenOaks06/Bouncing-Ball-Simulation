from lib import Vector

class Ball:
    def __init__(self, screen_width, screen_height, x, y, r):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x = x
        self.y = y
        self.r = r
        self.m = 100
        
