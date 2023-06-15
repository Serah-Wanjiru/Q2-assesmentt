class Storytelling:
    def __init__(self,oralStory,language,storyTeller):
        self.oralStory=oralStory
        self.language=language
        self.storyTeller=storyTeller
    
    def getStories(self):
        print(f"{self.StoryTeller} purin gave us {self.oralStory} that was written in kikuyu language but She translated to {self.language}")
        
        
    

storytelling=Storytelling("Being submissive to the husband during back day","kiswahili","GrandMa Purin")
storytelling.getStories()
class MyStory(Storytelling):
    def __init__(self,length,moralLessons,ageGroup):
        self.length=length      
        self.moralLessons=moralLessons
        self.ageGroup=ageGroup
    
    def getDetailsOfStory():
        print(f"{self.oralStory} it was narated to us {self.storyTeller} from english to {self.language} which took {self.length} the targeted listeners were girls who were between {self.ageGroup} and above and the most important moral lessons were {self.moralLessons}"):


    
    

mystory=MyStory("one hour","Stand with your values","16yrs")
mystory.getDetailsOfStory() 


# Create a LibraryCatalog class that handles the cataloging and management of
# books in a library. Implement methods to add new books, search for books by
# title or author, keep track of available copies, and display book details.
class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
    
    def statement(self):
        return f"{self.title} by {self.author} ({self.copies} available)"
    
class LibraryCatalog:
    def __init__(self):
        self.books = []
    
    def add_book(self, title, author, copies=1):
        book = Book(title, author, copies)
        self.books.append(book)
    
    def search_by_title(self, title):
        return [book for book in self.books if book.title == title]
    
    def search_by_author(self, author):
        return [book for book in self.books if book.author == author]
    
    def display_book_details(self, book):
        print(book)
    
    def display_all_books(self):
        for book in self.books:
            print(book)
            
catalog = LibraryCatalog()

catalog.add_book("Blossoms of the savannah", "HR. Ole kulet", 5)
catalog.add_book("Decolonise Mind", "Ngugi", 3)
catalog.add_book("Kigogo", "Pauline Kea", 6)

results = catalog.search_by_author("J.K. Rowling")
for book in results:
    catalog.display_book_details(book)

catalog.display_all_books()            

# //Create a FlightBooking class that represents a flight booking system. Implement
# //methods to search for available flights based on destination and date, reserve
# //seats for customers, manage passenger information, and generate booking
# //confirmations.
class FlightBooking:
   def __init__ (self destination,date,seats,information,booking):
        self.destination=destination
        self.date=date
        self.seats=seats
        self.information=information
        self.booking=booking
    
   def availableFlight():
        print(f"The fly Emirate plane will will fly in {self.date} to {self.destination} who ever had given {self.booking} with ${self.information} will seat in {self.seats} the plane will be available for you"):
    

flightBooking=FlightBooking("Eldorect","12.july.2023","infront seats","morning travelling","morning booking")
flightBooking.availableFlight()

# //Create a class called Product with attributes for name, price, and quantity.
# //Implement a method to calculate the total value of the product (price * quantity).
# //Create multiple objects of the Product class and calculate their total values.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def total_value(self):
        return self.price * self.quantity
    
product1 = Product("Apple", 0.5, 10)
product2 = Product("Banana", 0.25, 20)
product3 = Product("Orange", 0.75, 5)
total_value1 = product1.total_value()
total_value2 = product2.total_value()
total_value3 = product3.total_value()
total_value_all = total_value1 + total_value2 + total_value3
print( total_value_all)
