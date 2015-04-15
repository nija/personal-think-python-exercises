#!/usr/bin/python

from TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
bob.delay=0.01			# make the turtle draw faster
print bob

def square(t,l):		# t is turtle, l is length
	"""Given a turtle t and length l, square makes the trutle draw a square"""
	polygon(t,l,n=4)

def polygon(t,l,n):		# t is turtle, l is length, n is number of sides
	"""Given a turtle t, length l and number of sides n, polygon makes the trutle draw a polygon"""
	for i in range(n):	
		fd(t,l)		# tell the turtle to go forward by l
		lt(t,360.0/n)	# tell the turtle to turn left by 360/numberOfSides 
def circle(t,r):		# t is turtle, r is radius
	"""Given a turtle t and radius r, circle  makes the trutle draw a circle"""
	arc(t,r,360)		# a circle is a very long arc

def arc(t,r,a): 		# t is turtle, r is radius, a is angle in degrees
	"""Given a turtle t, radius r and angle in degrees a, arc makes the trutle draw an arc"""
	n=360.0
	l=(2.0*math.pi*r)/n      # l is length of each side; used formula for circumference
	if (int(a/n) >= 1):
		a=n+(a%n)
	print "arc: length of each side = ",l, "; arc length = ",a,"; modulus of arc length = ",a%n
	for i in range(a):
		fd(t,l)
		lt(t,(n/n))	# tell the turtle to turn left by 1 degree




#polygon(bob,20,19)
#circle(bob,20)
#arc(bob,50,(360*5)+90)
wait_for_user()

