import subprocess
import os
from datetime import datetime
from log import logger

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

log = logger(__name__)

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

def gitCommit()-> None:
    subprocess.run(['git', 'add', 'number.txt'])
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    commitMessage = f"Update number : {date}"
    subprocess.run(['git', 'commit', '-m', commitMessage])
    return None
    

def main():
    try:
        number = readNumber()
        log.info(f"number: {number}")
        number = updateNumber(number)
        writeNumber(number)
        gitCommit()
    except Exception as e:
        log.info(f"Error:{e}")

if __name__ == '__main__':
    main()
