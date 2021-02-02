# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 14:36:49 2021

@author: MTAEXAM
"""

score=int(input("分数:"))
if score>=90 and score<=100 and score<=0:
    print("A")
elif score>=80 and score<=89 and score<=0:
    print("B")
elif score>=70 and score<=79 and score<=0:
    print("C")
elif score>=60 and score<=69 and score<=0:
    print("not good")
else:
    print("error")