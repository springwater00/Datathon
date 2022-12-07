import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

exercise = sns.load_dataset("exercise")

df = pd.DataFrame(exercise)
print(df.head())
print(df.tail())
print(df.columns)
print(df['diet'].value_counts())
print(df['kind'].value_counts())

#print kind is walking
walking_df = df[df['kind'] == 'walking']
#print(walking_df)

#print pulse with diet is low fat
x = df[df['diet'] == 'low fat'].loc[:, 'pulse'].mean()
y = df[df['diet'] == 'no fat'].loc[:, 'pulse'].mean()
print(x, y)

#print bar diet plot
def print_bar(df):
    plt.bar(['low fat', 'no fat'], [x, y])
    plt.show()

#print pulse
def print_pulse(df):
    x_rest = df[(df['diet'] == 'low fat') & (df['kind'] == 'rest')].loc[:, 'pulse'].mean()
    x_run = df[(df['diet'] == 'low fat') & (df['kind'] == 'running')].loc[:, 'pulse'].mean()
    y_rest = df[(df['diet'] == 'no fat') & (df['kind'] == 'rest')].loc[:, 'pulse'].mean()
    y_run = df[(df['diet'] == 'no fat') & (df['kind'] == 'running')].loc[:, 'pulse'].mean()

    plt.bar([0, 1, 2, 3], [x_rest, x_run, y_rest, y_run])
    plt.show()

#print scatter time and pulse plot
def print_scatter(df):
    plt.subplot(2,2,1)
    x = df[(df['diet'] == 'low fat') & (df['kind'] == 'rest')].loc[:, 'time']
    y = df[(df['diet'] == 'low fat') & (df['kind'] == 'rest')].loc[:, 'pulse']
    plt.scatter(x, y)
    plt.xlim([-1, 3])
    plt.ylim([60, 170])

    plt.subplot(2,2,2)
    x = x = df[(df['diet'] == 'low fat') & (df['kind'] == 'running')].loc[:, 'time']
    y = df[(df['diet'] == 'low fat') & (df['kind'] == 'running')].loc[:, 'pulse']
    plt.scatter(x, y)
    plt.xlim([-1, 3])
    plt.ylim([60, 170])

    plt.subplot(2,2,3)
    x = df[(df['diet'] == 'no fat') & (df['kind'] == 'rest')].loc[:, 'time']
    y = df[(df['diet'] == 'no fat') & (df['kind'] == 'rest')].loc[:, 'pulse']
    plt.scatter(x, y)
    plt.xlim([-1, 3])
    plt.ylim([60, 170])

    plt.subplot(2,2,4)
    x = df[(df['diet'] == 'no fat') & (df['kind'] == 'running')].loc[:, 'time']
    y = df[(df['diet'] == 'no fat') & (df['kind'] == 'running')].loc[:, 'pulse']
    plt.scatter(x, y)
    plt.xlim([-1, 3])
    plt.ylim([60, 170])

    plt.show()

#combine plots
def print_plots(df):
    x = df[(df['diet'] == 'low fat') & (df['kind'] == 'rest')].loc[:, 'time']
    y = df[(df['diet'] == 'low fat') & (df['kind'] == 'rest')].loc[:, 'pulse']
    plt.scatter(x, y, color='purple')

    x = x = df[(df['diet'] == 'low fat') & (df['kind'] == 'running')].loc[:, 'time']
    y = df[(df['diet'] == 'low fat') & (df['kind'] == 'running')].loc[:, 'pulse']
    plt.scatter(x, y, color='blue')

    x = df[(df['diet'] == 'no fat') & (df['kind'] == 'rest')].loc[:, 'time']
    y = df[(df['diet'] == 'no fat') & (df['kind'] == 'rest')].loc[:, 'pulse']
    plt.scatter(x, y, color='pink')

    x = df[(df['diet'] == 'no fat') & (df['kind'] == 'running')].loc[:, 'time']
    y = df[(df['diet'] == 'no fat') & (df['kind'] == 'running')].loc[:, 'pulse']
    plt.scatter(x, y, color='red')

    plt.show()
