import os,shutil

def move(src,fName,dest):
    shutil.move(src + fName,dest)
    return 'File moved'

def newName(src,fName,dest):
    print(os.listdir(dest))
    newName = input(f'provide a alternate name for {fName} :')
    shutil.move(src + fName,dest + newName)
    
def check(fName,dest):
    if not os.path.exists(dest + fName):
        return True
    else:
        return False

dirDict = {
    'inputDirList' : 'D:\Python project\inputs\\',
    'doc' : 'D:\Python project\organized files\Documents\\',
    'img' : 'D:\Python project\organized files\Images\\',
    'mp3' : 'D:\Python project\organized files\Music\\',
    'mp4' : 'D:\Python project\organized files\Videos\\',
    'misc' : 'D:\Python project\organized files\Others\\'
}

for file in os.listdir(dirDict['inputDirList']):
    if file.endswith('.txt') or file.endswith('.pdf'):
        if check(file,dirDict['doc']) == True:
            print(move(dirDict['inputDirList'],file,dirDict['doc']))
        else:
            newName(dirDict['inputDirList'],file,dirDict['doc'])

    elif file.endswith('.jpg') or file.endswith('.jpeg'):
        if check(file,dirDict['img']) == True:
            print(move(dirDict['inputDirList'],file,dirDict['img']))
        else:
            newName(dirDict['inputDirList'],file,dirDict['img'])

    elif file.endswith('.mp3'):
        if check(file,dirDict['mp3']) == True:
            print(move(dirDict['inputDirList'],file,dirDict['mp3']))
        else:
            newName(dirDict['inputDirList'],file,dirDict['mp3'])

    elif file.endswith('.mp4') or file.endswith('.mkv'):
        if check(file,dirDict['mp4']) == True:
            print(move(dirDict['inputDirList'],file,dirDict['mp4']))
        else:
            newName(dirDict['inputDirList'],file,dirDict['mp4'])
            
    else:
        if check(file,dirDict['misc']) == True:
            print(move(dirDict['inputDirList'],file,dirDict['misc']))
        else:
            newName(dirDict['inputDirList'],file,dirDict['misc'])