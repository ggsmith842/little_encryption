
import string

        
def ceasar_cipher(text: str, encrypt: bool = True, shift_value: int = 1) -> str:
        
        # set character set
        ascii_vals = string.printable 

        # if decrption take the negative of the shift value to get the original message
        if not encrypt:
            shift_value = 0 - shift_value    
                      
        # get index value for each character in text
        shifted_index_vals = [ascii_vals.index(i) + shift_value for i in text]  
            

        # get shifted characters in ascii list
        shifted_chrs = [ascii_vals[i] for i in shifted_index_vals]

        # join shifted chrs to get encrypted text
        return "".join(shifted_chrs)


if __name__ == '__main__':
    text = "hello, world"

    encrypted_text = ceasar_cipher(text)

    print(encrypted_text)

    decrypted_text = ceasar_cipher(encrypted_text, encrypt=False)

    print(decrypted_text )
