names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']


n = min(len(names), len(colors))

for i in range(n):
    print names[i], '-->', colors[i]

for name, color in zip(names, colors):
    print name, '-->', color

for name, color in izip(names, colors):
    print name, '-->', color
