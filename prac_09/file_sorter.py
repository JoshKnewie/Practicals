import os
import shutil

categories = {}
files_types = []
for file in os.listdir('.'):
    extention = file.split(".", 1)[1]
    if extention in categories:
        pass
    else:
        new_key = input("What category would you like to sort doc files into?")
        categories[new_key] = extention
        # os.mkdir(extention)
    # shutil.move(file, extention)
    print(categories)
