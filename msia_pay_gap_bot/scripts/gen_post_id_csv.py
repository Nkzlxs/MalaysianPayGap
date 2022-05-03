import os
import sys

unique_file_names = []
for f in os.listdir(sys.argv[1]):
    f = f.split(".")[0]
    if f != "":
        unique_file_names.append(f)

unique_file_names = list(set(unique_file_names))
with open("posts.csv","w") as f:
    f.write(",".join(unique_file_names))