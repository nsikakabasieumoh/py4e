# from topics import functions as func

# Working with basic functions
# print(elevatorConv())
# print(sample_try_except())
# print(func.largest_number([3, 41, 12, 9, 74, 15]))

# Examples of extract information from a string
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atsign_postion = data.find('@')
space_position = data.find(' ', atsign_postion)
print(data[atsign_postion+1: space_position])
