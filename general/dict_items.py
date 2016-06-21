# Accessing python dictionary elements

x = {
    'van': 'motor',
    'ben': 'car',
    'tan': 'train'
}

for name, typ in x.items():
    print("%s key of %s" % (name, typ))
