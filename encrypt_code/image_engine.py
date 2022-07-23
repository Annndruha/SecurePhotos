import os
from encrypt_code.cipher import AESCipher

ENCODED_EXTENSION = '.cipher'
UTF_8 = 'utf-8'


def read_image(path: str) -> bytes:
    with open(path, 'rb') as f:
        byte = f.read()
        return byte


def write_image(path: str, data: bytes) -> None:
    with open(path, 'wb') as f:
        f.write(data)


def encrypt_image(path: str, key: str) -> None:
    img_bytes = read_image(path)
    ext = os.path.splitext(path)[1]
    data_bytes = img_bytes + bytes(ext, UTF_8)
    cipher = AESCipher(key)
    encrypted_text = cipher.encrypt(data_bytes)
    new_path = os.path.splitext(path)[0] + ENCODED_EXTENSION
    write_image(new_path, encrypted_text)


def decrypt_image(path: str, key: str) -> None:
    old_ext: str
    img_bytes = read_image(path)
    cipher = AESCipher(key)
    data_bytes: bytes = cipher.decrypt(img_bytes)
    idx = data_bytes.rindex(b'.')
    original_ext = str(data_bytes[idx:].decode(UTF_8))
    img_bytes = data_bytes[:idx]
    new_path = os.path.splitext(path)[0] + '_1' + original_ext
    write_image(new_path, img_bytes)


if __name__ == '__main__':
    keyphrase = 'mypassword'
    encrypt_image(os.path.join('space.jpg'), keyphrase)
    decrypt_image(os.path.join('space.cipher'), keyphrase)