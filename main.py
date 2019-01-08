#coding = utf-8

import sys
from datetime import datetime
import json

class Book():
    def __init__(self, title, author, language, rating, date):
        self.set_title(title)
        self.set_author(author)
        self.set_language(language)
        self.set_rating(rating)
        self.set_date(date)
    
    def set_title(self, title):
        self.title = title
        
    def set_author(self, author):
        self.author = author
    
    def set_language(self, language):
        self.language = language
        
    def set_rating(self, rating):
        self.rating = rating
        
    def set_date(self, date):
        self.date = date
        
class Library():
    def __init__(self):
        self.books = []
        try:
            with open("bodleian.json", "r") as file:
                book_list = [json.loads(line) for line in file]
                for dict in book_list:
                    self.books.append(Book(title = dict["title"], author = dict["author"], language = dict["language"], rating = dict["rating"], date = datetime.strptime(dict["date"], "%d, %m, %Y")))
        except:
            pass
        
    def add_book(self, title, author, language, rating, date):
        dict = {
            "title": title,
            "author": author,
            "language": language,
            "rating": rating,
            "date": date.strftime("%d, %m, %Y")
            }
        
        for book in self.books:
            if title == book.title:
                print("Book already exists")
                return
        self.books.append(Book(title, author, language, rating, date))
        with open("bodleian.json", "a+") as outfile:
            json.dump(dict, outfile)
            outfile.write(" \n")
        print("Book has been added, thank you")
 
    def delete_book(self, delete_book):
        for i, book in enumerate(self.books):
            if delete_book == book.title:
                self.books.pop(i)
                with open("bodleian.json", "w") as outfile:
                    for book in self.books:
                        json.dump({"title": book.title,"author": book.author,"language": book.language,"rating": book.rating,"date": book.date.strftime("%d, %m, %Y")}, outfile)
                        outfile.write(" \n")
                print("This book has been deleted from The Library")
                return
            else:
                pass
        print("I'm sorry, this book does not exist in The Library")
        
    def view_all_books(self):
        for counter, book in enumerate(self.books):
            counter = counter + 1
            print("\n", counter, "\n Title: ", book.title, "\n Author: ", book.author, "\n Language: ", book.language, "\n Stars out of 5: ", "*"*book.rating, "\n Finished reading: ", book.date)
        if len(self.books) == 0:
            print("The Library is empty")
    
    def view_one_book(self, title_choice, author_choice):
        state = True
        for book in self.books:
            if title_choice == book.title and author_choice == book.author:
                state = False
            else: pass
        if state == True:
            print("\n The Library contains no such volume on its shelves")
        else:
            print("\n Title: ", book.title, "\n Author: ", book.author, "\n Language: ", book.language, "\n Stars out of 5: ", "*"*book.rating, "\n Finished reading: ", book.date)
     
def main():
    
    bodleian = Library()
    
    while True:
        print("Welcome to The Library \n")
        #print("Select an account")
        print("What can I help you with? \n")
        print("(1) Enter 1 to view all books")
        print("(2) Enter 2 to view one book")
        print("(3) Enter 3 to add a new book")
        print("(4) Enter 4 to remove a book")
        print("(5) Enter 5 to exit")
    
        try:
            user_choice= int(input("Choice: "))
        except ValueError:
            print("\n That's not a number I recognise. Try again.")
            user_choice = None
    
        if user_choice == 1:
            bodleian.view_all_books()
        elif user_choice == 2:
            title_choice = input("Title? ")
            author_choice = input("Author? ")
            bodleian.view_one_book(title_choice, author_choice)
        elif user_choice == 3:
            enter_title = input("Title? ")
            enter_author = input("Author? ")
            enter_language = input("Language? ")
            print("How would you rate that book?")
            num_check = True
            while num_check:
                try:
                    enter_rating = int(input("From 1 (lowest) to 5 (highest) starts: "))
                    if enter_rating in range(1, 6):
                        num_check = False
                    else:
                        print("The number needs to be between 1 and 5. Try again.")
                except ValueError:
                    print("I don't recognise this number. Try again.") 
            format_check = True
            while format_check:
                try:
                    user_entry = str(input("When did you finish reading it (DD, MM, YYYY)? "))
                    enter_date = datetime.strptime(user_entry, "%d, %m, %Y")
                    format_check = False
                except ValueError:
                    print("Incorrect date format. Try again using DD, MM, YYYY.")
            bodleian.add_book(enter_title, enter_author, enter_language, enter_rating, enter_date)
        elif user_choice == 4:
            delete_book = input("What is the title of the book you want to delete? ")
            bodleian.delete_book(delete_book)
        elif user_choice == 5:
            break
        else:
            print("\n Unkown choice")
        input("\n Press ENTER to continue")

    print("\n Goodbye! And thank you for visiting The Library!")
    
main()
    
    
    
    
        
        
        
