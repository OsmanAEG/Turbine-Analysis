#Importing Numpy, Matplotlib, Math, and Pandas
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd 

figure_counter = 0

def extract_data(extension):
    raw_data = pd.read_csv(extension + '.csv', sep = ';', header = None)
    edited_data = raw_data.to_numpy()
    return edited_data

def calcHead(p, rho, g):
    H = P/(rho*g)
    return H

def calcTorque(F):
    r = 0.045
    T = F*r
    return T

def calcBrakePower(n, T):
    Pb = 2.0*math.pi*n*T/60.0
    return Pb

def calcHydroPower(rho, g, H, Q):
    Ph = rho*h*H*Q
    return Ph

def calcEfficiency(Pb, Ph):
    E = Pb/Ph
    return E

def analysisConduct(name):
    data = extract_data(name)
    H = calcHead(data[1], 1000.0, 9.81)
    T = calcTorque(data[3])
    Pb = calcBrakePower(data[2], T)
    Ph = calcHydroPower(1000.0,  9.81, H, data[0])

    return data, H, T, Pb, Ph

def makingPlots(fig_number, x1, x2, y1, y2, runs):
    set90, H90, T90, Pb90, Ph90 = analysisConduct('90')
    set100, H100, T100, Pb100, Ph100 = analysisConduct('100')

