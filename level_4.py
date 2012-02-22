START_URL = "http://www.pythonchallenge.com/pc/def/linkedlist.php"

PREFIX_URL = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

def getFirstUrlFromPageSource(start_url):
    from urlister import URLister
    import urllib
    from sgmllib import SGMLParseError
    
    first_url = ""
    try:
        usock = urllib.urlopen(start_url)
        parser = URLister()
        parser.feed(usock.read())
    except IOError:
        print "open url error"
    except SGMLParseError:
        print "parser feed error"
    finally:
        usock.close()
        parser.close()
    
    urls = parser.getUrl()
    
    for url in urls:
        if url.find("nothing") >= 0:
            temp = url.split("=")
            first_url = PREFIX_URL + temp[-1]
            break
        
    return first_url

def getSixthQuizURLFromFirstURL(first_url):
    import urllib
    
    loop_time = 398
    next_url = first_url
    usock = None
    for i in range(loop_time):
        usock = urllib.urlopen(next_url)
        page_src = usock.read()
        tokens = page_src.split()
        nothing_num = tokens[-1]
        next_url = PREFIX_URL + nothing_num
    
    usock.close()
    return next_url

def anotherSimpleWay():
    import urllib
    import re
    
    loop_time = 400
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    seed = "12345"
    
    pre_seed = seed
    
    for i in range(loop_time):
        if i == 84:
            pass
        try:
            text = urllib.urlopen(url + seed).read()
            pre_seed = seed
            seed = "".join(re.findall(r"nothing is (\d+)", text))
            int(seed)
            print i, "    Next:", seed
        except IOError:
            print "url", url + seed, "is error"
        except:
            print i, "    Last:", text
            seed = str(int(pre_seed) / 2)
    
if __name__ == "__main__":
    #first_url = getFirstUrlFromPageSource(START_URL)
    #print getSixthQuizURLFromFirstURL(first_url)  
    anotherSimpleWay()

# url http://www.pythonchallenge.com/pc/def/peak.html    
        
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
    