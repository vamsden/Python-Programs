# String incrementor
data = input("Enter the string to be incremented: ")

while True:
    num = int(input("Increment alphabets by?: "))
    if int(num > 26):
        print("Enter number less than 26")
    else:
        def incrementors(object):
            final_str = ""
            for x in object:
                if (ord(x) + num) > 122:
                    inc = (ord(x) - 26) + num
                else:
                    inc = ord(x) + num
                new = bytes([inc]).decode("utf-8")
                final_str = final_str + str(new)
            print(final_str)
        break

incrementors(data)


# l = string.lower
'''
t = bytes.maketrans(l, l[2:] + l[:2])
m = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
print(m.translate(t))

print("map".translate(t))
'''
