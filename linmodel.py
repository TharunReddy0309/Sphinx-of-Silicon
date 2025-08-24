import joblib
import numpy as np
model=joblib.load("linearmodel.joblib")
def p(a,b):
    k=model.predict([[a,b]])
    return k[0]