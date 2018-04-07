import zipfile
import os
import shutil

home = os.path.expanduser('~')
def unzip(name):
    zname = home + '/files/' + name + '.zip'
    fname = home + '/files/' + name
    fantasy_zip = zipfile.ZipFile(zname)
    fantasy_zip.extractall(fname)
    fantasy_zip.close()

