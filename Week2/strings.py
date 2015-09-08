##########################################
#### String Tutorial #####################
########################################## 

stringHello = "hello from Pittsburgh!"

#### capitalize() #####################
# Returns string where the first character (if a letter)
# is made upper-case, rest lower-case
print stringHello.capitalize()
# OUTPUT: Hello from pittsburgh!

#### center(#,fill-character) #####################
# Starting at the center, counts left then right
# the number specified. Then adds fill-character
print "ciao".center(1)
print "ciao".center(2)
print "ciao".center(4)
print "ciao".center(5)
print "ciao".center(6)
print "ciao".center(10, "!")
# OUTPUT: !!!ciao!!!

#### count(sub,start=0,end=sys.maxint) #####################
# Counts the number occurrences of sub
print stringHello.count("hello")
print stringHello.count("o")
print stringHello.count("o", 6)
#OUTPUT: 2
print stringHello[6:]
#OUTPUT: from Pittsburgh!
print stringHello.count("o", 6, 3) # not what we are looking for!
#OUTPUT: 0
print stringHello.count("o", 6, len(stringHello)-3)
#OUTPUT: 1
print stringHello[6:len(stringHello)-3] 
#OUTPUT: from Pittsbur

#### endswith(suffix,start=0,end=sys.maxint) or startswith #####################
# returns true or false if ends/starts with suffix
print stringHello.endswith("Pittsburgh!")
#OUTPUT: TRUE
print stringHello.endswith("Pittsburgh") # No "!"
#OUTPUT: FALSE
print stringHello.startswith("hello")
#OUTPUT: TRUE

#### expandtabs(tabsize) #####################
# the tabs turn into space (tabsize)
somethingElse = "%s\t%s\t%s\t\t%s?" % ("this","is","tabbed","see?")
print somethingElse
#OUTPUT: this    is      tabbed          see??
print somethingElse.expandtabs(15)
#OUTPUT: this           is             tabbed                        see??

#### find(suffix,start=0,end=sys.maxint) or rfind #####################
# gives the position value of the first occurrence
# returns -1 (if not found)
print len(stringHello)
#OUTPUT 21
print stringHello.find("o")
#OUTPUT: 4
print stringHello.rfind("o")
#OUTPUT: 18

#### index(suffix,start=0,end=sys.maxint) or rindex #####################
# like find: gives the position value of the first occurrence
# returns ValueError 
print stringHello.index("z")
#OUTPUT: Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# ValueError: substring not found

#### isalnum, isalpha, isdigit, islower, isspace, istitle, isupper #####################
# returns true if.. well.. true. False if not.
print stringHello.isdigit()
#OUTPUT: False
print stringHello.isalpha()
#OUTPUT: False
print stringHello.isalnum()
#OUTPUT: False 

#### ljust(n,fillchar=" ") or rjust
# places the fillchar to nth character (if available) from l(eft) or r(ight) #####################
# using len() helps with making sure the characters get added
print stringHello.ljust(len(stringHello)+2,"x")
#OUTPUT: hello from Pittsburgh!xx
print stringHello.rjust(len(stringHello)+2,"x")
#OUTPUT: xxhello from Pittsburgh!

#### lower() or upper()
# change all chars to lower or upper - case
print stringHello.lower()
#OUTPUT: hello from pittsburgh!
print stringHello.upper()
#OUTPUT: HELLO FROM PITTSBURGH!

#### lstrip(x=string.whitespace) or rstrip or strip #####################
# remove x (default, whitespaces) from l(eft) or r(ight) or both sides
somethingElse = "this is a sentence    " 
print somethingElse.rstrip()
# OUTPUT: this is a sentence
print stringHello.rstrip("!")
# OUTPUT: hello from Pittsburgh
print stringHello.lstrip("h")
# OUTPUT: ello from Pittsburgh!

#### replace(old,new,maxsplit) #####################
# reads the string, replace all letters in old, with letter in new (where maxsplit is how many occurences)
stringHello.replace("e", "a")
#OUTPUT: hallo from Pittsburgh!
stringHello.replace("o", "0", 2)
#OUTPUT: hell0 fr0m Pittsburgh!

#### swapcase() #####################
# changes lower case to upper case (and vice versa)
stringHello.swapcase()
# OUTPUT: HELLO FROM pITTSBURGH!

#### title() #####################
# creates a title out of the string
stringHello.title()
# OUTPUT: Hello From Pittsburgh!
