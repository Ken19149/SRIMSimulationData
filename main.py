import pandas as pd
import numpy as np

'''
text = str(open("Carbon.txt", "r").read())
text = text.replace("    ", "\t")
text = text.replace("   ", "\t")
text = text.replace("  ", "\t")
text = text.replace(" ", "\t")
'''

txt = pd.read_csv("TRIMOUT-Fe1.txt", sep="\t", header=None)
avg = np.mean(txt[3])
print(avg/1000000, "MeV")
