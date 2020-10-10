import joblib
import numpy as np
from sklearn.linear_model import LogisticRegression
import re

def prediction_model(parm):
    model = joblib.load('./model/iris.model')
    input = np.array(parm.split(','), dtype=np.float32).reshape(1,-1)
    predict_target = model.predict(input)
    if predict_target == 0:
        return 'Setosa'
    elif predict_target == 1:
        return 'Versicolour'
    else :
        return 'Viiginica'