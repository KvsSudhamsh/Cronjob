import subprocess
import os
from datetime import datetime

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def readNumber()-> int:
    with open('number.txt', 'r') as f:
        number = int(f.read().strip())
    return number

def writeNumber(n : int)-> None:
    with open('number.txt', 'w') as f:
        f.write(str(n))
    return None

def updateNumber(n:int)-> int:
    return n + 1

def gitCommit():
    pass
    

def main():
    try:
        number = readNumber()
        number = updateNumber(number)
        writeNumber(number)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
