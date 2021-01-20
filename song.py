import csv

songsfile = open('songs.csv')
songsreader = csv.reader(songsfile)
songsdata = list(songsreader)

#for i in range(len(songsdata)):
#print(songsdata[i][1] + " - " + songsdata[i][2])