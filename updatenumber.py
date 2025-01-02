import subprocess
import os
from datetime import datetime


def readNumber()-> int:
    with open('number.txt', 'r') as f:
        number = int(f.read().strip())
    return number

def writeNumber(n : int)-> None:
    n += 1
    with open('number.txt', 'w') as f:
        f.write(str(n))
    return None

def gitCommit():
    pass

def main():
    try:
        number = readNumber()
        writeNumber(number)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
