
"""
This is the 'main' file of HALucinator.
MINIMAL code should be added here. This is solely for argument parsing 
for the main halucinator tool.
"""

import sys
import argparse




def main():
    """ Entry point, argument parsing """
    p = ArgumentParser()
    p.add_argument('-c', '--config', dest='config', required=True,
                   help='Configuration file used to run emulation')


    


def rehost():
    """
    Routine that finds the appropriate pieces from sub logic inside 
    the halucinator project, puts them together and runs them.
    """
    pass
