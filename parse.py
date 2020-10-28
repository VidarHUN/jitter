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
fig, ax = plt.subplots(2, 1)
ax[1].plot(delta_forward, label='Forward')
ax[1].plot(delta_reverse, label='Reverse')
ax[1].set_xlabel('Packets')
ax[1].set_ylabel('Jitter (ms)')
ax[1].set_title('Jitter')
ax[1].legend()

# I don’t use it because I think it calculates an average of those values 
# for every second. But I left it here to see if it would come in handy.
# plt.xlim(0, data[-1][0]) # Change X axes range to 0 - last packet arrival time

# print(*delta_forward, sep='\n')

textstr = '\n'.join((
   'Average of Forward: {:.4f} ms'.format(avg(delta_forward)),
   'Max of Forward: {:.4f} ms'.format(max(delta_forward)),
   'Min of Forward: {:.4f} ms'.format(min(delta_forward)),
   'Average of Reverse: {:.4f} ms'.format(avg(delta_reverse)),
   'Max of Reverse: {:.4f} ms'.format(max(delta_reverse)),
   'Min of Reverse: {:.4f} ms'.format(min(delta_reverse))
   ))

props = dict(boxstyle='round', facecolor='white', alpha=0.5)

ax[0].text(0.05, 0.95, textstr, transform=ax[0].transAxes, fontsize=12, verticalalignment='top', bbox=props)

plt.show()
