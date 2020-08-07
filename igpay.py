def igpay(word):
    if word[0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', "O", "U"]:
        return word + "way"
    else:
        return word[1:] + word[0] + "ay"

print(igpay('pig')) #igpay
print(igpay('apple')) #appleway
print(igpay('elon')) #elonway
print(igpay('Earl'))
