# from topics import functions as func

# Examples of extract information from a string
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atsign_postion = data.find('@')
space_position = data.find(' ', atsign_postion)
# you can print 'uct.ac.za' use data[atsign_postion+1: space_position])

# Search through file
file_name = 'files/mbox-short.txt'
data = open(file_name)
for line in data:
    if line.startswith('From:'):
        print(line.strip())
