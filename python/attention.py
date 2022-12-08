import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

attention = sns.load_dataset("attention")
df = pd.DataFrame(attention)

def info(df):
    #get imformation of attention.csv
    print(df.columns)
    print(df.head())
    print(df.tail())
    print(df.info())

    for column in df.columns:
        print(df[column].value_counts())

def print_score(df):
    #relationship solution with score according to attention
    ax1_x = df[df["attention"] == "divided"].loc[:, "solutions"]
    ax1_y = df[df["attention"] == "divided"].loc[:, "score"]
    ax2_x = df[df["attention"] == "focused"].loc[:, "solutions"]
    ax2_y = df[df["attention"] == "focused"].loc[:, "score"]
    plt.xlabel("solutions")
    plt.ylabel("score")
    plt.plot(ax1_x, ax1_y, 'ro')
    plt.plot(ax2_x, ax2_y, 'bo')
    plt.show()



