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

def run(arguments):
    log.info(arguments.path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='List GIS Files in a directory')
    parser.add_argument('-p', dest='path', metavar='path', type=str, help='Input directory')
    args =  parser.parse_args()
    try:
        run(args)
    except Exception as e:
        log.critical("Exception detected, script exiting")
        log.critical(e)