import os

def showPaths(directory):
    for path in os.listdir(directory):
        fullPath = os.path.join(directory, path)
        if os.path.isdir(fullPath):
            showPaths(fullPath)
        else:
            print(fullPath)

dir = dir = 'C:\\Users\\mateu\\practice'
showPaths(dir)