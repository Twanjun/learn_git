# -*- coding:utf-8 -*-

import os

path = ''

for files in os.listdir(path):
    a = os.path.join(path, files)
    for file in os.listdir(a):
        for file3 in os.listdir(os.path.join(a, file)):
            print(file3)
