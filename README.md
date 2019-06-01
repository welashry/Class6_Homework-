# Class6_Homework-

1- Save your dataset "diabetes.csv" to your Desktop
2-Create a script on your Desktop called "test.py" and follow the instructions below:-
Import the libraries that you will need in your script(pandas-matplotlib-os, etc..):
               
               import pandas as pd

               import numpy as np

               import matplotlib.pyplot as plt

               import os
               from mpl_toolkits.mplot3d import Axes3D
Load the data:
           diabetes_df = pd.read_csv('diabetes.csv',

                     sep=',',

                     header=0)
To display the data in a table:
                                print(diabetes_df.to_string())
To generate tons of figures:
                        for col1_idx, column1 in enumerate(df.columns):

    for col2_idx, column2 in enumerate(df.columns):

        if col1_idx < col2_idx:

            fig, axes = plt.subplots(1, 1, figsize=(5, 5))

            axes.scatter(df[column1], df[column2], label=f'{column1} to {column2}', color='green', marker='x')

            axes.set_title(f'{column1} to {column2}')

            axes.set_xlabel(column1)

            axes.set_ylabel(column2)

            axes.legend()

            plt.savefig(f'plots/tons_of_figures/diabetes_{column1}_{column2}_scatter.png', dpi=300)

            plt.close(fig))
   
   To have multiple plots on the same figure:
                                                

                                  plt.style.use('ggplot')

                                  fig, axes = plt.subplots(3, 1, figsize=(10, 10))



                                  axes[0].plot(df['AGE'])

                                  axes[0].set_xlabel('Index')

                                  axes[0].set_ylabel('AGE')

                                  axes[0].set_title('AGE')



                                 axes[1].scatter(df['AGE'], df['BMI'])

                                 axes[1].set_xlabel('AGE')

                                 axes[1].set_ylabel('BMI')

                                 axes[1].set_title('AGE vs BMI')


                                 axes[2].scatter(df['BP'], df['SEX'])

                                 axes[2].set_xlabel('BP')

                                 axes[2].set_ylabel('SEX')

                                 axes[2].set_title('BP vs SEX')


                                plt.tight_layout()

                                plt.savefig("multiple_plots_on_the_same_figure.png")
                                
                                
To have multiple plots on the same axes:

                                   plt.style.use("ggplot")

                            fig, axes = plt.subplots(1, 1, figsize=(5, 5))

                            axes.grid(axis='y', alpha=0.5)

                            axes.scatter(df['AGE'], df['BP'], label='BP', marker='^', color='green')

                            axes.set_xlabel('AGE')

                            axes.scatter(df['AGE'], df['BMI'], label='BMI', marker='s', color='orange')

                            axes.scatter(df['AGE'], df['SEX'], label='SEX', color='aqua')

                            axes.set_title(f'Diabetes comparisons')

                            axes.legend()

                            plt.savefig(f'plots/matplotlib_multiple_plot_axes/multiple_plots_on_the_same_axes.png', dpi=300)

                    
To have 3D  visualizations:
                           
                           df.drop('AGE', axis=1, inplace=True)

                            fig = plt.figure()

                            axes = fig.add_subplot(1, 1, 1, projection='3d')

                            line1 = axes.scatter(df['SEX'], df['BMI'], df['BP'])

                            line2 = axes.scatter(df['SEX'], df['BMI'], df['BP'])


                            axes.set_xlabel('SEX')

                            axes.set_ylabel('BMI')

                            axes.set_zlabel('BP')

                            plt.savefig('plots/3d.png')
                            
                            
the most interest figure i found shows  that the relation between bmi and age(bmi vs age) 
people who are  40 year old or older have high bmi(body mass index) which increases your risk of having diabetes



#Doker

-Create a directory "dockerFolder" on the desktop and inside it Create a Dockerfile using (vim Dockerfile) contains Operating System such as ubuntu using (FROM Ubuntu:latest) or any OS on DockerHub and running the updates using (RUN apt-get update), then copy the script you want to run using (COPY) command and CMD to run your image
-Docker build ."to build your image"
-Now your image successfully built
-Use (docker run 'image ID') to run your image






































