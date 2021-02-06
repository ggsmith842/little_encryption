# caesar cipher

### What is  a caesar cipher?

A casesar cipher is a simple encryption method that shifts the value of a character by the value of the shift.

For example, if shift is 1, then A becomes B, 1 becomes 2, etc.

### The function 

 *``caesar_cipher``*
 
 ceasar_cipher accepts three arguments: <br>
     1. ``pw_str`` - the string you are wanting to encrypt <br>
     2. ``shift`` - the value you want the cipher to apply (1-9) <br>
     3. ``decryption`` - a bool when set to `True` will decrypt your encrypted string*
         *must know original shift value*

**Important Notes**

- Remember the shift value if you want to be able to decrypt a string later
