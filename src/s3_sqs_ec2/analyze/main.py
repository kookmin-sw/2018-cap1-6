from analyze import analyze
from unzip import unzip
from delete import delete

# name = 'kookmin-sw_2018-cap1-6_branch_master'

def main(name):
    unzip(name)
    print(name+" unzip completed")
    analyze(name)
    print(name+" analyze completed")
    delete(name)
    print(name+" delete completed")


if __name__ == "__main__":
    main(name)
