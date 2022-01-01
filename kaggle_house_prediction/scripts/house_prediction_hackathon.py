import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns

error_codes = {
    200 : "success",
    404 : "data file not found"
}

class Solution:
    def __init__(self):
        self.current_path = os.getcwd()
        self.parent_path = os.path.dirname(self.current_path)
        self.train_path = os.path.join(self.parent_path, "data", "train")
        self.test_path = os.path.join(self.parent_path, "data", "test")


if __name__ == '__main__':
    class_object = Solution()
    result = class_object.gradient_desent()
    print(error_codes[result])