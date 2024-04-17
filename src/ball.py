import pygame
from math import log

class Ball:
    
    def __init__(self, screen_width, screen_height, x, y, r, speed, color, fps, gravity):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.color = color
        self.x = x #center x
        self.y = y #center y
        self.r = r #ball radius
        self.m = 1000 #ball mass
        self.elasticity = 0.8
        self.airDrag = 0.99
        self.groundFriction = 0.98
        self.fps = fps
        self.gravity = gravity
        self.grounded = False
        self.speed = speed
        self.vel = [speed*1/fps, speed*1/fps] #calculate the initial to move per frame to reach a given pixels/second
        
    def update(self):
        nx = self.x + self.vel[0] #new x position of the ball's center
        ny = self.y + self.vel[1] #new y position of the ball's center
        
        if ny+self.r > self.screen_height or ny-self.r <= 0:
            self.vel[1] *= -self.elasticity
        if nx+self.r > self.screen_width or nx-self.r <= 0:
            self.vel[0] *= -self.elasticity
        if abs(self.vel[0]*self.fps) < 4:
            self.vel[0] = 0
        if abs(self.vel[1]*self.fps) < 4:
            self.vel[1] = 0
        
        #if on the ground and not moving
        if ny+self.r >= self.screen_height and self.vel[1] == 0:
            self.y = self.screen_height-self.r
        #if not on the ground
        elif not ny+self.r >= self.screen_height and self.vel[1] != 0:
            self.vel[1] += (self.m/self.gravity)*1/self.fps
        
        self.vel[0] *= self.airDrag
        self.vel[1] *= self.airDrag
        
        # update positions post bouncing, gravity, and friction
        nx = self.x + self.vel[0] #new x position of the ball's center
        ny = self.y + self.vel[1] #new y position of the ball's center
        
        self.x = nx
        self.y = ny
        
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r) #draw a circle from attributes