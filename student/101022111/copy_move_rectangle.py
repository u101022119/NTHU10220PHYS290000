import copy
class rectangle():
    """Represents a rectangle.attributes: width, height, corner."""
class point():
    """Represents a point in 2-D space."""
box=rectangle()
box.corner=point()
box.corner.x=0.0
box.corner.y=0.0
dx=float(raw_input("dx:"))
dy=float(raw_input("dy:"))
def print_point(p):
    print '(%g, %g)' % (p.x, p.y)
def move_rectangle(rect):
    p=point()
    p.x=rect.corner.x+dx
    p.y=rect.corner.y+dy
    print_point(p)
move_rectangle(box)

box2=copy.copy(box)
move_rectangle(box2)

box3=copy.deepcopy(box)
move_rectangle(box3)
print 'box2=copy.copy(box)'
print 'box3=copy.copy(box)'

print 'box is box2 ? Ans:',box is box2

print 'box is box3 ? Ans:',box is box3

print 'box.corner is box2.corner ? Ans:',box.corner is box2.corner

print 'box.corner is box3.corner ? Ans:',box.corner is box3.corner

