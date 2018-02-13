import numpy as np
import pandas as pd
class Normaliser:
    #contructor for
    #def __init__(self):
    def normalise(self,data,type='std'):
        if not isinstance(data, np.ndarray):
            raise ValueError('Input Value not of type Pandas.DataFrame')
        if(type == 'std'):
            data = (data - data.mean())/data.std()
        elif(type=='mean'):
            data = (data - data.min())/(data.max()-data.min())
        else:
            raise ValueError('Inavlid type')
        return data
