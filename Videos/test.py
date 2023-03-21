from random import randint

m = []
for i in range(5):
    n = randint(0, 1)
    m.append(n)

TEST_DATA = [    
    [m[0]],
    [m[1]],
    [m[2]],
    [m[3]],
    [m[4]]
    ]

for i in range(len(m)):
    if m[i] == 1:
        m[i] = 'lisa'
    else:
        m[i] = 'irregular'

print(m)

