import os
import shutil

categories = {}
files_types = []
os.chdir('FilesToSort')
for file in os.listdir('.'):
    extention = os.path.splitext(file)[1][1:]
    if extention in categories:
        shutil.move(file, extention)
    else:
        new_key = input("What category would you like to sort {} files into?").format(extention)
        categories[new_key] = extention
        os.mkdir(new_key)

    print(categories)
