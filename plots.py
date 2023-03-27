import pandas as pd
import matplotlib.pyplot as plt

elements = ["Carbon", "Copper", "Iron", "Zinc"]
colors = ["#fc0362", "#03fc84", "#0352fc", "#cf03fc"]

data_hydrogen = pd.read_csv("Hydrogen in Carbon.txt", sep="\t", header=None)
data_copper = pd.read_csv("Hydrogen in Copper.txt", sep="\t", header=None)
data_iron = pd.read_csv("Hydrogen in Iron.txt", sep="\t", header=None)
data_zinc = pd.read_csv("Hydrogen in Zinc.txt", sep="\t", header=None)

data = [data_hydrogen, data_copper, data_iron, data_zinc]

#--------------histogram plots-----------------

bins = 200

for i in range(0, len(data)):
    plt.title("Energy of Hydrogen Ions on " + elements[i])
    plt.xlabel("Energy (MeV)")
    plt.ylabel("Frequency")
    plt.hist(data[i][3], bins=bins, histtype="step", color=colors[i])
    file_name = "histogram_" + elements[i] + ".png"
    plt.savefig(file_name)
    plt.show()


for i in range(0, len(data)):
    plt.hist(data[i][3], bins=bins, histtype="step", color=colors[i])

plt.title("Energy of Hydrogen Ions on different Materials")
plt.legend(elements)
plt.xlabel("Energy (MeV)")
plt.ylabel("Frequency")

plt.savefig("histogram plots.png")
plt.savefig("histogram plots.pdf")
plt.show()

#------------scatter plots----------------

#set size
'''
canvas_size = []
horizontal = []
vertical = []
for i in range(0, len(data)):
    horizontal.append(max(data[i][5]))
    horizontal.append(min(data[i][5]))
    vertical.append(min(data[i][6]))
    vertical.append(max(data[i][6]))
horizontal_size = int(max(horizontal) - min(horizontal))
vertical_size = int(max(vertical) - min(vertical))
'''

#show each plot
for i in range(0, len(data)):
    plt.title("Scatter plot showing position of ions on " + elements[i])
    plt.xlabel("y-axis")
    plt.ylabel("z-axis")
    plt.scatter(data[i][5], data[i][6], alpha=0.5, color=colors[i])
    file_name = "scatter_" + elements[i] + ".png"
    plt.savefig(file_name)
    plt.show()

#show all elements
for i in range(0, len(data)):
    plt.scatter(data[i][5], data[i][6], alpha=0.5, color=colors[i])

plt.title("Scatter plot showing position of ions")
plt.xlabel("y-axis")
plt.ylabel("z-axis")
plt.legend(elements)
plt.savefig("scatter plots.png")
plt.savefig("scatter plots.pdf")

plt.show()