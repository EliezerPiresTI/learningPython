#encoding: utf-8
#!/usr/bin/env python
import os
import re

def is_directory(way_path):
    if(os.path.isdir(way_path)):
        return os.listdir(way_path)
    elif(os.path.isfile(way_path)):
        return way_path
    else:
        print("Essa pasta não existe.")
#tempListDir = ['.system.lock', '.systemRootModFile']    
def browsing_directories(listOfDirectories):
    for unknowElement in listOfDirectories:  #unknowElement = .java #unknowElement = .systemPrefs
        global fullPathDir
        global listDir
        global listFiles
        fullPathDir = fullPathDir + '/' + unknowElement # fullPathDir = /etc/.java #fullPathDir = /etc/.java/.systemPrefs
        if(os.path.isdir(fullPathDir)): # .java é dir #.systemPref é dir
            #fullPathDir = fullPathDir + '/' + unknowElement # fullPathDir = /etc/.java #fullPathDir = /etc/.java/.systemPrefs
            listDir.append(fullPathDir) #listDir = ['/etc/.java'] #listDir = ['/etc/.java/.systemPres']
            # listOfDirectories.remove(unknowElement) # retirar o .java da lista inicial #remove o .systemPrefs
            
            # if(len(os.listdir(fullPathDir))>2 ): #verificando quantos elementos tem dentro de .java #verifica .systemPrefs = 4
            #     tempListDir = is_directory(fullPathDir) #cria lista temporaria de diretórios q tem dentro de .java #cria lista dentro .systemPrefs
            #     print(tempListDir) #tempListDir = ls -la /etc/.java = [.systemPrefs] # tempListDir = ls -la /etc/.java/.systemPrefs = ['.system.lock', '.systemRootModFile']
            #     # browsing_directories(tempListDir) # recursão para tempListDir de .java #recursão para temListDir de .systemPrefs
            fullPathDir = wayDirectorytoFind
        elif(os.path.isfile(fullPathDir)): #/etc/.java/.systemPrefs/.system.lock
            #fullPathDir = fullPathDir + '/' + unknowElement
            listFiles.append(fullPathDir)
            # listOfDirectories.remove(unknowElement)
            fullPathDir = wayDirectorytoFind
def find_word_in_file(listfile, keyWord):
    for rows in listfile:
        if (keyWords in rows): 
            print("Path founded->", fileToFindWord)
            print("Keyword founded->".format(), rows)

global fullPathDir 
global listDir
global listFiles
os.system("clear")
print("--------------------------------------------------------------------------------------------------")
print("This software is used to find keywords inside of files.")
print("Enter the path you would like to search or search all the system directories tree.  ")
print("--------------------------------------------------------------------------------------------------")
print("Esse programa serve para localizar palavras chaves dentro de arquivos.")
print("Podendo colocar o diretório que gostaria de pesquisar ou pesquisando em toda a arvore de diretórios do sistema.")
print("--------------------------------------------------------------------------------------------------")

ContinueBreak = True
while ContinueBreak:
    print("Deseja pesquisar a palavra chave em um arquivo ou em uma árvore de diretórios? ")
    print("1 - Único Arquivo; 2 - Árvore de Diretórios; 3 - Encerrar Programa;")
    option = input()
    if(option == '1'):
        wayDirectorytoFind = input("Digite o caminho do arquivo em que você gostaria de pesquisar: ")
        fileName = input("Digite o Nome do Arquivo em que gostaria de pesquisar: ")
        keyWords = input("Digite a Palavra Chave que quer encontrar: ")
        if(os.path.exists(wayDirectorytoFind)):
            filePathComplete = wayDirectorytoFind + fileName
            if(os.path.isfile(filePathComplete)):
                fileOpen = open(filePathComplete, 'r')
                fileSplitRows = fileOpen.readlines()
                find_word_in_file(fileSplitRows, keyWords)
            else:
                print("This file don't exist. Please insert valid file")
        else:
            print("This path don't exist. Enter an exist path.")
    elif(option == '2'):
        listDir = []
        listFiles = []
        wayDirectorytoFind = input("Digite o caminho do diretório em que você gostaria de pesquisar: ")
        keyWords = input("Digite a palavra chave: ")
        listOfElements = is_directory(wayDirectorytoFind)
        listOfElements.sort()
        fullPathDir = wayDirectorytoFind #/etc/
        browsing_directories(listOfElements)
        for direc in listDir:
            wayDirectorytoFind = direc + '/'
            fullPathDir = wayDirectorytoFind
            listSubdirectorieFile = is_directory(wayDirectorytoFind)
            browsing_directories(listSubdirectorieFile)
        for fileToFindWord in listFiles:
            fileOpen = open(fileToFindWord, 'r')
            fileSplitRows = fileOpen.readlines()
            find_word_in_file(fileSplitRows, keyWords)
    elif(option == '3'):
        ContinueBreak = False
    else:
        print("Opção Inválida")