#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 23:34:49 2017

@author: yuchunyan
"""

"""
file's format:
#column1\t column2 \t ....... \t columnN-1 \t columnN
#data1\t data2 \t ...... \t dataN-1 \t Label1

@result:

TODO：change fixed 3 column to dynamic columnNumbers
    
"""
def file2Matrix(fileName):
    fr = open(fileName)
    arrayLines = fr.readlines()
    numberOfLines = len(arrayLines)
    #TODO:change 3 to varible
    returnMat = zeros((numberOfLines,3))
    classLabelVector = []
    index = 0
    
    for line in arrayLines:
        line = line.strip()
        listFromLine = line.split('\t')
        #TODO:change 3 to varible
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
        
    return returnMat,classLabelVector
    