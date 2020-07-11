import os


directory = r'cuefc\static'
piclist = []
for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        piclist.append(filename)
    else:
        continue
print(piclist)

