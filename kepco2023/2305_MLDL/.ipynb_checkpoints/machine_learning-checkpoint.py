import numpy as np

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
    return x/(1+np.exp(-x))



class Leejunyoung:
    def __init__(self,x,y):
        self.x = x
        self.y_original = y
        self.y = make_onehot(y)
        # self.w = np.random.randn(self.x.shape[1],self.y.shape[1])
        self.w=np.random.uniform(0,1,size=(self.x.shape[1], self.y.shape[1]))
        self.b = np.zeros(self.y.shape[1])
        
    def fit(self,epochs,lr):
        for epoch in range(epochs):
            self.w -= self.diff()[0]*lr
            self.b -= self.diff()[1]*lr
            if epoch % 100 == 0:
                print(f'Loss : ==================> {self.cost()}')
    
    def predict(self):
        self.y_hat = np.dot(self.x,self.w) + self.b
        self.y_hat = np.apply_along_axis(softmax,1,self.y_hat)
        return self.y_hat
    
    def cost(self):
        self.predict()
        epsilon = 1e-7
        return -np.sum(self.y*np.log(self.y_hat+epsilon))
    
    def diff(self):
        h = 1e-4
        self.grad_a = np.zeros_like(self.w)
        for i in range(self.w.shape[0]):
            for j in range(self.w.shape[1]):
                tmp = self.w[i,j]
                fx = self.cost()
                self.w[i,j] += h
                fxh = self.cost()
                self.grad_a[i,j] = (fxh-fx)/h
                self.w[i,j] = tmp
        self.grad_b = np.zeros_like(self.b)
        for i in range(self.b.shape[0]):
            tmp = self.b[i]
            fx = self.cost()
            self.b[i] += h
            fxh = self.cost()
            self.grad_b[i] = (fxh-fx)/h
            self.b[i] = tmp
        return self.grad_a, self.grad_b
    
    def score(self,x,y):
        predict = np.argmax(softmax(np.dot(x,self.w)+self.b),1)
        score = np.sum(predict == y)/len(x)
        return score 
                