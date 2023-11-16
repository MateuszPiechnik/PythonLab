import os

def fileCounter(directory):
    counter = 0
    for path in os.listdir(directory):
        if os.path.isfile(os.path.join(directory,path)):
            counter +=1
    return counter



dir = 'C:\\Users\\mateu\\practice'
print("Number of files in", dir, ":", fileCounter(dir))