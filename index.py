from time import sleep
import os
os.system('cls' if os.name == 'nt' else 'clear')

def ArchiveExist(arq):
    try:
        a = open(arq, 'rt')
        a.close()

    except FileNotFoundError:
        return False
    
    else:
        return True
    

def CreateArchive(arq):
    try:
        a = open(arq, 'wt+')
        a.close()
    
    except:
        return f'Failed creating {arq}'
    
    else:
        return f'Sucess creating {arq}'


def ReadArchive(arq):
    try:
        with open(arq, 'rt') as file:
            lines = file.readlines()
    
    except FileNotFoundError:
        print(f'{arq} not found.')
        return

    lines.sort(key=lambda line: line.split('-')[0])

    for l in lines:
        data = l.split('-')
        data[1] = data[1].replace('\n', '')
        print(f'{data[0]:<30}{data[1]:>7}')


def AddArchive(arq, name='unknow', chap=0):
    try:
        a = open(arq, 'at')
    
    except:
        print('Add to database is not possible.')
    
    else:
        try:
            a.write(f'{name}-{chap}\n')
        except:
            print('ERRO while adding data to archive.')
        else:
            print(f'{name} registered to database.')
        finally:
            a.close()


def UpdateArchive(arq):
    try:
        with open(arq, 'r') as file:
            lines = file.readlines()
    
    except FileNotFoundError:
        print('Database file not found.')
        return

    name = str(input('Name: ')).strip()
    chap = int(input('New Numeric: '))

    found = False
    
    for i, line in enumerate(lines):
        data = line.split('-')
        if data[0] == name:
            lines[i] = f'{name}-{chap}\n'
            found = True
            print(f'{name} updated to chapter {chap}.')
            break

    if not found:
        print(f'{name} not found in the database.')

    try:
        with open(arq, 'w') as file:
            file.writelines(lines)
    
    except:
        print('Not possible to update the database.')
    
    finally:
        file.close()


def DeleteArchive(arq):
    try:
        with open(arq, 'r') as file:
            lines = file.readlines()
    
    except FileNotFoundError:
        print('Database file not found.')
        return
    
    name = str(input('Name: ')).strip()

    found = False
    for i, line in enumerate(lines):
        data = line.split('-')
        if data[0] == name:
            lines.pop(i)
            found = True
            print(f'{name} deleted from database.')
            break
    
    if not found:
        print(f'{name} not found on database or not possible to delete')

    try:
        with open(arq, 'w') as file:
            file.writelines(lines)
    
    except:
        print('Not possible to update the database.')
    
    finally:
        file.close()


def Menu(parameters):
    c = 1
    print(lin())
    for i in parameters:
        print(f'{c} --- {i}')
        c += 1
    print(lin())


def Option(msg):
    while True:
        try:
            a = int(input(msg))
        
        except (ValueError, TypeError):
            print(f'Please, choose a number in the options.')
            continue
        
        except KeyboardInterrupt:
            print(f"User did not wrote anything.")
            return 0
        
        else:
            return a
    
def lin():
    return '~~' * 18  


archive = 'example1.txt'

if not ArchiveExist(archive):
    CreateArchive(archive)

while True:
    print(lin())
    print(f'COLLETION'.center(5))
    Menu(('View', 'Update Existent', 'Add New', 'Delete', 'Exit'))
    x = Option('Your option: ')
    print('~' * 15)
    
    if x == 1:
        ReadArchive(archive)
        break
     
    elif x == 2:
        UpdateArchive(archive)
    
    elif x == 3:
        name = str(input('Name: ')).strip()
        chap = int(input('Chapter: '))
        AddArchive(archive, name, chap)
    
    elif x == 4:
        DeleteArchive(archive)
    
    elif x == 5:
        print('Exiting...')
        sleep(1.5)
        break
 
    sleep(3.5)

