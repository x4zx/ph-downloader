import sys
from core import download


def main():

    value = input('Enter video/playlist link: ')
    if not value:
        sys.exit()
    
    else:
        download(value)


if __name__ ==  '__main__':
    main()