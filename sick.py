import pandas as pd
import numpy as np


def main():
    dis_prob = pd.read_csv("disease.csv", sep = ";")
    dis_prob['probability'] = dis_prob['количество пациентов'] / dis_prob['количество пациентов'].iloc[-1]
    dis_prob.drop()
    print(dis_prob)

if __name__ == "__main__":
    main()
