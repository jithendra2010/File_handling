file=open("t.bin","wb")
data= b' \x48\x65\x6c\x6c\x6f'
file.write(data)
file.close()