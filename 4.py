def getPageSourceFromUrl(url):
    import urllib
    sock = urllib.urlopen(url)
    htmlSource = sock.read()
    sock.close()
    return htmlSource

def findLetterFromSourceString(src):
    import re
    res = []
    pattern = re.compile(r"""
    ([^A-Z][A-Z]{3})       # only three big bodyguard at the left side
    ([a-z])          # only a small letter at the middle
    ([A-Z]{3}[^A-Z])       # only another three big bodyguard at the right size
    """, re.VERBOSE)
    # finds is a list of tuple that matches all the strings
    finds = pattern.findall(src)
    for group in finds:
        res.append(group[1])
    return "".join(res)

if __name__ == "__main__":
    pageSource = getPageSourceFromUrl("http://www.pythonchallenge.com/pc/def/equality.html");
    print findLetterFromSourceString(pageSource)
    
# url: http://www.pythonchallenge.com/pc/def/linkedlist.php
