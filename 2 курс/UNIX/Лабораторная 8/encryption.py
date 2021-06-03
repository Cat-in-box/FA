def dh_encrypt(msg, K):
    new_msg = ''
    for c in msg:
        new_msg += chr(ord(c)+K)
    return new_msg

def dh_decrypt(msg, K):
    new_msg = ''
    for c in msg:
        new_msg += chr(ord(c)-K)
    return new_msg