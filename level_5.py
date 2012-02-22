URL = "http://www.pythonchallenge.com/pc/def/peak.html"

PREFIX = "http://www.pythonchallenge.com/pc/def/"

def getPickleSrcFromURL(url):
    from urlister import URLister
    import urllib
    from sgmllib import SGMLParseError
    
    try:
        usock = urllib.urlopen(url)
        parser = URLister()
        parser.feed(usock.read())
        
        unpickle_url = PREFIX + parser.getUrl()[0]
        usock = urllib.urlopen(unpickle_url)
        unpickle_src = usock.read()
    except IOError:
        print "open url error"
    except SGMLParseError:
        print "Parser Error"
    finally:
        usock.close()
        parser.close()
        
    return unpickle_src
        
    
    

def unpickleFromSrc(src):
    import pickle

    data = pickle.loads(src)
    return data
    
    
if __name__ == "__main__":
    src = getPickleSrcFromURL(URL);
    data = unpickleFromSrc(src)
    for line in data:
        print "".join([(k * v) for k, v in line])
        
#url http://www.pythonchallenge.com/pc/def/channel.html
    
        
    
    
    
    