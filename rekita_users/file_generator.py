from os import listdir
from os.path import isfile
import random

p = 'E://Computer engineering//rekiat//web-Uneversity-Task//rekita_users//test_files//'




def random_image(p = 'E://Computer engineering//rekiat//web-Uneversity-Task//rekita_users//test_files//'):
    p = p +'images'
    lst = [f for f in listdir(p)]
    return random.choice(lst)

def random_image_dir(p = 'E://Computer engineering//rekiat//web-Uneversity-Task//rekita_users//test_files//'):
    p += 'images'
    return p +'//'+ random_image()

def random_file(p = 'E://Computer engineering//rekiat//web-Uneversity-Task//rekita_users//test_files//'):
    p+='files'
    lst = [f for f in listdir(p)]
    return random.choice(lst)
def random_file_dir(p = 'E://Computer engineering//rekiat//web-Uneversity-Task//rekita_users//test_files//'):
    p+='files'
    return p + '//' + random_file()
