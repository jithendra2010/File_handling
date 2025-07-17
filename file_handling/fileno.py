'''
f=open("file1.txt",'w')
f.write("Hello")
print(f.isatty())
print(f.fileno())
f.flush()
----------------------------------------------------
'''
import sys
#print("py version:",sys.version)
print("py platform:",sys.platform)