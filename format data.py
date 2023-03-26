name = "Hydrogen in Zinc.txt"

text = str(open(name, "r").read())
text = text.replace("    ", "\t")
text = text.replace("   ", "\t")
text = text.replace("  ", "\t")
text = text.replace(" ", "\t")

file = open(name, "w")
file.write(text)
file.close()