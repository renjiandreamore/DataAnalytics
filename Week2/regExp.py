##########################################
#### Another Regular Expression Tutorial #
##########################################

startingString = "The lazy dog\nsleeps in the yard."
findIt = re.compile(r"[A-Z][a-z]*")
findIt.findall(startingString)
# OUTPUT: ['The']

startingString = "The lazy dog\nsleeps in the yard."
findIt = re.compile(r".*lazy.*")
findIt.findall(startingString)
# OUTPUT: ['The lazy dog']

startingString = "The lazy dog\nsleeps in the yard."
findIt = re.compile(r"[a-z]*\.")
findIt.findall(startingString)
# OUTPUT: ['yard.']

startingString = "The 'lazy' dog\nsleeps in the yard."
findIt = re.compile(r"\'.*\'")
findIt.findall(startingString)
# OUTPUT: ['lazy']

startingString = "The 'lazy' dog\nsleeps in the yard."
findIt = re.compile(r"\'(?P<wordInQuotes>.*)\'")
output = findIt.search(startingString)
print output.group('wordInQuotes')
# OUTPUT: lazy

startingString = "The 'lazy' dog\nsleeps in the yard."
findIt = re.compile(r"\'(?P<wordInQuotes>.*)\'")
output = findIt.search(startingString)
print output.group('wordInQuotes')
# OUTPUT: lazy

startingString = "The 'lazy' dog\nsleeps 'in' the yard."
findIt = re.compile(r"\'(.*)\'")
output = findIt.findall(startingString)
for word in output:
 print word
# OUTPUT: lazy
# OUTPUT: in
 
