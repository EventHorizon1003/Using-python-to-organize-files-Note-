# Note of Organizing files
#----------------------------------------------------------------
import shutil,os
# Introduce shutil module - shell utilities
# -let you copy, move, rename, delete files

# Copying files and folders -> shutil.copy(<source>,<destination>)
# *** the path must be in strings
    # copy an entire folder -> shutil.copytree()

# Moving and Renaming files -> shutil.move(<source>,<destination>)

# Permanently deleting file and folders -> os module
#   1) os.unlink(<path>) -> delete the file
#   2) os.rmdir(<path>) -> delete the folder
#   3) shutil.rmtree(<path>) -> will permanently delete the folder and all files it contain

# Safe delete -> send2trash module
import send2trash
# eg: send2trash.send2trash('bacon.txt')

# Waling a diretory tree -> os.walk()
# See the notefunction0 (be careful , that is a lot of output!!!)
# More detail of os.walk() -> notefunction1
#   1) the first list is the name of the file
#   2) the second list is the folder
#   3) the third list is the file
#   when looping the os.walk() will access each file folder in the root of the path

#------------------------------------------------------------------------
import zipfile
# Compressing files -> zipfile module
# We can use the Python to open / create the ZIP files
# See notefunction2
#   To read the contents of zipfile , u must create a zipfile object
#   Create the zipfile obj  -> zipfile.ZipFile(<zipfile name>)
#       zipobj.namelist() : show the list of files and folder
#       a = zipobj.getinfo(<content>)
#       a.file_size  /  a.compress_size
# Extracting from Zip files -> extractall() / extract(<filename>,<destination>)

# Creating and adding Zip files -> zipfile.ZipFile('<name>','w')
# eg: zipobj = zipfile.ZipFile('new.zip','w')
#     zipobj.write('dota_mmr.py', compress_type=zipfile.ZIP_DEFLATED)
#     zipobj.close()
#     compress_type=zipfile.ZIP_DEFLATED is typical compression algorithm ...
#     It works well on all types of data
# See the notefunction3

def notefunction0() :
    a = os.getcwd()
    print("the example of cwd ")
    for folderName , subfolders, filenames in os.walk(a) :
        print('The current file is' + folderName)
        for subfolder in subfolders:
            print("Subfolder of " + folderName+ ":" +subfolder)
        for filename in filenames:
            print('File Inside ' + folderName +':' +filename)
        space()
    print("the example of desktop")
    for folderName , subfolders, filenames in os.walk("C:\\Users\\ACER\\Desktop") :
        print('The current file is' + folderName)
        for subfolder in subfolders:
            print("Subfolder of " + folderName+ ":" +subfolder)
        for filename in filenames:
            print('File Inside ' + folderName +':' +filename)
        space()

def notefunction1() :
    m = 0
    for a, b, c  in os.walk('C:\\Users\\ACER\\Desktop'):
        print(a)
        space()
        print(b)
        space()
        print(c)
        m += 1
        if m == 3:
            break

def notefunction2() :
    example = zipfile.ZipFile('sample.zip')
    print(example.namelist())
    a = example.getinfo('day 3.jpg')
    print('compressed file is %sx smaller' %(round(a.file_size/a.compress_size,2)))
    example.close()

def notefunction3() :
    a = os.getcwd()
    b = a
    a += '\\dota_mmr.py'
    b += '\\new.zip'
    zipobj = zipfile.ZipFile(b,'w')
    zipobj.write(a,compress_type=zipfile.ZIP_DEFLATED)
    zipobj.close()

def space():
    print('')
def cwd() :
    print(os.getcwd())
def new_note(n):
    if n == '0' :
        notefunction0()
    elif n == '1' :

        notefunction1()
    elif n == '2' :
        notefunction2()
    elif n == '3' :
        notefunction3()
    elif n == 'cwd' :
        cwd()
#Loop
while True :
    print("What example you want me to show ?")
    num = input()
    new_note(num)