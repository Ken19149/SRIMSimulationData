import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
text = str(open("Hydrogen in Carbon.txt", "r").read())
text = text.replace("    ", "\t")
text = text.replace("   ", "\t")
text = text.replace("  ", "\t")
text = text.replace(" ", "\t")
'''

data = pd.read_csv("Hydrogen in Carbon.txt", sep="\t", header=None)
avg = np.mean(data[3])
sd = np.std(data[3])

print("AVG: " + str(avg/(10**6)), "MeV")
print("SD: " + str(sd/(10**6)), "MeV")

bins = 200

''''''
#--------------histogram plot---------------
x = plt.hist((data[3]), bins=bins, histtype="step")
plt.title("Energy of Hydrogen Ions on Carbon Material")
plt.xlabel("Energy (MeV)")
plt.ylabel("Frequency")

#-------------FWHM-------------
max_frequency = max(x[0])           #288
half_max_freq = max_frequency/2     #144
max_position = None
half_position = []

for i in range(len(x[0])):  #highest frequency
    if x[0][i]==max_frequency:
        max_position = i    #151

max_value = x[1][max_position]      #5054241.0015
half_max_value = max_value/2        #2527120.50075

temp = []  # store value to compare temporarily
for i in range(len(x[0])):  #highest frequency
    try:
        if x[0][i]==half_max_freq:
            half_position.append(i)     #[136]
        elif (x[0][i-1] < half_max_freq < x[0][i+1]) or (x[0][i-1] > half_max_freq > x[0][i+1]):
            temp.append(i)
            if len(temp)==2 and abs(temp[0] - temp[1])==1:
                half_position.append(i) #169
                temp.clear()
            elif len(temp)==2 and abs(temp[0] - temp[1])!=1:
                temp.clear()

    except:
        continue

half_position_value = []
for i in half_position:
    half_position_value.append(x[1][i])

mid_compare_position = None
compare = half_position_value
compare.append(max_value)
compare.sort()
for i in range(len(compare)):
    if compare[i]==max_value:
        mid_compare_position = i

fwhm_range = []
fwhm_range.append(compare[mid_compare_position+1])
fwhm_range.append(compare[mid_compare_position-1])

fwhm = fwhm_range[0] - fwhm_range[1]
print("FWHM: " + str(fwhm))

#----------------Plot Line------------------------

plt.axhline(y=max_frequency, color="red", linestyle="dotted")
plt.axhline(y=half_max_freq, color="red", linestyle="dotted")
for i in fwhm_range:
    plt.axvline(x=i, color="red", linestyle="dotted")
plt.show()

#---------------scatter plot----------------
plt.scatter(list(data[5]), list(data[6]))
plt.title("Scatter plot showing position of ions")
plt.xlabel("y-axis")
plt.ylabel("z-axis")
plt.show()

