#  ####################################################
#  ALGO CHALLENGE DAY #12 @everyone 
#  👇🏻 
#  #A Needle in the Haystack
#  Can you find the needle in the haystack?

#  Write a function findNeedle() that takes an array full of junk but containing one "needle"
#  After your function finds the needle it should return a message (as a string) that says:
#  "found the needle at position " plus the index it found the needle, so:

#  find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])
#  should return "found the needle at position 5" (in COBOL "found the needle at position 6")

def find_needle(arr):
    if len(arr) == 0: return "Hey! I can't search an empty array!"
    for i in range(len(arr)):
        if arr[i] == "needle": return f'Found the needle at position {i}!'
    return 'Needle not found!'
print(find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk']))
print(find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'randomJunk']))
print(find_needle([]))
