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
    pass

if __name__ == "__main__":
    run()
