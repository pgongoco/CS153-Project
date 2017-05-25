def addsubtract(A, B):
	c = []
	for i in range(0, min(len(A), len(B))):
		c.append((A[i] + B[i]) % 2)

	index = i+1

	if len(A) > len(B):
		for i in range(index, len(A)):
			c.append(A[i] % 2)
	elif len(B) > len(A):
		for i in range(index, len(B)):
			c.append(B[i] % 2)

	return c

def multiply(A, B, P):
	c = {}
	for i in range(0,len(A)):
		if A[i] != 0:
			for j in range(0,len(B)):
				if B[j] != 0:
					if i+j in c:
						c[i+j] = c[i+j] + A[i]*B[j]
					else:
						c[i+j] = A[i]*B[j]
	d = []
	for i in range(0,max(c)+1):
		if i in c:
			d.append(c[i])
		else:
			d.append(0)
	d = mod2(d)

	temp,r = polydiv(d,P)

	return r

def polydiv(A, B):
	dividend = mod2(A[:])
	divisor = mod2(B[:])
	degA = len(dividend)-1
	degB = len(divisor)-1
	if degA < degB:
		return [],dividend

	quo = {}
	while degA >= degB:
		if dividend[degA] != 0:
			quo[degA-degB] = 1
			temp = [0]*(degA-degB) + divisor
			dividend = addsubtract(dividend, temp)
		else:
			del dividend[degA]
			degA = len(dividend)-1

	q = []
	for i in range(0, max(quo)+1):
		if i in quo:
			q.append(1)
		else:
			q.append(0)

	return q,dividend
		


def mod2(A):
	for i in range(0, len(A)):
		A[i] = A[i] % 2
	return A

def toint(A):
	for i in range(0, len(A)):
		A[i] = int(A[i])
	return A

def tostring(A):
	for i in range(0, len(A)):
		A[i] = str(A[i])
	return A

loop = 0

while loop != 1:
	print "-------------------------"
	print "Galois Field Calculator"
	print "-------------------------"
	Ax = raw_input("Input A(x): ")
	Bx = raw_input("Input B(x): ")
	Px = raw_input("Input P(x): ")

	Ax = Ax.split(" ")
	Bx = Bx.split(" ")
	Px = Px.split(" ")
	Ax.reverse()
	Bx.reverse()
	Px.reverse()
	Ax = toint(Ax)
	Bx = toint(Bx)
	Px = toint(Px)

	print ""
	print "Choose which operation to perfom: (input the number)"
	print "(1) A(x) + B(x)"
	print "(2) A(x) - B(x)"
	print "(3) A(x) * B(x)"
	print "(4) A(x) / B(x)"
	op = input("Operation: ")
	print ""

	if op == 1:
		Cx = addsubtract(Ax,Bx)
	elif op == 2:
		Cx = addsubtract(Ax,Bx)
	elif op == 3:
		Cx = multiply(Ax,Bx,Px)
	elif op == 4:
		Cx,rem = polydiv(Ax,Bx)
	else:
		print "No operation."
		quit()

	Ax.reverse()
	Bx.reverse()
	Cx.reverse()
	Ax = " ".join(tostring(Ax))
	Bx = " ".join(tostring(Bx))
	Cx = " ".join(tostring(Cx))


	print "----------"
	print "1. A(x) =",Ax
	print "2. B(x) =",Bx
	print "3. Result:",Cx
	if op == 4:
		rem.reverse()
		rem = " ".join(tostring(rem))
		print "4. Remainder:",rem
	print ""

	loop = input("Do you want to exit? 1-yes, 2-no: ")
	print ""