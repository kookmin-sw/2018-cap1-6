import zipfile
import os
import shutil

home = os.path.expanduser("~")

def unzip(name):
    fname = home + '/files/' + name + '.zip'
    fantasy_zip = zipfile.ZipFile(fname)
    fantasy_zip.extractall(home + '/files/' + name)
    fantasy_zip.close()

