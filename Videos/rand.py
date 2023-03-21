from random import randint

n = (randint(0,5), randint(0,5), randint(0,5))

print(n)

m = [    
    [n[0]],
    [n[1]],
    [n[2]]
]

print(m[0:3])