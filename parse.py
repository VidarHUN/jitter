import sys
import matplotlib.pyplot as plt

# Calculate average of a list
def avg(l):
    sum = 0
    for i in range(len(l)):
        sum += l[i]
    return sum / len(l)

TICK = 1 / 8000 # Tick time 
base_ts = 0 # First Timestamp
data = []

# Reading data from csv file
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

delta_forward = []
delta_reverse = []

forward = data[0][0]
reverse = data[1][0]

for i in range(2, len(data) - 1):
    if data[i][1] == sys.argv[2]:
        # delta_forward.append(data[i][0] - forward) # Calculation of forward delta
        delta_forward.append(abs(((data[i][3] - base_ts) * TICK) - data[i][0]) * 1000)
        forward = data[i][0]
    if data[i][1] == sys.argv[3]:
        # delta_reverse.append(data[i][0] - reverse) # Calculation of reverse delta
        delta_reverse.append(abs(((data[i][3] - base_ts) * TICK) - data[i][0]) * 1000)
        reverse = data[i][0]
        
# print(*plot_data,sep='\n')
# plt.plot(delta_forward, 'r', delta_reverse, 'g')

# Plot settings
plt.plot(delta_forward, label='Forward')  # Set the forward stream data
plt.plot(delta_reverse, label='Reverse')  # Set the reverse stream data
plt.xlabel('Packets')
plt.ylabel('Jitter (ms)')
plt.title("Jitter")
plt.legend()

# I don’t use it because I think it calculates an average of those values 
# for every second. But I left it here to see if it would come in handy.
# plt.xlim(0, data[-1][0]) # Change X axes range to 0 - last packet arrival time

# print(*delta_forward, sep='\n')

plt.show()
