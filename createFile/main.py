import os

vol = 1024*1024*1024 # 1GB 
with open('results/file', 'wb') as fout:
    fout.write(os.urandom(vol)) 