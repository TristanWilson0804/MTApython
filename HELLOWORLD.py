# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 11:25:17 2021

@author: MTAEXAM
"""
f = open('0001.txt','r')
for line in f:
    print(line)
f.close()

with open ('0001.txt','r') as f:
    for line in f:
        print(line)
