names = ['one','two','three']
index = 0

# for name in names:
#     print(index, name)
#     index += 1

for index, name in enumerate(names, start=0):
    print(index, name)