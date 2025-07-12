filename=input("Enter he filename:")
with open(filename) as file:
    text=file.read()
    letter =input("Enter the char:")
    c=0
    for char in text:
        if char==letter:
            c+=1
print(letter,"appears", c ,"items in file")
