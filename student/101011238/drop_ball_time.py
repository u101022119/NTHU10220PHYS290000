import math
print 'A ball is dropped from a tower of height h with initial velocity zero.'
print 'I can tell when the ball hits the ground.'
height = input('Enter the height(m):')

time = math.sqrt(height*2/9.8)

print 'The ball will hit the ground after',time,'seconds.'
