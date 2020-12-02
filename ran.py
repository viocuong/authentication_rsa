
import tinyec.ec as ec

# p la truong cua E
# g la diem sinh

# n la bac cua E
field = ec.SubGroup(p=0x05177b8a2a0fd6a4ff55cda06b0924e125f86cad9b, g=(0x0017e7012277e1b4e43f7bf74657e8be08baca175b, 0x00aa03a0a82690704697e8c504cb135b2b6eef3c83), n=0x03177f8a2a0fd674ff556aa7b8a7851f88bd53b2c1, h=1)
curve = ec.Curve(a = 0x043182d283fce3880730c9a2fdd3f6016529a166af, b=0x020c61e9459e53d8871bcaadc2dfc8ad5225228035, field=field, name='p1707')
print('curve:', curve)
#k = 0xa78a2374871236e
k = 0x03177b8a2a0fd674ff556aa7b8a7851f88bd53b2c1
P = curve.g
p = curve.field.p
n = 10
for i in range(1, n+1):
	S = k * P
	xn = S.x
	
	if(xn == None):
		yn1 = S1.y
		k = yn1  + (i-1)%p
		S = k * P
		xn = S.xp
	#print(xn)
	if(i==n):
		break
	else:
		k = xn + i%p
	S1 = S

#print(hex(xn))