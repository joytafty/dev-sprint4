# This is where the answers to Chapter 10 questions
# Name: Tharathorn (Joy) Rimchala

# Exercise 10.7 (anagram)
def is_anagram(w1, w2):
	import collections
	a1 = collections.Counter(w1)
	a2 = collections.Counter(w2)
	return (a1 == a2)

w1 = 'reset'
w2 = 'steer'
b = is_anagram(w1, w2)
print b

# Exercise 10.13 (interlock)
# Use word list from last week
def madewlist():
	fin = open('words.txt')
	wl = [];
	for line in fin:
		ww = line.strip()
		wl.append(ww)
	return wl

def is_interlock(cweven, cwodd, cw, wl):
	if (cweven in wl) & (cwodd in wl):
		print cweven + " and " + cwodd + " are interlocked ! : " + cw
		return cweven, cwodd
		
# Generate word list
wl = madewlist()
for cw in wl:
	cweven = cw[0::2] 
	cwodd = cw[1::2]
	is_interlock(cweven, cwodd, cw, wl)