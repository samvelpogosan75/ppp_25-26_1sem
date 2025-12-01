def to_seconds(interval):
    kind, *values = interval.split()
    if kind == 'hms':
        h, m, s = map(int, values[0].split(':'))
        return h*3600 + m*60 + s
    elif kind == 'ms':
        return int(values[0]) // 1000
    elif kind == 'minsec':
        m, s = map(int, values)
        return m*60 + s
    elif kind == 'hours':
        return int(float(values[0])*3600)
    else:
        return 0

def human_readable(sec):
    h = sec // 3600
    m = (sec % 3600) // 60
    s = sec % 60
    return f"{h} h {m} min {s} s"

def compute(intervals, command):
    seconds_list = [to_seconds(i) for i in intervals]
    if command == 'sum':
        result = sum(seconds_list)
        label = "Total"
    elif command == 'avg':
        result = sum(seconds_list) // len(seconds_list)
        label = "Average"
    elif command == 'max':
        result = max(seconds_list)
        label = "Max"
    elif command == 'min':
        result = min(seconds_list)
        label = "Min"
    else:
        return "Unknown command"
    
    return f"{label}: {human_readable(result)}"

data = [
    "hms 01:30:00",
    "ms 90000",
    "minsec 3 45",
    "hours 2.5"
]

print(compute(data, 'sum'))
print(compute(data, 'avg'))
print(compute(data, 'max'))
print(compute(data, 'min'))