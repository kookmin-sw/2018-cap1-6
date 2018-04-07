import shutil
import os

home = os.path.expanduser("~")

def delete(name):
    fname = home + '/files/' + name
    zname = home + '/files/' + name + '.zip'

    shutil.rmtree(fname)
    os.remove(zname)
