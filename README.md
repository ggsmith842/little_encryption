# caesar cipher

### What is  a caesar cipher?

A casesar cipher is a simple encryption method that shifts the value of a character by the value of the shift.

For example, if shift if 1, then A becomes B, 1 becomes 2, etc.

### The function 

 *``ceasar_cipher``*
 
 ceasar_cipher accepts three arguments:
     1. ``pw_str`` - the string you are wanting to encrypt
     2. ``shift`` - the value you want the cipher to apply (can only accept values 1-3*)
         *shift currently only accepts values 1-3*
         *will try to fix so more shift values can be applied*
     3. ``decryption`` - a bool when set to `True` will decrypt your encrypted string*
         *must know original shift value*

**Important Notes**

- Remember the shift value if you want to be able to decrypt a string later
- The encryption function will currently only accept shift values 1-3