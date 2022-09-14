"""
Class representing a book with two attributes
'author' and 'title'
"""
class Book:
#Initializing author and titles to blank string
author = ""
title = ""
"""
A contructor that creates a Book object with given author and title
"""
def __init__(self, titleName, authorName):
self.title = titleName
self.author = authorName

"""
Function that prints a string representing the book in the format
'<title>', written by <author>
"""
def display(self):
print(f"\'{self.title}\', written by {self.author}")

#Creates two objects of Book class
obj1 = Book("Of Mice and Men", "John Steinbeck")
obj2 = Book("To kill a Mockingbird", "Harper Lee")

#Calls their display() function to display them
obj1.display()
obj2.display()