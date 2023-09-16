# Ceasar Function 
# which does both encrypt and decrypt
#-----------------------------------

def ceasar (plain_txt, shift, direction):
    ceaser_txt=""
    for char in plain_txt:
        # Code will handle special characters
        if char in alphabet:
            index = alphabet.index(char)
             #print("index of",char," ",index)
            if direction == "encode":
                 index=index + shift
            else:
                 index=index - shift    
                 #print(alphabet[index])
            ceaser_txt += alphabet[index]
        else:
              ceaser_txt += char         
    print (f"Ceasar {direction}d text is :" , " " , ceaser_txt)
        
#Main Block
#-----------
from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
            'v', 'w', 'x', 'y', 'z','!','@','#','$','%','&','*',' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','!','@','#','$','%','&','*',' ']

yesorno = "yes"
while yesorno == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
     
     # for shift greater than 26
     # another to validate saying Shift can be greater than 26
    shift = shift % 26

    ceasar(text, shift, direction)  
    yesorno = input("Type 'yes' to continue , or 'no' to end':\n")
    if yesorno == "no":
        print ("Exited, Good Bye !!! ")
    #else:
    #    continue
    