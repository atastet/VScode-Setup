# coding: utf-8

import os #Interact with th system

def launch_analysis(data_file):
    directory = os.path.dirname(os.path.dirname(__file__)) # On obtient le path de notre projet
    path_to_file = os.path.join(directory, "data", data_file) #On va dans data et on récupère le fichier
    
    with open(path_to_file,'r') as file:
        preview = file.readline()

    print("Read the first line \n {}".format(preview))

def main():
    launch_analysis('current_mps.csv')

if __name__ == "__main__":
    main()
