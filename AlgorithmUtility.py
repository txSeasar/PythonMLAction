#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 19:09:35 2017

@author: yuchunyan
"""

from math import log

def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for eachVec in dataSet:
        currentLabel = eachVec[-1]
        if currentLabel not in labelCounts.keys:
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
        
    shannonEnt = 0.0
    for key in labelCounts.keys:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob,2)
        
    return shannonEnt
        