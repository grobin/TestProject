a = [1,2,3,4]
b = 5
c = a[::-1]
e = "your second favourite number is %d"

a.append(b)
print a 
#print a[-1]
print c

#for x in range(20):
#	print x

for x in a:
	print x

def d(b):
	print "your favourite number is %d" % b

d(b)
d(1+2+3+5)
d(3)
d(b+4)
print e % b

age = raw_input("how old are you?")
height = raw_input("how tall are you?")
print "so you're %r years old and %r feet tall" % (age, height)
print "%r" % age
