from django.shortcuts import render
import pickle
import numpy as np

with open('C:/www/app/model.pickle2', 'rb') as f:
    model=pickle.load(f)


species={
    0:'setosa',
    1:'versicolor',
    2:'verginica'
}

def predict(request):
    if request.POST.get('sepal_length') == None:
        contents={'result': '예측버튼을 클릭하세요.'}
    else:
        sepal_length=request.POST.get("sepal_length")
        sepal_width=request.POST.get("sepal_width")
        petal_length=request.POST.get("petal_length")
        petal_width=request.POST.get("petal_width")
        
        sepal_length=float(sepal_length)
        sepal_width=float(sepal_width)
        petal_length=float(petal_length)
        petal_width=float(petal_width)
        
        x=np.c_[sepal_length, sepal_width, petal_length, petal_width]
        result=species.get(model.predict(x)[0])
        prob=np.max(model.predict_proba(x))
        prob=np.around(prob,2)*100
        prob=str(prob)+'%'
        
        contents={
            'result':result,
            'prob':prob,
        }
    
    return render(request, 'app/predict.html', contents)
