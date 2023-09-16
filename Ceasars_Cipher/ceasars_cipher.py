# Encrypt Function 
#--------------------
def encrypt(plain_text,shift_amount):
    var_txt = plain_text
    index = 0
    encrypted_txt= []
    for char in var_txt:
        index = alphabet.index(char)
        #print("index of",char," ",index)
        index=index + shift
        #print(alphabet[index])
        encrypted_txt.append(alphabet[index])
    var_encypted_join = ' '.join(encrypted_txt)
    var_encypted_str_wos = var_encypted_join.replace(" ", "")
    print ("encrypted_txt:" , " " , var_encypted_str_wos)

# Decrypt Function 
#--------------------

def decrypt(encrypyted_txt,encrypted_shift):
    decrypted_txt=""
    for char in encrypyted_txt:
         index = alphabet.index(char)
         #print("index of",char," ",index)
         index=index - shift
         #print(alphabet[index])
         decrypted_txt += alphabet[index]
    print ("decrypted_txt:" , " " , decrypted_txt)
        
#Main Block
#-----------
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


if direction == "encode":
    encrypt(text,shift)
if direction == "decode":
    decrypt(text, shift)
   
