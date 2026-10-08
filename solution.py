import random
import csv
import matplotlib.pyplot as plt
import numpy as np

filename = 'stroke_separable.csv'

def load_data(filename):
    with open(filename) as f:
        f.readline()
        csvReader = csv.reader(f)
        age = []
        hg = []
        cls = []
        for line in f:
            data = line.strip('\n').split(',')
            age.append(int(data[0]))
            hg.append(int(data[1]))
            cls.append(int(data[2]))
        age = tuple(age)
        hg = tuple(hg)
        cls = tuple(cls)
        return age, hg, cls
age, hg, cls = load_data(filename)

def perceptron(age,hg,cls):
    random.seed(10)
    w0 = random.random()
    w_age = random.random()
    w_hg = random.random()
    w = [w0,w_age,w_hg]
    
    for i in range(50):
        xIndex = random.randint(0,len(age)-1)
        x = [1, age[xIndex],hg[xIndex]]
        dotProduct = w0 + w_age * x[1] + w_hg * x[2]
        print(x, cls[xIndex])

        if cls[xIndex] == 0:
            if dotProduct < 0: # x @ w < 0:
                continue
            else:
                print("subtract")
                w_age -= x[1]
                w_hg -= x[2]
                w0 -= x[0]
                continue
        if cls[xIndex] == 1:
            if dotProduct >= 0:  # x @ w >= 0:
                continue
            else:
                print("add")
                w_age += x[1]
                w_hg += x[2]
                w0 += x[0]
                continue
    #y = w0 + w_age * age + w_hg * hg
    return w0,w_age,w_hg
w0, w_age, w_hg =  perceptron(age,hg,cls)


