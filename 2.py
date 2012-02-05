cipherText = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

url = "map"

pattern = {'k': 'm', 'o': 'q', 'e': 'g'}
    
def convert(str):
    l = []
    for letter in str:
        if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
            ascii_convert = ord(letter) + 2
            if ascii_convert > ord('z'):
                ascii_convert = ord('a') + ascii_convert % ord('z') - 1
            letter = chr(ascii_convert)
        l.append(letter)
    return "".join(l)

if __name__ == "__main__":
    print convert(cipherText)
    print convert(url)
 # url: http://www.pythonchallenge.com/pc/def/ocr.html
    

    