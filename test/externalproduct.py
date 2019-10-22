from pyFHE.trlwe import trlweSymEncrypt,trlweSymDecrypt
from pyFHE.trgsw import trgswSymEncrypt,trgswExternalProduct
from pyFHE.key import SecretKey
from pyFHE.mulfft import PolyMul
from pyFHE.utils import dtot32
import numpy as np

np.set_printoptions(threshold=2000)
for i in range(100):
    sk = SecretKey(500,2**(-7),1024,2,10,3.73e-9,8,2,2.43e-5)
    x = trlweSymEncrypt(np.full(sk.params.N,2**-3),sk.params.alpha,sk.key.trlwe,sk.params.twist)
    A = trgswSymEncrypt(np.append([1],np.zeros(sk.params.N - 1)),sk.params.bkalpha,sk.params.h,sk.key.trlwe,sk.params.twist)
    y = trgswExternalProduct(A,x,sk.params)
    if np.sum(trlweSymDecrypt(y,sk.key.trlwe,sk.params.twist)) != len(y[0]):
        print(trlweSymDecrypt(y,sk.key.trlwe,sk.params.twist))
        print(np.uint32(y))
        print(i)
        break