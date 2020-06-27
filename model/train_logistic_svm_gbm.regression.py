# -*- coding: utf-8 -*-
import sys
import pandas as pd
import numpy as np
import pickle
import torch
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn import metrics
from sklearn.metrics import roc_auc_score
from sklearn.metrics import average_precision_score
from sklearn import datasets, ensemble
from sklearn.inspection import permutation_importance
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

## Loading Data
trainDataFile = './data/trainData.pkl'
with open(trainDataFile, 'rb') as f:
    trainData = pickle.load(f)

testDataFile = './data/testData.pkl'
with open(testDataFile, 'rb') as f:
    testData = pickle.load(f)

trainMeanArrays = None
trainMaxArrays = None
trainLastArrays = None

trainShockArray = []
trainMortality  = []
for k,v in trainData.items() :
    meanArray =  np.mean( v[0].numpy(), axis=0, keepdims=True )[0]
    maxArray =  np.max( v[0].numpy(), axis=0, keepdims=True )[0]
    lastArray = v[0].numpy()[-1]
    if trainMeanArrays is None :
        trainMeanArrays = meanArray
        trainMaxArrays = maxArray
        trainLastArrays = lastArray
    else :
        trainMeanArrays = np.append ( trainMeanArrays, meanArray )
        trainMaxArrays = np.append ( trainMaxArrays, maxArray )
        trainLastArrays = np.append ( trainLastArrays, lastArray )
    trainShockArray.append( v[1][0] )
    trainMortality.append( v[1][1] )
trainMeanArrays = trainMeanArrays.reshape( len(trainData.keys()), 84 )
trainMaxArrays = trainMaxArrays.reshape( len(trainData.keys()), 84 )
trainLastArrays = trainLastArrays.reshape( len(trainData.keys()), 84 )

testMeanArrays = None
testMaxArrays = None
testLastArrays = None

testShockArray = []
testMortality  = []
for k,v in testData.items() :
    meanArray =  np.mean( v[0].numpy(), axis=0, keepdims=True )[0]
    maxArray =  np.max( v[0].numpy(), axis=0, keepdims=True )[0]
    lastArray = v[0].numpy()[-1]
    if testMeanArrays is None :
        testMeanArrays = meanArray
        testMaxArrays = maxArray
        testLastArrays = lastArray
    else :
        testMeanArrays = np.append ( testMeanArrays, meanArray )
        testMaxArrays = np.append ( testMaxArrays, maxArray )
        testLastArrays = np.append ( testLastArrays, lastArray )
    testShockArray.append( v[1][0] )
    testMortality.append( v[1][1] )
testMeanArrays = testMeanArrays.reshape( len(testData.keys()), 84 )
testMaxArrays = testMaxArrays.reshape( len(testData.keys()), 84 )
testLastArrays = testLastArrays.reshape( len(testData.keys()), 84 )

# Model
train_x = trainMeanArrays[:,:-1]
test_x  = testMeanArrays[:,:-1]
train_shock_y = np.array(trainShockArray)
test_shock_y = np.array(testShockArray)
train_mortality_y = np.array(trainMortality)
test_smortality_y = np.array(testMortality)

## Logistic Regression
lr = LogisticRegression(C=100.0, random_state=0, max_iter = 1000000, solver = 'saga')
lr.fit(train_x, train_shock_y)

pred_train_y = lr.predict(train_x)
pred_test_y = lr.predict(test_x)
print("Logistic Regression shock")
print(roc_auc_score(train_shock_y, pred_train_y))
print(average_precision_score(train_shock_y, pred_train_y))
print(roc_auc_score(test_shock_y, pred_test_y))
print(average_precision_score(test_shock_y, pred_test_y))

lr.fit(train_x, train_mortality_y)
pred_train_y = lr.predict(train_x)
pred_test_y = lr.predict(test_x)
print("Logistic Regression mortality")
print(roc_auc_score(train_mortality_y, pred_train_y))
print(average_precision_score(train_mortality_y, pred_train_y))
print(roc_auc_score(test_smortality_y, pred_test_y))
print(average_precision_score(test_smortality_y, pred_test_y))

## SVM
regr = svm.SVR()
regr.fit(train_x, train_shock_y)

pred_train_y = regr.predict(train_x)
pred_test_y = regr.predict(test_x)
print("svm shock")
print(roc_auc_score(train_shock_y, pred_train_y))
print(average_precision_score(train_shock_y, pred_train_y))
print(roc_auc_score(test_shock_y, pred_test_y))
print(average_precision_score(test_shock_y, pred_test_y))

regr.fit(train_x, train_mortality_y)
pred_train_y = regr.predict(train_x)
pred_test_y = regr.predict(test_x)
print("svm mortality")
print(roc_auc_score(train_mortality_y, pred_train_y))
print(average_precision_score(train_mortality_y, pred_train_y))
print(roc_auc_score(test_smortality_y, pred_test_y))
print(average_precision_score(test_smortality_y, pred_test_y))

## GBM
params = {'n_estimators': 500,
          'max_depth': 4,
          'min_samples_split': 5,
          'learning_rate': 0.01,
          'loss': 'ls'}

reg = ensemble.GradientBoostingRegressor(**params)

reg.fit(train_x, train_shock_y)
pred_train_y = reg.predict(train_x)
pred_test_y = reg.predict(test_x)
print("gbm shock")
print(roc_auc_score(train_shock_y, pred_train_y))
print(average_precision_score(train_shock_y, pred_train_y))
print(roc_auc_score(test_shock_y, pred_test_y))
print(average_precision_score(test_shock_y, pred_test_y))

reg.fit(train_x, train_mortality_y)
pred_train_y = reg.predict(train_x)
pred_test_y = reg.predict(test_x)
print("gbm mortality")
print(roc_auc_score(train_mortality_y, pred_train_y))
print(average_precision_score(train_mortality_y, pred_train_y))
print(roc_auc_score(test_smortality_y, pred_test_y))
print(average_precision_score(test_smortality_y, pred_test_y))
