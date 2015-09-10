#### Read a remote file #
import urllib
fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
for line in fhand:
 print "# " + line.strip()
# But soft what light through yonder window breaks
# It is the east and Juliet is the sun
# Arise fair sun and kill the envious moon
# Who is already sick and pale with grief


#### Opening a webpage (HTML) # 
import urllib
fhand = urllib.urlopen('http://www.pitt.edu/~pmd18/htmlTest/')
for line in fhand:
 print "# " + line.strip()
# <?xml version="1.0" encoding="iso-8859-1"?>
#
# <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
# <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
# <head>
# <title>Patrick Dudas</title>
#
# <!-- Use two CSS throughout the website -->
# <link rel="stylesheet" media="all" href="index.css" />
# <link rel="stylesheet" type="text/css" href="print.css" media="print" />
# <link rel="stylesheet" type="text/css" href="handheld.css" media="handheld" />
# </head>
#
# <body>
#
# <!-- MASTHEAD (Title Bar) -->
#
# <div id="masthead">
# <table class="masthead" border="0" width="100%">
# <tr>
# <td style="width:30%">
# <div id="sisimg">
# <a href="http://www.sis.pitt.edu">
# <img src="sis6.jpg" alt="SIS Image" width="400" height="63" />
# </a>
# </div>
# </td>
# <td style="width:50%">
# <h4>Patrick Dudas - 2nd PhD Student <br /> @ University of Pittsburgh<br />@ Information Science department</h4>
# </td>
# </tr>
# </table>
# </div>
# <!-- CONTENT -->
# <div id="content">
# <table class="masthead" border="0" width="100%">
# <tr>
# <td style="width:30%">
# <div id="sisimg">
# <img src="pics/me_taiwan.jpg" alt="In Taiwan" width="300" height="225" />
# </div>
# </td>
# <td style="width:30%">
# Let's see.. as you can see from above. I am 2nd year PhD student in the IS school at Pitt. I also received my Masters here in the same curriculum.
# For undergrad, I went to Westminster College to get my bachelors of science degree in Physics.
# I'm a native Pittsburghian. So naturally I love the Steelers, Pens, and Buccos.
# <br />
# Fav Visualizations:
# <br />
# <a href="http://www.chrisharrison.net/projects/visualization.html">http://www.chrisharrison.net/projects/visualization.html</a>
# <br />
# <a href="http://vis.robbymacdonell.com/stanley-cup/">http://vis.robbymacdonell.com/stanley-cup/</a>
# <br />
# Favorite TED talk:
# <br />
# <a href="http://www.ted.com/talks/david_mccandless_the_beauty_of_data_visualization.html">http://www.ted.com/talks/david_mccandless_the_beauty_of_data_visualization.html</a>
# <br />
# HTML 5 Beauty:
# <br />
# <a href="http://www.thewildernessdowntown.com/">http://www.thewildernessdowntown.com/</a>
#
# </td>
# <td style="width:40%">
# </td>
# </tr>
# </table>
# </div>
# </body>
# </html>

#### Just looking at the pics #
import urllib
import re
allHTML = urllib.urlopen('http://www.pitt.edu/~pmd18/htmlTest/').read()
pics = re.findall('<img src="(.*?)"', allHTML)
for pic in pics:
 print "# " + pic
# sis6.jpg
# pics/me_taiwan.jpg
  
#### Let's get the pics #
import urllib
import re
siteHTML = "http://www.pitt.edu/~pmd18/htmlTest/"
allHTML = urllib.urlopen(siteHTML).read()
pics = re.findall('<img src="(.*\.[j|J][p|P][g|G])"', allHTML)
counter = 1
dirPictures = 'C:\pics\picNumber'
if not os.path.exists(dirPictures):
 os.makedirs(dirPictures)

for pic in pics:
 urllib.urlretrieve((siteHTML + pic), dirPictures + '\\' + `counter` + '.jpg') 
 counter = counter + 1
 
#### BeautifulSoup Example #
from BeautifulSoup import *
import urllib
siteHTML = "http://www.pitt.edu/~pmd18/htmlTest/"
html = urllib.urlopen(siteHTML).read()
soup = BeautifulSoup(html)
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
 print "# " + tag.get('href', None)
 
# http://www.sis.pitt.edu
# http://www.chrisharrison.net/projects/visualization.html
# http://vis.robbymacdonell.com/stanley-cup/
# http://www.ted.com/talks/david_mccandless_the_beauty_of_data_visualization.html
# http://www.thewildernessdowntown.com/
