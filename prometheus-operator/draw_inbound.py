import os
import numpy as np
import matplotlib.pyplot as plt 
from collections import Counter

def read(file):
    with open(file, 'r') as f:
        return f.read().strip().split('\n')

dir = "/home/pranjal/Documents/no-throttle/3000"
reports = os.listdir(dir)

x = []
y = []

for file in reports:
    logs = list(map(lambda x: x.split('\t'), read(os.path.join(dir, file))))
    if "throttle" in file:
        x.append(file.strip('.log').split('_')[-1])
    else:
        x.append("no-throttle")

    total_log_loss = 0
    for i in range(1, len(logs)):
        total_log_loss += int(logs[i][2]) - int(logs[i][3])

    time = int(logs[-1][1]) - int(logs[0][1])
    y.append(total_log_loss/time)

fig = plt.figure()
ax = fig.add_axes([0,0,0.5,0.5])
print (x, y)
ax.bar(x,y)
plt.show()