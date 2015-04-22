def right_justify(mystr):
	mystrlen=len(mystr)
	spacer=' '*(70-mystrlen)
	print spacer + mystr

right_justify('spam')
