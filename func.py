import os

def find_main(directory,houzhui,):  
    for root, dirs, files in os.walk(directory):  
        if 'main.java' in files:  
            return os.path.join(root, f'main.{houzhui}')  
    return None 