# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 21:38:06 2018

@author: Mahadi
"""



import random


def password(length):
    
    m = str()
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"+"abcdefghijklmnopqrstuvwxyz" + "0123456789" + "@#$%&*/*+-_"
    
    for i in range(length):
        m = m + random.choice(characters)
    return m
    

#password(7)
    
