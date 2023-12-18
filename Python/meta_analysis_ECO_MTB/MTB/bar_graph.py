import numpy as np
import matplotlib.pyplot as plt
 
  
# creating the dataset
condition = ["BPD16-BPD24", "TRP16-TRP24", "TRP16 vs BPD16", "TRP24 vs BPD24"]
v = [0.7687, 0.9202, 0.7931, 0.8811]
c = ["red", "blue", "green", "yellow"]
 
# creating the bar plot
plt.bar(condition, height = v, color = c)
plt.show()