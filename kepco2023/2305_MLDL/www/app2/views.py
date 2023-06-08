from django.shortcuts import render
import numpy as np

# Create your views here.
coef=np.load('app/coef.npy')
intercept=np.load('app/intercept.npy')

def predict(x1, x2, x3, x4):
    x=np.c_[x1, x2, x3, x4]
    result=np.argmax(np.dot(x, coef) + intercept)
    return result
    
    # rng = np.random.RandomState(10)
    # x=rng.randn(1, 4)
    # result=np.argmax(np.dot(x, coef) + intercept)


def iris_predict(request):
    if request.GET.get('a') != None:
        x1= request.GET.get('a')
        x2= request.GET.get('b')
        x3= request.GET.get('c')
        x4= request.GET.get('d')
        
        x1= float(x1)
        x2= float(x2)
        x3= float(x3)
        x4= float(x4)
        
        result = predict(x1, x2, x3, x4)
        contents={'result':result}
    else:
        contents={'result':'예측버튼을 눌러주세요.'}
    return render(request, 'app2/predict_iris.html', contents)