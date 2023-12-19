import os as s

file = s.listdir("ToEditFolder")
print(file)
j = 1
for i in file:
    
    if i.endswith(".png"):
        s.rename(f"ToEditFolder/{i}", f"ToEditFolder/{j}.png")
        j = j + 1