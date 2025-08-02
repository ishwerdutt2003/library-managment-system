import datetime
import os

class LMS:
    """this class is used to keep record of books library.
    It has total four modules:"display books","Issue books","Return books","Add books" """
    def __init__(self, list_of_books, library_name):
        self.list_of_books = "List_of_books.txt"
        self.library_name = library_name
        self.books_dict = {}
        Id=101
        with open(self.list_of_books) as bk:
            content=bk.readlines()
        for line in content:
            self.books_dict.update({str(Id):{"books_title":line.replace("\n"," "),
            "lender_name":"","Issue_date":"","Status":"Available"}})
            Id=Id+1
        
        
    def display_books(self):
        print("------------------List of Books----------------")
        print("Books_Id","\t","Title")
        print("-------------------------------------------------")
        for key , value in self.books_dict.items():
            print(key,"\t\t",value.get("books_title"),"- [",value.get("Status"),"]")

    def Issue_books(self):
        books_id=input("Enter books ID:")
        current_date=datetime.datetime.now().strftime("%Y-%m_%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]['Status']=="Available":
                print(f"This book is already issued to {self.books_dict[books_id]['lender_name']} on{self.books_dict[books_id]['Issue_date']}")
                return self.Issue_books()        
        
            elif self.books_dict[books_id]['Status']=="Available":
              
              your_name=input("Enter your name:")
              self.books_dict[books_id]['lender_name']=your_name
              self.books_dict[books_id]['Issue_date']=current_date
              self.books_dict[books_id]['Status']="Already issued"
              print("Books issued successfully!!!\n")
        else:
            print("Books ID not found!!!")
        
    def add_books(self):
        new_books=input("Enter books title: ")
        if new_books=="":
            return self.add_books()
        elif len(new_books)>25:
            print("Books title length is too long !!! Title length should be 20 character")
            return self.add_books()
        else:
            with open(self.list_of_books,"a") as bk:
                bk.writelines(f"{new_books}\n")
                self.books_dict.update({str(int(max(self.books_dict))+1):{'books_title':new_books,'lender_name':"",
                'Issue_date':"",'Status':"Available"}})
                print(f"this book {new_books} has been successfully added")
    def Return_books(self):
        books_id=input("Enter book id :")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]["Status"]=="available":
                print("this book is already in library.please check your book id.")
                return self.Return_books()
            elif not self.books_dict[books_id]["Status"]=="Available":
                self.books_dict[books_id]["lender_name"]=""
                self.books_dict[books_id]["Issue_date"]=""
                self.books_dict[books_id]["Status"]="Available"
                print("successfully returned !!!\n")
        else:
            print("book id not found.")

    def search_books(self):
        search_term = input("Enter book title to search: ").lower()
        found = False
        print("------------------Search Results----------------")
        print("Books_Id\tTitle\t\t\tStatus")
        print("------------------------------------------------")
        for book_id, details in self.books_dict.items():
            if search_term in details['books_title'].lower():
                print(f"{book_id}\t\t{details['books_title'][:25]:<25} - [{details['Status']}]")
                found = True
        if not found:
            print("No matching books found.")


try:
    myLMS=LMS("list_of_books.txt","Python's")
    press_key_list ={"D":"Display Books","I":"Issue Books","S":"Search book","A":"Add Books","R":"Return Books","Q":"Quit"}
    key_press=False
    while not (key_press=="q"):
        print(f"\n------------------welcome to {myLMS.library_name} Library managment system------------------\n")
        for key, value in press_key_list.items():
            print("Press",key,"To",value)
        key_press=input("press key: ").lower()

        if key_press=="i":
                print("\nCurrent selection:Issue books\n")
                myLMS.Issue_books()
        elif key_press=="a":
                print("\nCurrent selection:add books\n")
                myLMS.add_books()
        elif key_press=="d":
                print("\nCurrent selection:display books\n")
                myLMS.display_books()
        elif key_press=="s":
            print("\nCurrent selection: search books\n")
            myLMS.search_books()

        elif key_press=="r":
                print("\nCurrent selection:return books\n")
                myLMS.Return_books()
        elif key_press=="q":
                break
        else:
                continue
except Exception as e:
    print("something went wrong,please check your input !!!")

l=(LMS("List_of_books.txt","Python's Library"))
print(l.display_books())
