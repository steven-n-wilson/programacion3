import sys,os
import csv

filename = 'InitialContacts.txt'

data = []
file = open(filename, "r")
for line in file:
   data.append(line)



data = ''.join(data)
data = data.split(',')


print(data)



