#! /usr/bin/env python3
# coding: utf-8

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def main():
    un_panda = [100, 5, 20, 80]
# informations sur un panda [taille, poil, pate, ventre]
    un_panda_numpy = np.arrray(un_panda)
    un_bb_panda = un_panda_numpy / 2
    print(un_bb_panda)

    mps = pd.read_csv("current_mps.csv", sep=";")

if __name__ == "__main__":
    main()