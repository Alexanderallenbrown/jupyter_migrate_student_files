import os
import shutil

#list of students in NEW course
students = ['bontjen','cumminmj','fiskez','galbrajw','gasparg','steurerg','hurleyr','keanee','olivasm','wengerb']

#what course?
course = 'ES103'

#current home directory
dir_working = os.getcwd()

#directory to hold ALL files before tar
dir_staging = course

#create that directory
if not os.path.exists(dir_staging):
    os.makedirs(dir_staging)

#now set up the directory where all student files live (home)
dir_homeroot = '/home/'

#change to home directory
os.chdir(dir_homeroot)

#now walk through the home directory
for root, dirs, files in os.walk(".", topdown=False):
    for current_dir in dirs:
        for student in students:
            if (student==current_dir and root=='.'):
                print("Found student directory: "+os.path.join(root,current_dir))
		shutil.copytree(os.path.join(root,current_dir),os.path.join(dir_working,dir_staging,student,course))

#now make the archive
os.chdir(dir_working)
shutil.make_archive(course, 'gztar', dir_working)
#now delete the folder
shutil.rmtree(course)
