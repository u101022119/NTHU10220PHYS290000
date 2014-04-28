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
