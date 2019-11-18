# coding: utf-8

import os #Interact with th system
import logging as lg

lg.basicConfig(level=lg.DEBUG)

def launch_analysis(data_file):
    directory = os.path.dirname(os.path.dirname(__file__)) # On obtient le path de notre projet
    path_to_file = os.path.join(directory, "data", data_file) #On va dans data et on récupère le fichier
    
    try:
        with open(path_to_file,'r') as file:
            preview = file.readline()
        lg.debug('Read the first line \n {}'.format(preview))
    except:
        lg.critical('File not found')

def main():
    launch_analysis('current_mps.csv')

if __name__ == "__main__":
    main()
