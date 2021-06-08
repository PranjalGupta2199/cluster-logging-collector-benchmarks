import matplotlib.pyplot as plt 
time_interval = 10

vals = []

x = []
y = []
i = 0

for idx in range(1, len(vals) - 1):
    x.append(i) 
    i += time_interval
    y.append(vals[idx + 1] - vals[idx])

print(y)
plt.plot(x, y)
plt.xlabel("Time (sec)")
plt.ylabel("Outbound log loss")
plt.show()