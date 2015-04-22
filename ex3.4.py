

#def do_twice(f):
#	f()
#	f()

def do_twice(f, o):
	f(o)
	f(o)

def print_spam():
	print 'spam'

def print_twice(o):
	print o
	print o


def do_four(f, o):
	do_twice(f,o)
	do_twice(f,o)


#print_twice('spam')
#do_twice(print_twice, 'spammy')
do_four(print_twice,'bacon')
