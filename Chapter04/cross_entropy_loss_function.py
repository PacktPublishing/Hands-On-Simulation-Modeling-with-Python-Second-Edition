import numpy as np
 
y = np.array([1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0])
p = np.array([0.8, 0.1, 0.9, 0.2, 0.8, 0.1, 0.7, 0.3, 0.6, 0.4])

ce_loss = -sum(y*np.log(p)+(1-y)*np.log(1-p))

ce_loss = ce_loss/len(p) 
print(f'Cross Entropy Loss =  {ce_loss:.3f} nats')