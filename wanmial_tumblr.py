import urllib
import re

baseurl = "http://wanimal1983.tumblr.com"


for i in range(1, 115):
    count = 1
    print i
    if i == 1:
        url = baseurl
    else:
        url = baseurl + '/page/' + str(i)
    lines = urllib.urlopen(url).readlines()
    usefulline = []
    for line in lines:
        if "img src=" in line:
            usefulline.append(line)
    uline = []
    for line in usefulline:
        if ".jpg" in line:
            uline.append(line)
    for line in uline:
        imgurl = re.split('img src="', line)[1]
        imgurl = re.split('" ', imgurl)[0]
        filename = str(i) + '.' + str(count) + '.jpg'
        urllib.urlretrieve(imgurl, filename)
        count = count + 1
        
