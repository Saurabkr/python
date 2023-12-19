import os as s

if not s.path.exists("Variable"):
 s.makedirs("Variable")

# To make folder and rename it
for i in range(10):
    # s.makedirs(f'Variable/tutorial {i+1}')
    s.rename(f'Variable/tutorial {i+1}', f'Variable/tut{i+1}')


# To print all folders list

folders = s.listdir("Variable")
print(folders)

# give file inside folder
for i in folders:
    print(i)
    print(s.listdir(f'Variable/{i}'))

# to get current working dir
print(s.getcwd())

# we can only remove empty folders
for i in range(10):
  s.rmdir(f'Variable/tutorial{i+1}')