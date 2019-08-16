#*-* coding: utf-8 *-*
import os
import codecs
import io
import binascii
import chardet

fileToFindWord = '/home/eliezerpires/ld.so.cache'

fileOpen = open(fileToFindWord, 'rb', )
charset = chardet.detect(fileToFindWord)
fileOpen.seek(0,2)
binaryFileOpen = fileOpen.read()
binaryFileOpen = fileOpen.readline()

# asciiFileDecode = binascii.b2
# sizeFile = binaryFileOpen.tell()

codecs.decode(binaryFileOpen, encoding='utf-8', errors='ignore')
print(binaryFileOpen)