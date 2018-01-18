# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 15:53:33 2018

@author: gaoyf
"""
import numpy as ny
import matplotlib.pyplot as plt

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
    return 1.0/(1+ny.exp(-inX))

def gradAscent(dataMatIn, classLabels):
    dataMatrix = ny.mat(dataMatIn)
    labelMat = ny.mat(classLabels).transpose()
    m,n = ny.shape(dataMatrix)
    alpha = 0.001
    maxCycles = 500
    weights = ny.ones((n,1))
    for k in range(maxCycles):
        h = sigmoid(dataMatrix * weights)
        error = (labelMat -h)
        weights = weights + alpha * dataMatrix.transpose()*error
    return weights

def plotBestFit(weights):
    dataMat,labelMat = loadDataSet()
    dataArr = ny.array(dataMat)
    n = ny.shape(dataArr)[0]
    xcord1=[];ycord1=[]
    xcord2=[];ycord2=[]
    for i in range(n):
        if int(labelMat[i]) == 1:
            xcord1.append(dataArr[i,1])
            ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i,1])
            ycord2.append(dataArr[i,2])
        
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1,ycord1,s=30,c='red',marker='s')
    ax.scatter(xcord2,ycord2,s=30,c='green')
    x=ny.arange(-6.0,6.0,0.1)
    y=(-weights[0]-weights[1]*x)/weights[2]
    ax.plot(x,y)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()
        
    