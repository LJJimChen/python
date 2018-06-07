import os
print os.name
#print os.environ

path1 = os.path.abspath(".")
print path1
dir = os.path.join(path1, "testDir")
print dir
# os.makedirs(dir)

print os.path.split(path1)
print os.path.splitdrive(path1)
print os.path.splitunc(path1)
print os.path.splitext(os.path.join(path1, "test.txt"))

listPaths = os.listdir(path1)
print listPaths
print [p for p in listPaths if os.path.isdir(p)]
