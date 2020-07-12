import define as de
import math as ma

def distanceFromCtoAB(TABLE,C):
	xa = TABLE[0][0]
	ya = TABLE[0][1]
	xb = TABLE[1][0]
	yb = TABLE[1][1]
	xc = C[0]
	yc = C[1]
	a = abs((ya-yb)*xc+(xb-xa)*yc-xa*(ya-yb)-ya*(xb-xa))/ ma.sqrt(xc*xc + yc*yc)
	# print("CH")
	# print(a)
	return abs((ya-yb)*xc+(xb-xa)*yc-xa*(ya-yb)-ya*(xb-xa))/ ma.sqrt(xc*xc + yc*yc)
def solvePointH(TABLE,C):
	xa = TABLE[0][0]
	ya = TABLE[0][1]
	xb = TABLE[1][0]
	yb = TABLE[1][1]
	xc = C[0]
	yc = C[1]
	A1 = ya-yb
	if A1 == 0:
		A1 = A1+0.001
	B1 = xb-xa
	C1 = -xa*(ya-yb)-ya*(xb-xa)
	A2 = xb-xa
	B2 = yb-ya
	C2 = -xc*(xb-xa)-yc*(yb-ya)
	mau = (B2 - B1 * A2 / A1)
	if ( B2-B1*A2/A1 ) == 0 :
		mau = 0.001

	yh = (A2*C1/A1 - C2)/mau
	xh = (-C1-yh*B1)/A1
	H = (xh, yh)
	# print(H)
	return H
def distanceAH(TABLE,H):
	xa = TABLE[0][0]
	ya = TABLE[0][1]
	xh = H[0]
	yh = H[1]
	# print("AH")
	# print( ma.sqrt((xh-xa)*(xh-xa)+(yh-ya)*(yh-ya)))
	return ma.sqrt((xh-xa)*(xh-xa)+(yh-ya)*(yh-ya))

def distanceBH(TABLE,H):
	xb = TABLE[1][0]
	yb = TABLE[1][1]
	xh = H[0]
	yh = H[1]
	# print("BH")
	# print( ma.sqrt((xh - xb)*(xh - xb) + (yh - yb)*(yh - yb)))
	return ma.sqrt((xh - xb)*(xh - xb) + (yh - yb)*(yh - yb))
def distanceAB(TABLE):
	xa = TABLE[0][0]
	ya = TABLE[0][1]
	xb = TABLE[1][0]
	yb = TABLE[1][1]
	# print("AB")
	# print( ma.sqrt((xa-xb)*(xa-xb)+(ya-yb)*(ya-yb)))
	return  ma.sqrt((xa-xb)*(xa-xb)+(ya-yb)*(ya-yb))
def checkCondition( AH, BH , AB , HC , Value):
	print("Ben")
	print(AH)
	print(BH)
	print(AB)
	print(HC)
	if (AH<AB) and (BH<AB) and (HC<= 20) :
		print("Ben")
		print(AH)
		print(BH)
		print(AB)
		print(HC)
		return True
	else :
		return False






solvePointH(de.table1, (3, 4))
distanceAH(de.table1,solvePointH( de.table1, solvePointH( de.table1,(3,4 ))))
distanceBH(de.table1,solvePointH( de.table1, solvePointH( de.table1,(3,4 ))))
distanceAB(de.table1)
distanceFromCtoAB(de.table1, (3,4))



