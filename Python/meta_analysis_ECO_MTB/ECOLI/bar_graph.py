import numpy as np
import matplotlib.pyplot as plt
 
  
# creating the dataset
condition = ["Cold stress (CS)", "Oxydative stress (OS)", "CS vs OS"]
v = [0.9798, 0.9939, 0.9613]
c = ["red", "blue", "green"]
 
# creating the bar plot
plt.bar(condition, height = v, color = c)
plt.show()