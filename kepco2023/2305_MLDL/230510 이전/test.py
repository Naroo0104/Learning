import numpy as np
import pandas as pd

## one hot 작성함수
def make_onehot(x):
    col = np.unique(x).size
    row = len(x) ## x.shape[0]
    onehot = np.zeros((row,col))
    for idx, val in enumerate(x):
        onehot[idx,val] = 1
    return onehot
## softmax 
def softmax(x):
    m = np.max(x)
    x -= m
    return np.exp(x)/np.sum(np.exp(x))

def sigmoid(x):
    return 1/(1+np.exp(-x))

class Leejunyoung:
    def __init__(self,x,y):
        self.x = x
        self.y_original = y
        self.y = make_onehot(y)
        self.w = np.random.randn(self.x.shape[1],self.y.shape[1])
        self.b = np.zeros(self.y.shape[1])
        
    def fit(self,epochs):
        pass
    
    def predict(self):
        y_hat = np.dot(self.x,self.w) + self.b
        self.predict = np.apply_along_axis(softmax,1,y_hat)
        return self.predict
    
    def cost(self):
        y_hat = softmax(self.predict())
        return -np.sum(self.y*np.log(y_hat))
    
