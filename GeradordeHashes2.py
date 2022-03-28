import hashlib
string = input('Digite a frase para gerar hash:')
#resultado = hashlib.md5(b'Python security')# b vai converter a strings em byte
resultado = hashlib.md5(string.encode('utf-8'))
print('O hash da string e: ', resultado.hexdigest())
