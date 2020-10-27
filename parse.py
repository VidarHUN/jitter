import sys
import matplotlib.pyplot as plt

def mean(l):
    sum = 0
    for i in range(len(l)):
        sum += l[i]
    return sum / len(l)

TICK = 1 / 8000
base_ts = 0
data = []

with open(str(sys.argv[1]), 'r') as f: 
    line = f.readline()
    line = f.readline()
    new_line = line.strip().split(',')
    data.append([
        float(new_line[1].strip('"')), 
        new_line[2].strip('"'), 
        new_line[3].strip('"'), 
        int(new_line[-2].strip('"')), 
        int(new_line[-1].strip('"'))
        ])
    base_ts = data[0][3]
    while True:
        line = f.readline()
        if not line:
            break
        new_line = line.strip().split(',')
        data.append([
            float(new_line[1].strip('"')), 
            new_line[2].strip('"'), 
            new_line[3].strip('"'), 
            int(new_line[-2].strip('"')), 
            int(new_line[-1].strip('"'))
            ])

plot_data = []
delta_forward = []
delta_reverse = []

forward = data[0][0]
reverse = data[1][0]

for i in range(2, len(data) - 1):
    if data[i][1] == '10.2.0.17':
        # delta_forward.append(data[i][0] - forward)
        delta_forward.append(abs(((data[i][3] - base_ts) * TICK) - data[i][0]) * 1000)
        forward = data[i][0]
    if data[i][1] == '10.2.0.11':
        # delta_reverse.append(data[i][0] - reverse)
        delta_reverse.append(abs(((data[i][3] - base_ts) * TICK) - data[i][0]) * 1000)
        reverse = data[i][0]
    if data[i][4] == data[i+1][4]:
        plot_data.append(data[i+1][0] - data[i][0])
        jump = data[i+1][4]
        
# print(*plot_data,sep='\n')
# plt.plot(delta_forward, 'r', delta_reverse, 'g')

plt.plot(delta_forward, label='Forward')  # etc.
plt.plot(delta_reverse, label='Reverse')
plt.xlabel('Packets')
plt.ylabel('Jitter (ms)')
plt.title("Jitter")
plt.legend()
# plt.xlim(0, data[-1][0])

# print(*delta_forward, sep='\n')

# print(mean(delta_forward))
# print(mean(delta_reverse))

plt.show()
