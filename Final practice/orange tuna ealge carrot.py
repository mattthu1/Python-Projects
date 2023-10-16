phrase = 'OrANGe TUNA EaGlE cARRot'
new_phrase = ''
for c in phrase:
    if c >= 'a' and c <= 'z':
        new_phrase += c.lower
print(new_phrase,end='')