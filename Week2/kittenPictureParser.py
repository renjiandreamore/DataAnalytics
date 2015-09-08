import urllib
import re
import os
siteHTML = "http://www.allthosekittens.com/kittens.php"
allHTML = urllib.urlopen(siteHTML).read()
pics = re.findall('img src="([^"]*)', allHTML)

directoryForKittenPics = 'C:\pics\kittens\kittenPic'
if not os.path.exists(directoryForKittenPics):
 os.makedirs(directoryForKittenPics)

counter = 1
for pic in pics:
 urllib.urlretrieve(("http://www.allthosekittens.com/" + pic), directoryForKittenPics + '\\' + `counter` + '.jpg') 
 counter = counter + 1
