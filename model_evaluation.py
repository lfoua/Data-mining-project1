#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 08:52:29 2023

@author: loufoua
"""

import pandas as pd

def model_evaluation(df_result):
    TP = 0
    FP = 0
    TN = 0
    FN = 0
    
    data = {" ":["TP", "FP", "TN", "FN", "Sensitivity", "Specificity"]}
    for k in [1, 3, 5, 7]:
        
        for i in range(1, len(df_result.index)):
            
            if df_result.loc[i].at["Prediction k="+str(k)] == 1 and df_result.loc[i].at["Actual Grade"] == 1:
                TP += 1 
            elif df_result.loc[i].at["Prediction k="+str(k)] == 1 and df_result.loc[i].at["Actual Grade"] == 0:
                FP += 1
            elif df_result.loc[i].at["Prediction k="+str(k)] == 0 and df_result.loc[i].at["Actual Grade"] == 0:
                TN += 1
            elif df_result.loc[i].at["Prediction k="+str(k)] == 0 and df_result.loc[i].at["Actual Grade"] == 1:
                FN += 1
            else:
                continue
        sensitivity = TP/(TP + FN)
        specificity = TN/(TN + FP)
        data["k="+str(k)]=[TP,FP,TN,FN,sensitivity,specificity]
        
    return data

result = pd.read_csv('result.csv')
df_result = pd.DataFrame(result)


df_evaluation = pd.DataFrame(model_evaluation(df_result))
df_evaluation.to_csv('Evaluation.csv', index=False)

