byte= b"E\x00\x00A\x99\x1f\x00\x00\x80\x11\x00\x00\n\x00\x02\x0f\xc0\xa8\x01\x01\xef\x97\x005\x00-\xcd\xf62`\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x05fp-vp\tazureedge\x03net\x00\x00\x01\x00\x01"

print("Converts byte to Hex: ", byte.hex())
print("Converts Hex to str: ", byte.fromhex(byte.hex()).decode('utf-8'))

byte =  b'\xce\x9c\xce\xb9\xce\xb1 \xce\xb3\xcf\x81\xce\xae\xce\xb3\xce\xbf\xcf\x81\xce\xb7 \xce\xba\xce\xb1\xcf\x86\xce\xad \xce\xb1\xce\xbb\xce\xb5\xcf\x80\xce\xbf\xcf\x8d'

print("Converts byte to Hex: ", byte.hex())
print("Converts Hex to str: ", byte.fromhex(byte.hex()).decode('utf-8'))