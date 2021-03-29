#Importing Numpy, Matplotlib, Math, and Pandas
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd 

figure_counter = 0

def extract_data(extension):
    raw_data = pd.read_csv(extension + '.csv', sep = ';', header = None)
    edited_data = raw_data.to_numpy()
    edited_data = edited_data.astype(np.float)
    return edited_data

def calcHead(p, rho, g):
    H = p/(rho*g)
    return H

def calcTorque(F):
    r = 0.045
    T = F*r
    return T

def calcBrakePower(n, T):
    Pb = 2.0*math.pi*n*T/60.0
    return Pb

def calcHydroPower(rho, g, H, Q):
    Ph = rho*g*H*Q/60.0
    return Ph

def calcEfficiency(Pb, Ph):
    E = Pb/Ph*100.0
    return E

def analysisConduct(name):
    data = extract_data(name)
    H = calcHead(data[:, 1], 1000.0, 9.81)
    T = calcTorque(data[:, 3])
    Pb = calcBrakePower(data[:, 2], T)
    Ph = calcHydroPower(1000.0,  9.81, H, data[:, 0])
    E = calcEfficiency(Pb, Ph)

    return data, H, T, Pb, Ph, E

def makingPlots(fig_number, x1, x2, y1, y2, runs, name1, name2, title):
    fig = plt.figure(fig_number)
    plt.plot(x1, y1)
    plt.plot(x2, y2)
    plt.legend([name1 + '% Turbine Speed', name2 + '% Turbine Speed'])
    plt.xlabel('Rotational Speed [rpm]')
    plt.ylabel(runs)
    plt.title(title)
    plt.savefig(title + '.png')
    fig.show()

def mainFunc():
    global figure_counter
    set90, H90, T90, Pb90, Ph90, E90 = analysisConduct('90')
    set100, H100, T100, Pb100, Ph100, E100 = analysisConduct('100')

    figure_counter += 1
    makingPlots(figure_counter, set100[:, 2], set90[:, 2], Pb100, Pb90, 'Brake Power [W]', '100', '90', 'Brake Power vs Rotational Speed')
    figure_counter += 1
    makingPlots(figure_counter, set100[:, 2], set90[:, 2], T100, T90, 'Brake Torque [Nm]', '100', '90', 'Torque vs Rotational Speed')
    figure_counter += 1
    makingPlots(figure_counter, set100[:, 2], set90[:, 2], E100, E90, 'Efficiency [%]', '100', '90', 'Efficiency vs Rotational Speed')

mainFunc()

input()