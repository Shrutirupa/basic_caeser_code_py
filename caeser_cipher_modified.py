
#caeser_cipher
import sys
print("what do you want to perform??")
input1=raw_input("press E for encryption and D for decryption \n")

if (input1=="E".strip() or input1=="e".strip()):
    txt1=raw_input("enter your text \n")
    key1=4#input("what is your key \n")
    if (txt1.isupper()):            
        for i in txt1:
            asc=ord(i)-65
            encrp=((asc+key1)%26)+65
            sys.stdout.write(chr(encrp))
        
    else:
        for j in txt1:              
            asc=ord(j)-97
            encrp=((asc+key1)%26)+97
            sys.stdout.write(chr(encrp))

else:
    txt2=raw_input("enter your cipher text: \n")
    key2=input("what is the key length \n")
    if (txt2.isupper()):            
        for i in txt2:
            asc=ord(i)-65
            decrp=((asc-key2)%26)+65
            sys.stdout.write(chr(decrp))
        
    else:
        for j in txt2:              
            asc=ord(j)-97
            decrp=((asc-key2)%26)+97
            sys.stdout.write(chr(decrp))

    
