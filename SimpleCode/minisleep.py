import time
"""
i = 0
while i < 30:
    print(i)
    i += 1
    time.sleep(10/(i+1))
"""
"""
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a ** b)  # Output: [5 7 9]
"""
"""
import pandas as pd
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
print(df)
"""
"""
import random
import matplotlib.pyplot as plt
a = []
b = []
for i in range(100):
    a.append(random.randint(-500,500))
    b.append(random.randint(-500,500))
plt.plot(a, b)
plt.title('Simple Plot')
plt.show()
"""
"""
from sklearn.linear_model import LinearRegression
reg = LinearRegression().fit([[0], [1], [4]], [0, 1, 2])
print(reg.predict([[3]]))  # Output: [3.]
"""

import torch
x = torch.tensor([1.0, 2.0, 3.0])
print(x * 2)  # Output: tensor([2., 4., 6.])
