from numpy import *
from numpy.matlib import repmat
from numpy.linalg import inv, pinv


"""""
Regularized Linear Kramers Kronig

(c) Mess- und Sensortechnik, TU Chemnitz
Author: Ahmed Yahia Kallel

Kallel, Ahmed Yahia, and Olfa Kanoun. "Regularized linear kramers-kronig transform for consistency check of noisy impedance spectra with logarithmic frequency distribution." 2021 International Workshop on Impedance Spectroscopy (IWIS). IEEE, 2021.

"""""

def rLKK(Z, f ,lambd=1e-4,fx=logspace(-8,8,160)):
    """
    rLKK function, constructs ideal impedance spectrum from measurement data
    Zf = rLKK(Z, f):
    
    
    :param Z: complex-valued impedance spectrum contain (Array N-values)
    :type Z: array[complex]
    :param f: frequency vector containing N values (Array N-values)
    :type f: array[double]
    
    
    :param lambd: (Optional) lambd=1e-4: regularization parameter, can be a scalar (regularization value) or a vector (weight vector)
    :type lambd: double or array[double]
    :param fx: (Optional) fx=logspace(-8,8,160): DRT Frequency vector M values
    :type fx: array[double]
    
    :return:  Zf: reconstructed impedance spectrum (N values)
    :rtype: array[double]
    
    

    """
    
    # %% weight vectors
    if isinstance(lambd, float): lambd*=ones_like(Z.real)
    if isinstance(lambd, int): lambd*=ones_like(Z.real)
    if len(lambd) == 1: lambd*=ones_like(Z.real)
    lambd = lambd.reshape(-1)
    
    
    
    #%%  DRT Frequency vector
    #fx = logspace(-8,8,160); 
    
    
    #%% DRT function
    def Z_ww0(R,w,w0) : 
        return R/(1j*repmat(w[:], len(w0), 1).T / repmat(w0[:], len(w), 1) + 1)
    
    #%% Construct A matrix (4MxN) as in Ax = b
    A = Z_ww0(1,f,fx);
    A = vstack([A.real, A.imag]);
    
    
    dA = zeros(A.shape);
    dA[0:A.shape[0]//2,0:A.shape[0]//2] = diag(lambd)[0:A.shape[0]//2,0:A.shape[1]]
    dA[A.shape[0]//2:A.shape[0],0:A.shape[0]//2] = diag(lambd)[0:A.shape[0]//2,0:A.shape[1]]
    A = vstack((A,dA))
    
    #%% Construct vector b 4Mx1
    b = hstack((Z.real,Z.imag,reshape(zeros((Z.shape[0]*2,1)),-1))).T
    
    #%% as it'll be ill-posed, we will be using pseudo-inverse instead of 
    x = pinv(A) @ b
    
    #%% get the results, remove 2M, get real and imaginary and return complex vector
    bb = A@x;
    bb = bb[0:len(bb)//2];
    bb = bb[0:len(bb)//2] + 1j*bb[len(bb)//2:];
    
    
    
    return bb;