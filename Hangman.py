import random
z = 'play'
print("H A N G M A N")
print()
while z == 'play':
    z = input('Type "play" to play the game, "exit" to quit')
    if z == 'exit':
        break
    if z != 'play':
        continue
    l = ['python', 'java', 'kotlin', 'javascript']
    b = random.choice(l)
    e = set(b)
    g = list(b)
    n = list()
    a = list()
    al = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    for i in range(len(b)):
        n.append('-')
    chance = 8
    while chance > 0:
        print()
        print(''.join(n))
        if ''.join(n) == b:
            print('''You guessed the word!
You survived!''')
            break
        f = input("Input a letter")
        if len(f) != 1:
            print('You should input a single letter')
            continue
        if f not in al:
            print('It is not an ASCII lowercase letter')
            continue
        if f in a:
                print('You already typed this letter')
                continue
        else:
            a.append(f)
        if f not in e:
            print('No such letter in the word')
            chance = chance - 1
        else:
            for k in range(len(b)):
                if f == b[k]:
                    n[k] = f
        if chance > 0:
            print()
    else:
        print('You are hanged!')
