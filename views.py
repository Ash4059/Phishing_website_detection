from django.shortcuts import render
from django.http import HttpResponse
from . import feature_extraction
import joblib
import numpy as np
# Create your views here.
url=""
model_reload=joblib.load('./model/Phishing_website_detection.pkl')
def index(request):
    return render(request,'index.html')
def detectWebsite(request):
    if(request.method=="POST"):
        url=request.POST.get('url')
    X_new=feature_extraction.generate_data_set(url)
    print(X_new)
    X_new = np.array(X_new).reshape(1,-1)
    try:
        prediction = model_reload.predict(X_new)
        if prediction == -1:
            result = "this is a Phishing Url"
        else:
            result = "this is Legitimate Url"
    except:
        result = "this is Phishing Url"
    return render(request,'result.html',{'result':result})
            
        
