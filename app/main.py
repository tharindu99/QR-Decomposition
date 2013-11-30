from numpy import *
# generating a random overdetermined system

#,cl2,cl3,cl4,cl5
#A = random.rand(3,3)
file_com = open("combine.js","w")

A = ([ [2,-1,0 ],
	   [-1,2,-1], 
	   [0,-1,2 ]
	   ])
print A
#b = random.rand(4,1)
b=([[200],[0],[0]]) # b([[in],[0],[out]])
print
 
x_lstsq = linalg.lstsq(A,b)[0] # computing the numpy solution

Q,R = linalg.qr(A) # qr decomposition of A

Qb = dot(Q.T,b) # computing Q^T*b (project b onto the range of A)

x_qr = linalg.solve(R,Qb) # solving R*x = Q^T*b

# comparing the solutions

print 'qr solution\n'
print x_qr,"\n"

numbers = b[0]
cl1 = numbers[0]
numbers = b[2]
cl5 = numbers[0]
number1 = x_qr[0]
cl2 = int(number1[0])
number2 = x_qr[1]
cl3 = int(number2[0])
number3 = x_qr[2]
cl4 = int(number3[0])

def color_code(x):
	if x>350:
		color = 0x3333cc
	elif x>300:
		color = 0x66ffff
	elif x>250:
		color = 0x66ff00
	elif x>200:
		color = 0x99ff00
	elif x>150:
		color = 0xffcc00
	elif x>100:
		color = 0xff6600
	elif x>50:
		color = 0xff3333
	else:
		color = 0xffffff
	return color

cl11 = "var clr_1 ="+hex(color_code(cl1))+";\n"
cl21 = "var clr_2 ="+hex(color_code(cl2))+";\n"
cl31 = "var clr_3 ="+hex(color_code(cl3))+";\n"
cl41 = "var clr_4 ="+hex(color_code(cl4))+";\n"
cl51 = "var clr_5 ="+hex(color_code(cl5))+";"

file_com.write(cl11)
file_com.write(cl21)
file_com.write(cl31)
file_com.write(cl41)
file_com.write(cl51)
file.close	

print "all the measurements are equal to input measurements\n"
print "smalest sphere temperature :",cl1
print "2nd smalest sphere temperature :",number1[0]
print "3rd smalest sphere temperature :",number2[0]
print "4th smalest sphere temperature :",number3[0]
print "largest sphere temperature :",cl5


