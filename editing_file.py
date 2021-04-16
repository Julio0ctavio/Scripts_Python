import re
import os

new_file = []

with open("sample.txt", "r") as file:
    for line in file:
        if ("Devs" in line):
            new_line = re.sub("Devs", "DevOps", line)
            new_file.append(new_line)
        else:
            new_file.append(line)

with open("new_sample.txt", "a+") as nfile:
    for line in new_file:
        nfile.write(line)

os.remove("sample.txt")
