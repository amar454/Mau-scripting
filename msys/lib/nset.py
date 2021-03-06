"""
nset function and dependencies in mau
Amar Djulovic and others
2020
"""
import os


def usrname(userNameFinal, rootDir, posixfinder):
    # nset usrname
    with open(f'{rootDir}/msys/nml/username.txt' if posixfinder else f'{rootDir}\\msys\\nml\\username.txt', 'w+') as f:
        f.truncate(0)
        f.write(userNameFinal)
        return None


def cmpname(compnamefinal, rootDir, posixfinder):
    with open(f'{rootDir}/msys/nml/computername.txt' if posixfinder else f'{rootDir}\\msys\\nml\\computername.txt', 'w+') as f:
        f.truncate(0)
        f.write(compnamefinal)
        return None


def nsmain(commandList, posixfinder):
    if len(commandList) == 1:
        return None
    elif commandList[1] == 'usrname':
        if len(commandList) == 3:
            usrname(commandList[2], os.path.dirname(os.path.abspath(__file__)), posixfinder)
    elif commandList[1] == 'cmpname':
        if len(commandList) == 3:
            cmpname(commandList[2], os.path.dirname(os.path.abspath(__file__)), posixfinder)
        elif len(commandList) == 2:
            if commandList[1] == '--help':
                return None
            else:
                return print(f'{commandList[0]}: {commandList[1]}: expected argument(s) after cmpname')
