import pandas as pd
import matplotlib.pyplot as plt

elements = ["Carbon", "Copper", "Iron", "Zinc"]
colors = ["#fc0362", "#03fc84", "#0352fc", "#cf03fc"]

data_hydrogen = pd.read_csv("data/reformat/Hydrogen in Carbon.txt", sep="\t", header=None)
data_copper = pd.read_csv("data/reformat/Hydrogen in Copper.txt", sep="\t", header=None)
data_iron = pd.read_csv("data/reformat/Hydrogen in Iron.txt", sep="\t", header=None)
data_zinc = pd.read_csv("data/reformat/Hydrogen in Zinc.txt", sep="\t", header=None)

data = [data_hydrogen, data_copper, data_iron, data_zinc]

#--------------histogram plots-----------------

bins = 200

for i in range(0, len(data)):
    plt.title("Energy of Hydrogen Ions on " + elements[i])
    plt.xlabel("Energy (MeV)")
    plt.ylabel("Frequency")
    plt.hist(data[i][3], bins=bins, histtype="step", color=colors[i])
    file_name = "plots/histogram/histogram_" + elements[i] + ".png"
    plt.savefig(file_name)
    plt.show()


for i in range(0, len(data)):
    plt.hist(data[i][3], bins=bins, histtype="step", color=colors[i])

plt.title("Energy of Hydrogen Ions on different Materials")
plt.legend(elements)
plt.xlabel("Energy (MeV)")
plt.ylabel("Frequency")

plt.savefig("plots/histogram/histogram plots.png")
plt.savefig("plots/histogram/histogram plots.pdf")
plt.show()

#------------scatter plots----------------

#set size

limit = []
for i in range(0, len(data)):
    limit.append(abs(max(data[i][5])))
    limit.append(abs(min(data[i][5])))
    limit.append(abs(min(data[i][6])))
    limit.append(abs(max(data[i][6])))


#show each plot
for i in range(0, len(data)):
    ax = plt.axes()
    ax.set_aspect("equal")
    ax.set_xlim(-max(limit), max(limit))
    ax.set_ylim(-max(limit), max(limit))
    plt.title("Scatter plot showing position of ions on " + elements[i])
    plt.xlabel("y-axis")
    plt.ylabel("z-axis")
    plt.scatter(data[i][5], data[i][6], alpha=0.5, color=colors[i])
    file_name = "plots/scatter/scatter_" + elements[i] + ".png"
    plt.savefig(file_name)
    plt.show()

#show all elements
ax = plt.axes()
for i in range(0, len(data)):
    ax.set_aspect("equal")
    ax.set_xlim(-max(limit), max(limit))
    ax.set_ylim(-max(limit), max(limit))
    plt.scatter(data[i][5], data[i][6], alpha=0.5, color=colors[i])

plt.title("Scatter plot showing position of ions")
plt.xlabel("y-axis")
plt.ylabel("z-axis")
plt.legend(elements)
plt.savefig("plots/scatter/scatter plots.png")
plt.savefig("plots/scatter/scatter plots.pdf")

plt.show()