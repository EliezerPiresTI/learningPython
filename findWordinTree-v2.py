#!/usr/bin/env python
#*-* coding: utf-8 *-*
import os
import re
import chardet
import codecs

def is_directory(way_path):
    if(os.path.isdir(way_path)):
        return os.listdir(way_path)
    elif(os.path.isfile(way_path)):
        return way_path
    else:
        print("Essa pasta não existe.")
def browsing_directories(listOfDirectories):
    for unknowElement in listOfDirectories:
        global fullPathDir
        global listDir
        global listFiles
        fullPathDir = fullPathDir + '/' + unknowElement
        if(os.path.isdir(fullPathDir)):
            listDir.append(fullPathDir)
            fullPathDir = wayDirectorytoFind
        elif(os.path.isfile(fullPathDir)):
            listFiles.append(fullPathDir)
            fullPathDir = wayDirectorytoFind
def find_word_in_file(listfile, keyWord):
    for rows in listfile:
        if (keyWords in rows): 
            print(30*"-----")
            print("Path founded->", fileToFindWord)
            print("Keyword founded->".format(), rows)
            print(30*"-----")

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
            fileToFindWord = wayDirectorytoFind + fileName
            if(os.path.isfile(fileToFindWord)):
                fileOpen = open(fileToFindWord, 'r')
                fileSplitRows = fileOpen.readlines()
                find_word_in_file(fileSplitRows, keyWords)
                fileOpen.close()
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
        fullPathDir = wayDirectorytoFind
        browsing_directories(listOfElements)
        for direc in listDir:
            wayDirectorytoFind = direc + '/'
            fullPathDir = wayDirectorytoFind
            listSubdirectorieFile = is_directory(wayDirectorytoFind)
            browsing_directories(listSubdirectorieFile)
        for fileToFindWord in listFiles:
            try:
                fileOpen = open(fileToFindWord, 'r')
                fileSplitRows = fileOpen.readlines()
                fileOpen.close()
            except (UnicodeDecodeError, UnicodeEncodeError, UnicodeError):
                binaryFileOpen = open(fileToFindWord, 'rb')
                binaryFileOpen = binaryFileOpen.read()
                charsetsFile = chardet.detect(binaryFileOpen)
                newFileUtf8 = codecs.decode(binaryFileOpen, charsetsFile['encoding'], 'ignore')
                
                binaryFileOpen.close()
                fileSplitRows = newFileUtf8.readlines()
            else:
                pass
            find_word_in_file(fileSplitRows, keyWords)
            
    elif(option == '3'):
        ContinueBreak = False
    else:
        print("Opção Inválida")