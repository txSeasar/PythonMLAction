#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 20:41:31 2017

@author: yuchunyan
"""
"""
algorithm:KNN
"""
def classifyKNN(obj, sampleDataSet, labels, k):
    dataSetSize = sampleDataSet.shape[0]
    diffMat = tile(obj, (dataSetSize,1)) - sampleDataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distance = sqDistances**0.5
    sortedDistIndicies = distance.argsort()
    classCount = {}
    for i in range(k):
        voteLabel = labels[sortedDistIndicies[i]]
        classCount[voteLabel] = classCount.get(voteLabel,0)+1
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]


"""
algorithm:decision tree
"""
def classifyDecisionTrees(obj, sampleDataSet, labels):
    dataSetSize = sampleDataSet.shape[0]
    diffMat = tile(obj, (dataSetSize,1)) - sampleDataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distance = sqDistances**0.5
    sortedDistIndicies = distance.argsort()
    classCount = {}
    for i in range(k):
        voteLabel = labels[sortedDistIndicies[i]]
        classCount[voteLabel] = classCount.get(voteLabel,0)+1
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]