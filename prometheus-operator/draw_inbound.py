import matplotlib.pyplot as plt 

def read(file):
    with open(file, 'r') as f:
        return f.read().strip().split('\n')

file = "./without throttle/heavy_loss_inbound.log"
# file = "./without throttle/simple_inbound.log"
group_key = "heavy"
step = 2 if group_key == "heavy" else 8 
# step = 1

logs = read(file)
logs = list(filter(lambda x: group_key in x, logs))
logs = list(map(lambda x: x.split(), logs))

x = []
y = []

for i in range(step, len(logs), step):
    x.append(int(logs[i][1]) - int(logs[0][1])) # time
    y.append(sum([int(logs[j][2]) - int(logs[j][3]) for j in range(i, i + step)]))


plt.plot(x, y)
plt.title("Log Loss - \"{}\" Group - Avg Loss - {}".format(group_key, sum(y)/x[-1] ))
plt.xlabel("Time in sec")
plt.ylabel("Log loss")
plt.show()