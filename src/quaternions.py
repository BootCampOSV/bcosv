import numpy as np
import pdb
import copy

class DualNumber(object):
    """ Class which implements dual numbers

        x = r + e d with e**2 = 0 

        x1 + x2 = r1 + r2 + e ( d1 + d2) 
        x1 - x2 = r1 - r2 + e ( d1 - d2) 
        x1 * x2 = (r1 * r2) + e ( r1 * d2 + d1 * r2 )
        conj(x) = r - e d
        1/x = 1/r  - e d/r**2 

    """
    def __init__(self,r,d):
        """
        r : real part 
        e : dual part 

        """
        self.r = r
        self.d = d
        self.shape = np.shape(self.r)

    def __repr__(self):    
        st=''
        st+=str(self.r)+' + '
        st+=str(self.d)+' e'
        return(st)

    def __neg__(self):    
        return DualNumber(-self.r,-self.d)

    def __add__(self,other):
        return DualNumber(self.r+other.r,self.d+other.d)
        
    def __sub__(self,other):
        return DualNumber(self.r-other.r,self.d-other.d)
        
    def __mul__(self,other):
        c=self.r*other.r
        d=self.r*other.d+self.d*other.r
        return DualNumber(c,d)

    def __div__(self,other):
        #return(DualNumber(1.0*self.n/other.n,(self.d*other.n-self.n*other.d)/(1.0*other.n**2)))
        return(self*other.inv())

    def __getitem__(self,key):
        return DualNumber(self.r[key],self.d[key])
    
    def __setitem__(self,key,val):
        self.r[key] = val.r[key] 
        self.d[key] = val.d[key] 
    

    def sqrt(self):
        return(DualNumber(np.sqrt(self.r),self.d/(2*np.sqrt(self.r))))

    def inv(self):
        assert(self.r!=0), "pure dual numbers have no inverse"
        return(DualNumber(1./self.r,-1.0*self.d/(self.r**2)))

class Quaternion(object):
    
    def __init__(self,a=1,b=0):
        """
        a : np.array (Nx4) dtype=complex
        b : np.array (Nx4) dtype=complex
        """
        if type(a)!=np.ndarray:
            self.a=np.array([a])[:,None].astype(complex)
            self.b=np.array([b])[:,None].astype(complex)
        else:
            if len(a.shape)==2:
                self.a=a.astype(complex)
                self.b=b.astype(complex)
            else:
                self.a = a[:,None].astype(complex)
                self.b = b[:,None].astype(complex)

        assert(self.a.shape==self.b.shape)
        self.shape = np.shape(self.a)

        
    def __repr__(self):
        st = ''
        st += str(self.a.real)+' + '
        st += str(self.a.imag)+'i + '
        st += str(self.b.real)+'j + '
        st += str(self.b.imag)+'k'
        return st
        
    def __neg__(self):
        return Quaternion(-self.a,-self.b)
        
    def __add__(self,other):
        return Quaternion(self.a+other.a,self.b+other.b)
        
    def __sub__(self,other):
        return Quaternion(self.a-other.a,self.b-other.b)
        
    def __mul__(self,other):
        c = self.a*other.a-self.b*other.b.conjugate()
        d = self.a*other.b+self.b*other.a.conjugate()
        return Quaternion(c,d)
        
    def __rmul__(self,k):
        return Quaternion(self.a*k,self.b*k)
        
    def __abs__(self):
        return np.hypot(abs(self.a),abs(self.b))

    def __getitem__(self,key):
        return Quaternion(self.a[key],self.b[key])
    
    def __setitem__(self,key,val):
        self.a[key] = copy.copy(val.a)
        self.b[key] = copy.copy(val.b)

    def normalize(self):
        return (1/abs(self))*self
                
    def conjugate(self):
        return Quaternion(self.a.conjugate(),-self.b)

    def polar(self):
        mq = abs(self)
        qu = (1./mq)*self
        return(mq,qu)

    def scal(self):
        return self.a.real

    def vect(self):
        v = np.hstack((self.a.imag,self.b.real,self.b.imag))
        return(v)

    def from_mat(self,M):
        tr = np.trace(M)
        if (tr > 0): 
            S = np.sqrt(tr+1.0)*2 
            self.a = 0.25 * S +1j* (M[2,1] - M[1,2])/ S
            self.b = (M[0,2]-M[2,0]/S)+1j*(M[1,0]-M[0,1])/S
        elif ((M[0,0] > M[1,1])&(M[0,0]>M[2,2])):
            S = np.sqrt(1.0 + M[0,0] - M[1,1] - M[2,2])* 2
            self.a = (M[2,1] - M[1,2])/S +1j*0.25*S
            self.b = M[0,1] + M[1,0])/S + 1j*(M[0,2] + M[2,0])/S 
        elif (M[1,1] > M[2,2]):  
            S = np.sqrt(1.0 + M[1,1] - M[0,0]  - M[2,2]* 2
            self.a = (M[0,2]  - M[2,0])/S+1j*(M[0,1]+M[1,0])/S
            self.b = 0.25*S+1j* (M[1,2]  + M[2,1]) / S 
        else: 
            S = np.sqrt(1.0 + M[2,2]  - M[0,0]  - M[1,1]*2
            self.a = (M[1,0] - M[0,1])/S +1j* (M[0,2]  + M[2,0])/S
            self.b = (M[1,2] + M[2,1])/S +1j* 0.25 * S

    def __div__(self,other):
        u  = 1./abs(other)**2
        qu = Quaternion(u+0j,np.zeros(u.shape)+0j)
        qv  = qu*other.conjugate()
        return self*qv

    def log(self):
        q = abs(self)
        v = self.vect()
        if len(v.shape)>1:
            vn = v/np.sqrt(np.sum(v*v,axis=1))
            v2 = np.arccos(self.a.real/q)*vn
            a = np.log(q) + 1j*v2[:,0]
            b = v2[:,1]+1j*v2[:,2]  
        else:
            vn = v/np.sqrt(np.sum(v*v))
            v2 = np.arccos(self.a.real/q)*vn
            a = np.log(q) + 1j*v2[0]
            b = v2[1]+1j*v2[2]
        return(Quaternion(a,b))

    def exp(self):
        """ exponential of a quaternion 
        """
        
        ea = np.exp(self.a.real)
        v = self.vect()
        if len(v.shape)>1:
            theta = np.sqrt(np.sum(v*v,axis=1))
            vn = v/theta
            a = np.cos(theta)+1j*np.sin(theta)*vn[:,0]
            b = np.sin(theta)*(vn[:,1]+1j*vn[:,2])
        else:
            theta = np.sqrt(np.sum(v*v))
            vn = v/theta
            a = np.cos(theta)+1j*np.sin(theta)*vn[0]
            b = np.sin(theta)*(vn[1]+1j*vn[2])
            
        ev = Quaternion(a,b)
        return(ea*ev)

    def __pow__(self,n):
        r=1
        for i in range(n):
            r=r*self
        return r

class DualQuaternion(object):
    """

    For more details about Dual quaternions see the following ref

    www.euclideanspace.com/maths/algebra/realNormedAlgebra/other/dualQuaternion
    https://en.wikipedia.org/wiki/Dual_quaternion

    Real Time skeletal Animation (Ladislav Kavan) 2007
    https://www.cs.utah.edu/~ladislav/thesis/LKthesisHiresPrint.pdf

    """

    def __init__(self,qr,qd):
        """
        Parameters
        ----------

        qr : Quaternion 
            real part 
        qd : Quaternion
            dual part 

        """
        #assert(qr.shape==qd.shape), "%r , %r   " % (qr.shape,qd.shape)
        assert  (qr.shape==qd.shape), pdb.set_trace()
        self.qr = qr
        self.qd = qd
        self.shape = self.qr.shape

    def __repr__(self):    
        st=''
        st+=str(self.qr.scal())+'+'
        if len(self.qr.vect().shape)>1:
            st +=str(self.qr.vect()[:,0])+' i +'
            st +=str(self.qr.vect()[:,1])+' j +'
            st +=str(self.qr.vect()[:,2])+' k +'
            st +=str(self.qd.scal())+' e +'
            st +=str(self.qd.vect()[:,0])+' ei+'
            st +=str(self.qd.vect()[:,1])+' ej+'
            st +=str(self.qd.vect()[:,2])+' ek'
        else:
            st +=str(self.qr.vect()[0])+' i +'
            st +=str(self.qr.vect()[1])+' j +'
            st +=str(self.qr.vect()[2])+' k +'
            st +=str(self.qd.scal())+' e +'
            st +=str(self.qd.vect()[0])+' ei+'
            st +=str(self.qd.vect()[1])+' ej+'
            st +=str(self.qd.vect()[2])+' ek'

        return (st)

    def __neg__(self):  
        return DualQuaternion(-self.qr,-self.qd)

    def __add__(self,other):
        return DualQuaternion(self.qr+other.qr,self.qd+other.qd)

    def __sub__(self,other):
        return DualQuaternion(self.qr-other.qr,self.qd-other.qd)

    def __rmul__(self,s):
        return DualQuaternion(s*self.qr,s*self.qd)

    def __mul__(self,other):
        c = self.qr*other.qr
        d = self.qr*other.qd + self.qd*other.qr
        return DualQuaternion(c,d)

    def __getitem__(self,key):
        return DualQuaternion(self.qr[key],self.qd[key])
    
    def __setitem__(self,key,val):
        self.qr[key] = val.qr
        self.qd[key] = val.qd

    def conj1(self):
        """
            Quaternion conjugaison 

            (Q1 Q2)* = Q2*Q1*

        """
        return DualQuaternion(self.qr.conjugate(),self.qd.conjugate())

    def conj2(self):
        """
            Dual conjugaison 
        """
        return DualQuaternion(self.qr,-self.qd)

    def conj3(self):
        """ 
            Quaternion Dual conjugaison 
            ( conjugaison used for chaining displacement ) 
            
            dis * dqp * dis.conj3

        """
        return DualQuaternion(self.qr.conjugate(),-self.qd.conjugate())

    def abs(self):
        dq = self*self.conjugate()
        assert(np.allclose(dq.qr.vect(),0))
        assert(np.allclose(dq.qd.vect(),0))
        magnitude2 = DualNumber(dq.qr.scal(),dq.qd.scal())
        magnitude = magnitude2.sqrt()
        return(magnitude)

class QPoint(Quaternion):
    """ Quaternion point
    
    The scalar part is 0 

    """
    def __init__(self,pt):
        if len(pt.shape)==2:
            Quaternion.__init__(self,1j*pt[:,0][:,None],pt[:,1][:,None]+1j*pt[:,2][:,None])
        else:
            Quaternion.__init__(self,1j*np.array([pt[0]])[:,None]
                                       ,np.array([pt[1]])[:,None]
                                    +1j*np.array([pt[2]])[:,None])

class DQPoint(DualQuaternion):
    """ Dual quaternion point 

    The real part is unitary purely scalar quaternion 
    The dual part is a QPoint 

    """
    def __init__(self,pt):
        if len(pt.shape)>1:
            N = pt.shape[0]
        else:
            N = 1
        DualQuaternion.__init__(self,Quaternion(np.ones((N,1)),np.zeros((N,1))),QPoint(pt))

class Displacement(DualQuaternion):
    """ Class implementing a displacement 

    A displacement is a DualQuaternion built from a rotation and a translation

    """

    def __init__(self,qr=Quaternion(1+0j,0+0j),qt=Quaternion(0j,0+0j)):
        """ 

        qr : unitary quaternion
        qt : pure vector 

        """
        assert(np.allclose(abs(qr),1))
        assert(np.allclose(qt.scal(),0))
        DualQuaternion.__init__(self,qr,0.5*qr*qt)
        
    def setdis(self,v):
        self.qd = 0.5*QPoint(v)

    def setrotation(self,qr):
        self.qr = qr
