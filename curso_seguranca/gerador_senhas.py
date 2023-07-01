import random, string

tamanho = int(input('digite o tamanho da senha que vc deseja gerar: '))

chars = string.ascii_letters + string.digits + '!@#$%*()-=+-/][,:.'

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(tamanho)))
