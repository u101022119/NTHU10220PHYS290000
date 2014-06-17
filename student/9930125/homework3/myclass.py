import copy
class Point(object):
    pass

class Rectangle(object):
    pass

def distance_between_point(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

def move_rectangle(a,dx,dy):
    a.x += dx
    a.y += dy
    

p = Point()
p.x1 = 0
p.y1 = 0
p.x2 = 7
p.y2 = 24
print 'd =', distance_between_point(p.x1,p.y1,p.x2,p.y2)

box = Rectangle()
box.corner = Point()

box2 = copy.deepcopy(box)

box.corner.x = 100
box.corner.y = 200
box2.corner.x = 100
box2.corner.y = 200

move_rectangle(box.corner,40,50)
print 'x1, y1 become', box.corner.x,box.corner.y

move_rectangle(box2.corner,80,100)
print 'x2, y2 become', box2.corner.x,box2.corner.y
