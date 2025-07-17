"""
Situation:
A bullet is being fired from a rifle.
As soon as the bullet leaves the tube, the shell leaves the rifle horizontally
Assuming that the plane in front of the rifle is flat and has no obstacles and the rifle is being shot perfectly horizontally:
So the bullet and the shell start at the same height
Which ones hits the ground first: the shell or the bullet. To find out, write the functions shell_falls and bullet_falls.
Use them to print the duration of each fall until they hit the ground.

write two functions: 
one simulates the fall of the shell
one simulates the fall of the bullet

your job is to determine how long the shell takes to fall to the ground
and to determine how long the bullet takes to hit to the ground

you MUST at least write the following functions:
shell_falls
bullet_falls
Write all you need

so write your own simplistic physics engine to prove your point
"""
import sys

def object_falls(height):
    value = ((2*height)/9.81)**(.5)
    return (value)

def shell_falls(height):
    return (object_falls(height))

def bullet_falls(height):
    return (object_falls(height))

def fall_distance(duration):
    value = .5*9.81*duration**2
    return (value)

print(shell_falls(1))
print(bullet_falls(1))

#def shell_falls(height):
