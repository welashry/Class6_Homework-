import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

import os
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv('diabetes.csv',

                 sep=',',

                 header=0)


#generate  ton of figures
os.makedirs('plots/tons__of_figures', exist_ok=True)

for col1_idx, column1 in enumerate(df.columns):

    for col2_idx, column2 in enumerate(df.columns):

        if col1_idx < col2_idx:

            fig, axes = plt.subplots(1, 1, figsize=(5, 5))

            axes.scatter(df[column1], df[column2], label=f'{column1} to {column2}', color='green', marker='x')

            axes.set_title(f'{column1} to {column2}')

            axes.set_xlabel(column1)

            axes.set_ylabel(column2)

            axes.legend()

            plt.savefig(f'plots/tons__of_figures/diabetes_{column1}_{column2}_scatter.png', dpi=300)

            plt.close(fig)

os.makedirs('plots/tons__of_figures/matplotlib__multiple_plot_axes', exist_ok=True)


#multiple plots on the same axes
plt.style.use("ggplot")

fig, axes = plt.subplots(1, 1, figsize=(5, 5))

axes.grid(axis='y', alpha=0.5)

axes.scatter(df['AGE'], df['BP'], label='BP', marker='^', color='green')

axes.set_xlabel('AGE')

axes.scatter(df['AGE'], df['BMI'], label='BMI', marker='s', color='orange')

axes.scatter(df['AGE'], df['SEX'], label='SEX', color='aqua')

axes.set_title(f'Diabetes comparisons')

axes.legend()

plt.savefig(f'plots/tons__of_figures/matplotlib__multiple_plot_axes/multiple_plots_on_the_same_axes.png', dpi=300)


#multiple plots on the same figure
os.makedirs(f'plots/tons__of_figures/matplotlib__multiple_plot_axes/matplotlib__multiple_plot_figure', exist_ok=True)
plt.style.use('ggplot')

fig, axes = plt.subplots(3, 1, figsize=(10, 10))

axes[0].scatter(df['BMI'],df['BP'])

axes[0].set_xlabel('BP')

axes[0].set_ylabel('BMI')

axes[0].set_title('BP VS BMI')



axes[1].scatter(df['AGE'], df['BMI'])

axes[1].set_xlabel('AGE')

axes[1].set_ylabel('BMI')

axes[1].set_title('AGE vs BMI')


axes[2].scatter(df['BP'], df['SEX'])

axes[2].set_xlabel('BP')

axes[2].set_ylabel('SEX')

axes[2].set_title('BP vs SEX')

plt.tight_layout()

plt.savefig(f'plots/tons__of_figures/matplotlib__multiple_plot_axes/matplotlib__multiple_plot_figure/multiple__plots_on_the_same_figure.png')

#3D visualizations
os.makedirs(f'plots/tons__of_figures/matplotlib__multiple_plot_axes/matplotlib__multiple_plot_figure/3d_folder', exist_ok=True)
df.drop('AGE', axis=1, inplace=True)

fig = plt.figure()

axes = fig.add_subplot(1, 1, 1, projection='3d')

line1 = axes.scatter(df['SEX'], df['BMI'], df['BP'], color='green')

line2 = axes.scatter(df['SEX'], df['BMI'], df['BP'], color='yellow')


axes.set_xlabel('SEX')

axes.set_ylabel('BMI')

axes.set_zlabel('BP')

plt.savefig('plots/tons__of_figures/matplotlib__multiple_plot_axes/matplotlib__multiple_plot_figure/3d_folder/3d_graph.png')



plt.close()

