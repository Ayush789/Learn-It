import numpy as np
from array import array
from ..preprocessing.normalise import Normaliser

def computeCost(X, y):
    """
        Computes the mean squared differnce error for gradient descenct
    """
    theta=np.zeros(x.shape[1])
    m = y.size
    J = 0
    h = X.dot(theta)
    J = 1/(2*m)*np.sum(np.square(h-y))
    return(J)

def gradientDescent(X, y, alpha=0.01, num_iters=1500):
    """
        Gradient Descent Function
        X: Train Features
        y: Train Target Values
        theta: the weight matrix that needs to be updated
        alpha: Learning rate
        num_iters: number of iterations
    """
    theta=np.zeros(x.shape[1])
    m = y.size

    for iter in np.arange(num_iters):
        h = X.dot(theta)
        theta = theta - alpha*(1/m)*(X.T.dot(h-y))
        J_history[iter] = computeCost(X, y, theta)
    return theta

def grad_desc_predict(theta,X):
    return X.dot(theta)
