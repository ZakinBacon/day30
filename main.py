# Filenot found
# with open("afile.txt") as file:
#     file.read()
#-----------------------------------------------------------------#

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

#-----------------------------------------------------------------#

# indexerror
# fruit_list = ["Apple","bananas", "Pear"]
# fruit = fruit_list[3]

#-----------------------------------------------------------------#
# typeerror
# text = "abc"
# print(text + 5)

#-----------------------------------------------------------------#
# Try/except/else/finally
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["asda"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"the key {error_message} does not exist")
#
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print("file was closed")
#     raise TypeError("This is a type error I made up")

#-----------------------------------------------------------------#

# height = float(input("height: "))
# weight = int(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Human Height should not be over 3 meters")
#
# bmi = weight / height ** 2
# print(bmi)


#-----------------------------------------------------------------#

# fruits = ["Apple", "Pear", "Orange"]
#
# #TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     fruit = fruits[index]
#     print(fruit + " pie")
#
# try:
#     make_pie(4)
# except IndexError:
#     print("Fruit pie")

#-----------------------------------------------------------------#

# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]
#
# total_likes = 0
#
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except NameError as name_error:
#         print(f"No likes on post in {name_error}")
#     except KeyError:
#         pass
#
# print(total_likes)




