with  open("file.txt",'w+') as f:
    f.write("sathya....!....")
    f.seek(0)
    data=f.read()
    print("previous",data)

#with open("file.txt",'r+')as f:
 #   data = f.read()
  #  print("previous",data)
    new_data=data.replace("....!...."," is a goodboy")
    f.seek(0)
    f.write(new_data)
    f.truncate()
with open("file.txt",'r') as f:
    print("Latest",f.read())