import sys

TICK = 1 / 8000

with open(str(sys.argv[1]), 'r') as f: 
    line = f.readline()
    line = f.readline()
    new_line = line.strip().split(',')
    data = [
        float(new_line[1].strip('"')), 
        new_line[2].strip('"'), 
        new_line[3].strip('"'), 
        int(new_line[-2].strip('"')), 
        int(new_line[-1].strip('"'))
        ]
    base_ts = data[3]
    print(data)
    while True:
        line = f.readline()
        if not line:
            break
        new_line = line.strip().split(',')
        data = [
            float(new_line[1].strip('"')), 
            new_line[2].strip('"'), 
            new_line[3].strip('"'), 
            int(new_line[-2].strip('"')), 
            int(new_line[-1].strip('"'))
            ]
        print(data[3] - base_ts)
        base_ts = data[3]
        # print(data)

print(TICK)