#! /usr/bin/env python3
# coding: utf-8

import analysis.csv as c_an
import analysis.xml as x_an
import argparse

# Helps to read arguments in order to select an extension
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--extension", help="""Type of file to analyse. XML or CVS ?""")
    return parser.parse_args()

def main():
    args = parse_arguments()
    if args.extension == 'csv':
        c_an.launch_analysis('current_mps.cv')
    elif args.extension == 'xml':
        x_an.launch_analysis('SyceronBrut.xml')

if __name__== "__main__":
    main()
