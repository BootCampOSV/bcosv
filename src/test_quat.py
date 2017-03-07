import numpy as np 
from quaternions import * 
import imusim.maths.quaternions as q

N = 2
np.random.seed(1)
a = np.random.rand(N,1)+1j*np.random.rand(N,1)
b = np.random.rand(N,1)+1j*np.random.rand(N,1)
c = np.random.rand(N,1)+1j*np.random.rand(N,1)
d = np.random.rand(N,1)+1j*np.random.rand(N,1)
q1 = Quaternion(a,b)
q2 = Quaternion(c,d)
dq = DualQuaternion(q1,q2)
v1 = q1.vect()
s1 = q1.scal()
dq = DualQuaternion(q1,q2)
u = abs(q1/q1.conjugate())
v = abs(q2/q2.conjugate())
assert np.allclose(u,1)
assert np.allclose(v,1)

d1 =  DualNumber(1,2)
d2 =  DualNumber(2,3)

q3 = q.Quaternion(1,2,3,4)
q4 = q3.exp()
lq3 = q3.log()
lq4 = q4.log()
q3b = Quaternion(1+2*1j,3+4*1j)

u1 = Quaternion(1+2j,3+4j)
u2 = Quaternion(3j,4+5j)
u3 = Quaternion(2j,1+3j)
pdb.set_trace()
dq1 = DualQuaternion(u1,u2)
dq2 = DualQuaternion(u1,u3)
i = Quaternion(0+1j,0+0j)
j = Quaternion(0+0j,1+0j)
k = i*j


# 
di = Displacement()


qA = Quaternion(0,1j)
qB = Quaternion(0,-1j)
qr = Quaternion(np.cos(np.pi/4)+1j*np.sin(np.pi/4),0)
qt = Quaternion(0,6)


qAp = qr*qA*qr.conjugate()+qt
qBp = qr*qB*qr.conjugate()+qt

qApp = qr*qr*qA*qr.conjugate()*qr.conjugate()
qBpp = qr*qr*qB*qr.conjugate()*qr.conjugate()

qtA = qr*qt*qr.conjugate()+qt

qfA = qApp+qtA
qfB = qBpp+qtA



# from www.euclideanspace.com 
p1 = np.array([3,4,5])
v  = np.array([4,2,6])
qr = Quaternion(0+1j,0)
qp1 = QPoint(p1)
dqp1 = DQPoint(p1)
dis = Displacement()
dis.setdis(v)
rot = Displacement()
rot.setrotation(qr)
Q = rot*dis
p1d = dis*dqp1*dis.conj3()
p2d = Q*dqp1*Q.conj3()

dis2 = Displacement(qr=qr,qt=Quaternion(4*1j,2+6*1j))
th = 1.6
u = np.random.rand(3)
un = u/np.sqrt(np.sum(u*u))
qr3 = Quaternion(np.cos(th/2.)+1j*np.sin(th/2.)*un[0],np.sin(th/2.)*un[1]+1j*np.sin(th/2.)*un[2])


# __setitem__

v1 = np.random.rand(10)+1j*np.random.rand(10)
v2 = np.random.rand(10)+1j*np.random.rand(10)
qz = Quaternion(v1,v2)
qz[2:4] = q1
qz[3:5] = q2

