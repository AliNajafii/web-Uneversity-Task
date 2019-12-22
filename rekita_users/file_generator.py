from os import listdir
from os.path import isfile
from project import settings
import random
import os

base_dir = settings.BASE_DIR
users_file = os.path.join(base_dir,'rekita_users')
files_dir = os.path.join(users_file,'test_files')



def random_image(path):
    p = p +'images'
    lst = [f for f in listdir(p)]
    return random.choice(lst)

def random_image_dir(path):
    p += 'images'
    return p +'//'+ random_image()

def random_file(path):
    p+='files'
    lst = [f for f in listdir(p)]
    return random.choice(lst)
def random_file_dir(path):
    p+='files'
    return p + '//' + random_file()
