# -*- coding:utf-8 -*-

import os

path = 'F://2'

for file_1 in os.listdir(path):
    a = os.path.join(path, file_1)
    for file_2 in os.listdir(a):
        for file_3 in os.listdir(os.path.join(a, file_2)):
            p = os.path.splitext(file_3)
            print(p)
            if p[1] == '.jpg':
                newname = p[0] + '.png'
                os.chdir(os.path.join(a, file_2))
                os.rename(file_3, newname)
