import binascii

def messageFromBinaryCode(code):
    code = ('0b'+code)
    n = int(code,2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
