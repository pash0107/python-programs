def create_cubes(n):
    for x in range(n):
        yield x**3
    
for x in create_cubes(20):
    print(x)