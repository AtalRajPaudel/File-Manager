import os

current_directory = os.getcwd()
print(f"This is my current directory : {current_directory}")


# This a function to list the files in the directory
def list_files(directory):
    try:
        files = os.listdir(directory)
        print(f"Files in {directory}")
        for file in files:
            print(file)
    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist")
    
    except Exception as e:
        print(f"An error occured: {e}")

# This is a function to create the files in the directory
def create_directory(directory_path):
    try:
        os.mkdir(directory_path)
        print(f"Directory '{directory_path}' created successfully")
    except FileExistsError:
        print(f"Directory '{directory_path}' already exists")
    except Exception as e:
        print(f"An error occured: {e}")

# to create a file in python
file = open('../trial/trial.txt','a+')
file.write("Test Test once twice i dont know just count the lines okay")
file.close()
###

## to rename a file 
def rename_file(current_name, new_name):
    try:
        os.rename(current_name, new_name)
        print(f"File renamed from '{current_name}' to '{new_name}'.")
    except FileNotFoundError:
        print(f"The file '{current_name}' does not exist")
    except Exception as e:
        print(f"An error occured : {e}")


##to delete a file
def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully")
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist")
    except Exception as e:
        print(f"An error occured: {e}")


## to delete a directory  but the directory must be empty
def delete_directory(directory_path):
    try:
        os.rmdir(directory_path)
        print(f"The directory '{directory_path}' has been removed")
    except FileNotFoundError:
        print(f"The directory '{directory_path}' does not exist")
    except OSError:
        print(f"The directory '{directory_path}' is not empty or cannot be deleted")
    except Exception as e:
        print(f"An error occured: {e}")



#Example usage for the creation of directory
directory = input("Enter the path where you want to create a new directory: ")
new_directory_name = input("Enter the name of the new directory: ")
new_directory_path = os.path.join(directory, new_directory_name)
create_directory(new_directory_path)

    
directory = input("Enter the directory path: ")
list_files(directory)


## for renaming a file 
current_file = input ("Enter the curent file name with the path: ")
new_file_name = input ("Enter the new name for the file: ")
rename_file(current_file, new_file_name)


# for deleting a file 
file_to_delete  = input("Enter the file path to delete: ")
delete_file(file_to_delete)

##for deleting a directory
delete_the_directory = input(f"Enter the file path of the directory you want to remove : ")
delete_directory(delete_the_directory)