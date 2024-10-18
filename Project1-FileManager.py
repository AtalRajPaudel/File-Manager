import os
import shutil
import time
import zipfile

##Defining the functions
## to know current directory
def current_directory():
    current_directory = os.getcwd()
    print(f"You are in '{current_directory}' directory.")

##to list all the files and folders in the current directory
def list_directory(directory_path):
    try:
        files = os.listdir(directory_path)
        for file in files:
            print(file)
        print(f"The files in the directory '{directory_path}' have been listed")
    except FileNotFoundError:
        print(f"The directory '{directory_path}' does not exist")
    except Exception as e:
        print(f"An error occured. {e}")


## To create directories in a certain path
def create_directory(directory_path):
    try:
        os.mkdir(directory_path)
        print(f"A directory is created in '{directory_path}'")
    except FileExistsError:
        print(f"A directory already exists in the path '{directory_path}'")
    except Exception as e:
        print(f"An error occured {e}")


## To create a file
def create_file(file_name):
    try:
        file = open(file_name,"a+")
        file.write("This is new line in python file program")
        file.close()
        print(f"The file has been created with name '{file_name}'")
    except Exception as e:
        print(f"An error occured. {e}")
    

###to rename a file 
def rename_file(current_name, new_name):
    try:
        os.rename(current_name, new_name)
        print(f"File name changed from '{current_name}' to '{new_name}'")
    except FileNotFoundError:
        print(f"File is not found in the directory path : '{current_name}'")
    except Exception as e:
        print(f"An error occured {e}")


## To delete a file
def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"File deleted in the file path  '{file_path}")
    except FileNotFoundError:
        print(f"The file does not exist in the '{file_path}'")
    except Exception as e:
        print(f"An error occured {e}")

### To delete a directory. Also the directory must be empty to be deleted
def delete_directory(directory_path):
    try:
        os.rmdir(directory_path)
        print(f"The directory has been deleted from path '{directory_path}")
    except FileNotFoundError:
        print(f"The file does not exist in the path '{directory_path}")
    except OSError:
        print(f"The directory '{directory_path}' is not empty or cannot be deleted")
    except Exception as e:
        print(f"An error occured {e}")

### To copy files and folder
def copy_file(source,destination):
    try:
        shutil.copy(source, destination)
        print(f"The file is copied from '{source}' to '{destination}'")
    except Exception as e:
        print(f"An error occured {e}")

## to copy folder from one place to another
def copy_directories(source, destination):
    try:
        shutil.copytree(source, destination)
        print(f"Folder successfully copied from '{source}' to '{destination}'.")
    except FileExistsError:
        print(f"The file already exists in the '{destination}'.")
    except Exception as e:
        print(f"An error occured: {e}")

#to move file from one place to another
def move_file_directory(source,destination):
    try:
        shutil.move(source,destination)
        print(f"File successfully moved from '{source}' to '{destination}'.")
    except FileExistsError:
        print(f"File already exists in the destination: {destination}.")
    except exception as e:
        print(f"An error occured.'{e}')

#To check disk usage of the folder or file
def check_disk_usage(path):
    usage = shutil.disk_usage(path)
    print(f"Total Space : {usage.total//(1024**3)} GB")
    print(f" Used: {usage.used//(1024 ** 3)} GB")
    print(f" Free Space : {usage.free // (1024 ** 3)} GB") 

#To get file properties like creation time, file size and modified time of the file
def get_file_properties(file_path):
    try:
        stats = os.stats(file_path)
        print(f"File Size: {stats.st_size}")
        print(f"File Creation: {time.ctime(stats.st_ctime)}")
        ###The os.stats(file path).st_ctime behaves differently in different operating system.
        ## In UNIX it gives the time when the files metadata(permission,ownership) was changed.
        ### IN windows it gives the time when the file was created since the epoch.
        print(f"File Modified: {time.ctime(stats.st_mtime)}")
    except FileNotFoundError:
        print(f"The file does not exists in the location '{file_path}'.")
    except Exception as e:
        print(f"An error occured {e}")


## to view file content
def view_file_content(file_path):
    with open("file_path",'r') as file:
        print(file.read())
    except FileNotFoundError:
        print(f"The file in the path '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occured. {e}")

###To zip a file or directory
def zip_file_directory(name,source):
    try:
        shutil.make_archive(name,'zip',source)
        print(f"The file at '{source}' has been zipped at '{name}.zip'")
    except Exception as e:
        print(f"An error occured: {e}")

###To unzip a file or directory
def unzip_directory(zip_path, extract_to):
try:
    with zipfile.zipFile(zip_path,'r') as zip_ref:
        zip_ref.extractall(extract_to)
        print(f"The zip file from {zip_path} has been extracted to {extract_to}")
except Exception as e:
    print(f"An error occured. {e}")
        

## now creating a switch statement to do all the tasks as demanded by the user
def File_Manager(run):
    while run:
        print(f" Hii ! This is a File Manager")
        print(f"What would you like to do today? \n")
        print("1. Know your current directory")
        print("2. List the current directory")
        print("3. Create a directory")
        print("4. Remove a directory")
        print("5. Create a file")
        print("6. Remove a file")
        print("7. Rename a file")
        print("8. Copy file from one folder to another")
        print("9. Copy a folder from one place to another")
        print("10. Move a folder or file from one place to another")
        print("11. Check disk usage of a file or a folder")
        print("12. Get File properties")
        print("13. to view file content")
        print("14. to zip a file or a directory")
        print("15. EXIT")

        print("Choose from 1-7")
        choice = input("You would like to : ")

        if choice == '1':
            current_directory()
            
        elif choice == '2':
            to_list_directory = input(f"Enter the directory path: ")
            list_directory(to_list_directory)
            
        elif choice == '3':
            directory_name = input("Enter the directory name : ")
            directory_path = input("Enter the path of the directory: ")
            new_directory_path = os.path.join(directory_path, directory_name)
            create_directory(new_directory_path)
            
        elif choice == '4':
            to_delete_directory = input("Enter the path of the directory along with the name: ")
            delete_directory(to_delete_directory)
            
        elif choice == '5':
            file_path = input("Enter the path of the directory: ")
            file_name = input("Enter the name of the file to create: ")
            new_file_path = os.path.join(file_path, file_name)
            create_file(new_file_path)
            
        elif choice == '6':
            file_to_delete = input("Enter the file path: ")
            delete_file(file_to_delete)
            
        elif choice == '7':
            rename_file_path = input("Enter the file path: ")
            current_name = input("Enter the current name of the file: ")
            new_name = input("Enter the new name of the file: ")
            current_name = os.path.join(rename_file_path, current_name)
            new_name = os.path.join(rename_file_path, new_name)
            rename_file(current_name, new_name)

        elif choice == '8':
            copy_file = input("Enter the source from which to copy: ")
            copy_file_destination = input("Enter the destination of the file: ")
            copy_file(copy_file, copy_file_destination)

        elif choice == '9':
            copy_directory = input("Enter the source of the directory: ")
            copy_directory_destination = input("Enter the destination of the directory: ")
            copy_directories( copy_directory, copy_directory_destination)

        elif choice == '10':
            move_fof = input("Enter the source of the file or folder: ") ###fof means file or folder
            move_fof_to = input("Enter the destination of the file or folder: ")
            move_file_directory(move_fof, move_fof_to)

        elif choice == '11':
            usage_path = input("Enter the path of the file: ")
            check_disk_usage(usage_path)
            
        elif choice == '12':
            file_properties_path = input("Enter the path of the file: ")
            get_file_properties(file_properties_path)
            
        elif choice == '13':
            file_view = input("Enter the path of the file: ")
            view_file_content(file_view)
            
        elif choice == '14':
            zip_name = input("Enter the name of the file: ")
            zip_source = input("Enter the path of the file: ")
            Zip_file_directory(zip_name, zip_source)

        elif choice == '15':
            run = False
        else:
            run = True


            

        
run = True
File_Manager(run)

