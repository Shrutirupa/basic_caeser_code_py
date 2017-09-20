import sys

txt=raw_input("enter your cipher text \n")

if(txt.isupper()):
    for key in range(1,27): #the range can be changed accordingly
        for i in txt:
            asc=ord(i)-65
            decrp=((asc-key)%26)+65
            sys.stdout.write(chr(decrp))
        print("")
if(txt.islower()):
    for key in range(1,27):
        for i in txt:
            asc=ord(i)-97
            decrp=((asc-key)%26)+97
            sys.stdout.write(chr(decrp))
        print("")
