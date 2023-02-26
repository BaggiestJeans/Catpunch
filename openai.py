import gym
import pygame
import gym
class CustomEnv(gym.Env):
    # [...]
    def render(self):
        global window
        color = (100,255,0)
        x1, y1, x2, y2, linewidth, radius = 10, 100, 20, 200, 5, 10
        # make draw calls
        window.fill(color) # fill background with color
        pygame.draw.line(window,color,(x1,y1),(x2,y2),linewidth) # draw a line
        pygame.draw.circle(window,color,(x1,y1),radius) # draw a circle