import os


contents = []
for f in [
    "Common", 
    "Util", 
    "Salamander", 
    "Component",
    "Harmonics",
    "Keybed",
    "Pedal",
    "String",
    "Strings",
    "Piano",
]:
    sep = '//' + ('-' * 77)
    with open(f'./src/{f}.js', 'r+') as in_file:
        contents.append('\n'.join([
            '\n',
            sep,
            sep,
            '//' + f'{f}.js'.center(75, ' '),
            sep,
            sep,
            '\n',
        ]))

        contents.append(in_file.read())
    
    with open('tonejs-piano.js', 'w+') as out_file:
        out_file.write(''.join(contents))

