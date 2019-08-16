import binascii
import chardet
import io
import os

# main_ctrlO = bytearray()

main_ctrl0 = io.BytesIO()

binfile = open("binfile.bin", "wb")
binfile.write(b'7F45 4C46 0102 0100 0000 0000 0000 0000 0001 0014 0000 0001 0000 0000 0000')
binfile.close()
binfile = open("binfile.bin", "rb")

# main_ctrl0.write('7F45 4C46 0102 0100 0000 0000 0000 0000 0001 0014 0000 0001 0000 0000 0000'.encode('UTF-8'))
# main_ctrl0.seek(0)
# result = main_ctrl0.read()
# print(result)
# chardet.detect()



