# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 15:53:33 2018

@author: gaoyf
"""

def loadDataSet():
    dataMat = []
    labelMat = []
    fr = open('testData/testLogisticData.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat,labelMat

def sigmoid(inX):
    return 1.0/(1+exp(-inX))

