import nltk
#load data
from __future__ import division
import nltk

def PM(Old, New):
	levenshtein_distance = nltk.metrics.distance.edit_distance(Old, New)
	maximum_string_length = len(max(Old, New))
	return((1.0 - (levenshtein_distance/maximum_string_length))* 100)


def meandis(p,c,n):
	return((PM(p,c)+PM(c,n))/2)

def cleandata(list):
	cleaned = []
	for i in range(len(list)):
		if list[i] is not '':
			cleaned.append(list[i])
	return(cleaned)

#open data: 
bd = open("bostonsample.txt","r").read().split("\n")
sample = cleandata(bd)
#data types:
# of @ signs, length, lexical diversity, # of long words, 
data = [[len(sample[i]), len(set(sample[i].split(" ")))/len(sample[i].split(" ")),sample[i].count('@'), meandis(sample[i-1],sample[i],sample[i+1])] for i in range(len(sample))[3:-3]]


