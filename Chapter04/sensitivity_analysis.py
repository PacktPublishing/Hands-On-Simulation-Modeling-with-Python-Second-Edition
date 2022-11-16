import numpy as np
import math
from sensitivity import SensitivityAnalyzer

def my_func(x_1, x_2,x_3):
    return math.log(x_1/ x_2 + x_3)

x_1=np.arange(10, 100, 10)
x_2=np.arange(1, 10, 1)
x_3=np.arange(1, 10, 1)

sa_dict = {'x_1':x_1.tolist(),'x_2':x_2.tolist(),'x_3':x_3.tolist()}

sa_model = SensitivityAnalyzer(sa_dict, my_func)
plot = sa_model.plot()
styled_df = sa_model.styled_dfs()

