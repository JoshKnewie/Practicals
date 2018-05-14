"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import os


def main():
    """Demo of os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Make a new directory
    try:
        os.mkdir('temp')
    except:
        pass

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))

    # Process all subdirectories using os.walk()
    os.chdir('..')  # '..' means to go 'up' one directory
    lyrics_path = os.getcwd()  # store the path so we can get back to it
    for directory_name, subdirectories, filenames in os.walk('.'):
        os.chdir(directory_name)
        print("Current directory is:", os.getcwd())
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))
        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))
            os.rename(filename, new_name)

        os.chdir(lyrics_path)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    for index, character in enumerate(filename):
        if character.islower() and character.isupper():
            filename = filename[index:] + "_" + filename[:index]
        print(filename)

    return new_name


main()
