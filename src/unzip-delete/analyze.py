import os

home = os.path.expanduser("~")
gipath = os.getcwd() + '/gitinspector/gitinspector.py'
# name = 'kookmin-sw_2018-cap1-6_branch_master'

def analyze(name):
    fpath = home + '/files/' + name
    fname = name + '.html' 
    order = gipath + ' ' + fpath + ' -F html --grading > ' + home + '/files/html/' + fname

    try:
        os.system(order)
    except OSError as e:
        print(e)

if __name__ == "__main__":
    analyze(name)
