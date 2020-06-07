from PyLyrics import *
F = open('Ed_Sheeran_Deluxe.txt' , 'r')

Line_list = F.readlines()

for line in Line_list:
    Singer , Song = line.split(",")
    Song = Song.strip()
    try:
        File_name = Song + ".txt"
        print(File_name)
        f = open(File_name,'w')
        f.write(PyLyrics.getLyrics(Singer,Song))
        f.close()
    except:
        print('{} Not added',Song)
        
        
        
    
    
