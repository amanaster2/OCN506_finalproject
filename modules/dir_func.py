"""
Purpose: Function to create output folder if one doesn't
already exist.
"""
import os, sys, shutil
import numpy as np

shared_pth = os.path.dirname(os.path.realpath(__file__))

def make_dir(dirname, clean=False):
    """
    Make a directory if it does not exist.
    Use clean=True to clobber the existing directory.
    """
    if clean == True:
        shutil.rmtree(dirname, ignore_errors=True)
        os.mkdir(dirname)
    else:
        try:
            os.mkdir(dirname)
        except OSError:
            pass # assume OSError was raised because directory already exists
            
def get_outdir():
    """
    Find the absolute path to the output directory.
    
    ASSUMES we are working in the main directory,
    e.g. we are in .../OCN506_finalproject/ and it will return:
    ('OCN506_finalproject', '/Users/Amanda/Documents/GitHub/OCN506_finalproject/output')
    """
    this_parent = shared_pth.split('/')[-2]
    out_dir = os.path.abspath('../'+this_parent) + '/output/'
    return  this_parent, out_dir

#this_parent, out_dir = get_outdir()
#make_dir(out_dir)