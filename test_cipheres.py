from ciphers import ceasar_cipher


def test_ceasar_cipher_encryption():

    # encryption tests 
    assert ceasar_cipher('Hello', encrypt=True, shift_value=1) == 'Ifmmp'
    assert ceasar_cipher('Hello, World!', encrypt=True, shift_value=1) == 'Ifmmp-\tXpsme"'


def test_ceasar_cipher_decryption():

    # decryption tests
    assert ceasar_cipher('Ifmmp', encrypt=False, shift_value=1) == 'Hello'
    assert ceasar_cipher('Ifmmp-\tXpsme"', encrypt=False, shift_value=1) == 'Hello, World!'


    
