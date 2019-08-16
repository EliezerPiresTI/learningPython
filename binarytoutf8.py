#*-* coding: utf-8 *-*
import codecs

fileToFindWord = '/home/eliezerpires/mgca/main_ctrl.O'
binaryFileOpen = open(fileToFindWord, 'rb')
binaryFileOpen = binaryFileOpen.read()
new_binaryDecode = codecs.decode(binaryFileOpen, encoding='utf-8', errors='ignore')
print(new_binaryDecode)


# newFileUtf8 = codecs.decode(binaryFileOpen, charset['encoding'], 'strict')
# print(newFileUtf8)
# binaryFileOpen.close()