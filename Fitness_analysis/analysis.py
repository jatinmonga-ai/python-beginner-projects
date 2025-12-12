import csv
import numpy as np
import matplotlib.pyplot as plt

days=[]
steps=[]
calories=[]
sleep=[]

with open("fitness_data.csv", "r") as file:
    reader= csv.DictReader(file)
    for row in reader:
        days.append(int(row["day"]))
        steps.append(int(row["steps"]))
        calories.append(int(row["calories"]))
        sleep.append(float(row["sleep_hours"]))

days= np.array(days)
steps= np.array(steps)
calories= np.array(calories)
sleep= np.array(sleep)


print("Average Steps:", np.mean(steps))
print("Maximum Steps:", np.max(steps))
print("Average Sleep Hours:", np.mean(sleep))
print("Total Calories Burned :", np.sum(calories))
print("Correlation (Sleep vs Steps):", np.corrcoef(sleep, steps)[0, 1])
                     
                     
# Create a figure with 3 subplots (3 rows, 1 column)
fig, axs = plt.subplots(3, 1, figsize=(6, 6))

# 1. Bar Chart: Steps Per Day 
axs[0].bar(days, steps)
axs[0].set_title("Steps Per Day")
axs[0].set_xlabel("Day")
axs[0].set_ylabel("Steps")
axs[0].grid(axis="y", linestyle='--', alpha=0.2)

# 2. Line Chart: Calories Burned 
axs[1].plot(days, calories, marker='o')
axs[1].set_title("Calories Burned Over Time")
axs[1].set_xlabel("Day")
axs[1].set_ylabel("Calories")
axs[1].grid(True, linestyle='--', alpha=0.3)

# 3. Scatter Plot: Sleep vs Steps 
axs[2].scatter(sleep, steps, s=30)
axs[2].set_title("Sleep vs Steps")
axs[2].set_xlabel("Hours of Sleep")
axs[2].set_ylabel("Steps")
axs[2].grid(True, linestyle='--', alpha=0.3)

# Adjust spacing so plots don’t overlap
plt.tight_layout()

plt.show()

                     
