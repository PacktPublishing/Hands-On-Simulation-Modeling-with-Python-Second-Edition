from cryptography.fernet import Fernet
 
title = "Simulation Modeling with Python"
 
secret_key = Fernet.generate_key()
 
fernet_obj = Fernet(secret_key)
 
enc_title = fernet_obj.encrypt(title.encode())
 
print("My last book title = ", title)
print("Title encrypted = ", enc_title)
 
dec_title = fernet_obj.decrypt(enc_title.decode())
 
print("Title decrypted = ", dec_title)