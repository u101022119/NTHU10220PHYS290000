class Point(object):
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

class Rectangle(object):
	def __init__(self, width, height, corner):
		self.width = width
		self.height = height
		self.corner = corner

def distance_between_points(a,b):
	dx = a.x - b.x
	dy = a.y - b.y
	return (dx**2 + dy**2)**0.5

def move_rectangle(rec,dx,dy):
	rec.corner.x += dx
	rec.corner.y += dy

def move_rectangle_version2(rec,dx,dy):
	return Rectangle(rec.width, rec.height, rec.corner.x+dx, rec.corner.y+dy)

