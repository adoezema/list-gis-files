import argparse
import arcpy
import os
import logging
from pathlib import Path
from rich.logging import RichHandler
from rich.traceback import install
from rich import print
from typing import List, Dict, Set

#Logging Config
install()
logging.basicConfig(level='INFO', format='%(asctime)s - %(message)s',
                        datefmt='[%X]', handlers=[RichHandler(rich_tracebacks=True)])

log = logging.getLogger('rich')

def list_gis_files(directory):
    #TODO: Add docstring
    for dirpath, dirnames, files in arcpy.da.Walk(directory):
        direc = Path(dirpath)
        print(f'Current Dir: {direc.parent.parent.name}\\{direc.parent.name}\\{direc.name}')
        print('\n')
        #TODO: code structure repeats, refactor.
        if dirnames:
            print(f'{" "*3}📁 Directories\Geodatabases\Datasets')
            print(f'{" "*3}{"-"*50}')
            for dir in dirnames:
                print(f'{" "*3}{" "*3} {dir}')
            print('\n')
        if files:
            print(f'{" "*3}📄 Files\Feature Classes\Excel Sheets')
            print(f'{" "*3}{"-"*50}')
            for file in files:
                print(f'{" "*3}{" "*3} {file}')
            print('\n')


def run(arguments):
    log.info(f'[ANALYZING] - {arguments.path}')
    list_gis_files(arguments.path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='List GIS Files in a directory')
    parser.add_argument('-p', dest='path', metavar='path', type=str, help='Input directory')
    args =  parser.parse_args()
    try:
        run(args)
    except Exception as e:
        log.critical("Exception detected, script exiting")
        log.critical(e)