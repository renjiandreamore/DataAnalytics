import csv
import urllib

PopulationAndDensity = "http://boxnumbertwo.com/PittsburghData/Population_and_Density.csv"

fhand = urllib.urlopen(PopulationAndDensity)

pop1940 = dict()
try:
	reader = csv.reader(fhand)
	next(reader, None)  # skip the headers
	for row in reader:
		print "add here"
finally:
	fhand.close()
	
popDifference4050 = dict()	

for key in pop1940:
	print "add here"
	

print "Difference between 1940 - 1950: "
print "Difference between 1950 - 1960: "
print "Difference between 1960 - 1970: "
print "Difference between 1970 - 1980: "
print "Difference between 1980 - 1990: "
print "Difference between 1990 - 2000: "
print "Difference between 2000 - 2010: "

#Difference between 1940 - 1950:  5148
#Difference between 1950 - 1960:  -61563
#Difference between 1960 - 1970:  -95088
#Difference between 1970 - 1980:  -96216
#Difference between 1980 - 1990:  -54059
#Difference between 1990 - 2000:  -36352
#Difference between 2000 - 2010:  -27823

print "#Difference between 1940 - 1950 for Mount Washington: "
print "#Difference between 1950 - 1960 for Mount Washington: "
print "#Difference between 1960 - 1970 for Mount Washington: "
print "#Difference between 1970 - 1980 for Mount Washington: "
print "#Difference between 1980 - 1990 for Mount Washington: "
print "#Difference between 1990 - 2000 for Mount Washington: "
print "#Difference between 2000 - 2010 for Mount Washington: "
#Difference between 1940 - 1950 for Mount Washington:  -953
#Difference between 1950 - 1960 for Mount Washington:  -1645
#Difference between 1960 - 1970 for Mount Washington:  -2628
#Difference between 1970 - 1980 for Mount Washington:  -2992
#Difference between 1980 - 1990 for Mount Washington:  -1095
#Difference between 1990 - 2000 for Mount Washington:  -822
#Difference between 2000 - 2010 for Mount Washington:  -1079

print "#Difference between 1940 - 1950 for North Oakland: "
print "#Difference between 1950 - 1960 for North Oakland: "
print "#Difference between 1960 - 1970 for North Oakland: "
print "#Difference between 1970 - 1980 for North Oakland: "
print "#Difference between 1980 - 1990 for North Oakland: "
print "#Difference between 1990 - 2000 for North Oakland: "
print "#Difference between 2000 - 2010 for North Oakland: "
#Difference between 1940 - 1950 for North Oakland:  1936
#Difference between 1950 - 1960 for North Oakland:  -610
#Difference between 1960 - 1970 for North Oakland:  1213
#Difference between 1970 - 1980 for North Oakland:  42
#Difference between 1980 - 1990 for North Oakland:  2128
#Difference between 1990 - 2000 for North Oakland:  -979
#Difference between 2000 - 2010 for North Oakland:  694

	
print "#Difference between 1940 - 1950 for Shadyside: "
print "#Difference between 1950 - 1960 for Shadyside: "
print "#Difference between 1960 - 1970 for Shadyside: "
print "#Difference between 1970 - 1980 for Shadyside: "
print "#Difference between 1980 - 1990 for Shadyside: "
print "#Difference between 1990 - 2000 for Shadyside: "
print "#Difference between 2000 - 2010 for Shadyside: "
#Difference between 1940 - 1950 for Shadyside:  1599
#Difference between 1950 - 1960 for Shadyside:  -1102
#Difference between 1960 - 1970 for Shadyside:  -2329
#Difference between 1970 - 1980 for Shadyside:  -1903
#Difference between 1980 - 1990 for Shadyside:  -560
#Difference between 1990 - 2000 for Shadyside:  369
#Difference between 2000 - 2010 for Shadyside:  161

totalDiff20101940 = dict()  
### USE THIS TO SORT, Returns a list (array) ###
totalDiff20101940 = sorted(totalDiff20101940.items(), key=lambda x:x[1])
print "Top 10 - Worst"
print "Top 10 - Best"	

	
#Top 10 - Worst

#  ('South Side Flats', -15879)
#  ('Middle Hill', -15322)
#  ('Crawford-Roberts', -14789)
#  ('Bloomfield', -12266)
#  ('Larimer', -11610)
#  ('Mount Washington', -11214)
#  ('East Allegheny', -10835)
#  ('Homewood South', -10678)
#  ('South Side Slopes', -10660)
#  ('Perry South', -10521)
#  ('Homewood North', -10319)
#Top 10 - Best
#  ('Stanton Heights', -9)
#  ('Bon Air', -6)
#  ('Swisshelm Park', 23)
#  ('Oakwood', 290)
#  ('New Homestead', 301)
#  ('Northview Heights', 552)
#  ('Westwood', 618)
#  ('Squirrel Hill North', 928)
#  ('Windgap', 1151)
#  ('Banksville', 2930)
#  ('North Oakland', 4424)
	
