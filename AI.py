import pygame
import random
import time
bin=[0,1]
def ran(num):
    num=random.randint(0,6)
    return num
def ran2(nums):
    bin=[0,1]
    nums=[]
    for i in range(0,6):
        nums.append(random.choice(bin))
    return nums