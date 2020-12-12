import os

for filename in os.listdir('set/'):
    sub_index = filename.index('_')
    print(filename[0:sub_index])