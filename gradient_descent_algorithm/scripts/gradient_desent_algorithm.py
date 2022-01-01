import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

error_codes = {
    200 : "success",
    404 : "data file not found"
}

class Solution:
    def __init__(self, file_name):
        self.file_name = file_name
        self.current_path = os.getcwd()
        self.parent_path = os.path.dirname(self.current_path)
        self.data_path = os.path.join(self.parent_path, "data", self.file_name)

    def gradient_desent(self):
        if os.path.exists(self.data_path):
            self.data = pd.read_csv(self.data_path)
            self.X = self.data.iloc[:,0]
            self.Y = self.data.iloc[:,1]
            # plt.scatter(self.X,self.Y)
            # plt.show()
            self.initialize_slope_intercept()
            self.learning_rate_and_iterations()
            self.iterate_loop()
            self.make_prediction()
            self.plot_gradient_descent()
            return 200
        return 404

    def initialize_slope_intercept(self):
        '''
        Step 1: Initialize Slope and Intercept
        :return:
        '''
        self.slope = 0
        self.intercept = 0

    def learning_rate_and_iterations(self):
        '''
        Step 2: Initialize Learning Rate and Iterations
        :return:
        '''
        self.learning_rate = 0.0001
        self.iteration = 1000

    def iterate_loop(self):
        '''
        Step 3:
        Loop Iteration (Performing Gradient Descent)
        :return:
        '''
        self.data_length = float(len(self.X))

        for loop in range(self.iteration):
            self.Y_prediction = (self.slope * self.X) + self.intercept
            self.step_slope = (-2/self.data_length)*sum(self.X * (self.Y - self.Y_prediction))
            self.step_intercept = (-2/self.data_length)*sum(self.Y - self.Y_prediction)
            self.slope -= (self.learning_rate * self.step_slope)
            self.intercept -= (self.learning_rate * self.step_intercept)
            print("----------------------------------------")
            print(f"Iteration : {loop + 1}")
            print(f"Slope : {self.slope}")
            print(f"Intercept : {self.intercept}")

        print(f"After {self.iteration} iterations value slope is {self.slope} and intercept is {self.intercept}")

    def make_prediction(self):
        '''
        Step 4: Make Y prediction (Y_prediction = m*X+c)
        :return:
        '''
        self.Y_prediction = (self.slope * self.X) + self.intercept

    def plot_gradient_descent(self):
        plt.scatter(self.X, self.Y)
        plt.plot([min(self.X), max(self.X)], [min(self.Y_prediction), max(self.Y_prediction)], color='red')
        plt.show()

if __name__ == '__main__':

    file_name = "data.csv"
    class_object = Solution(file_name)
    result = class_object.gradient_desent()
    print(error_codes[result])