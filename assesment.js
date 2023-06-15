//Ancestral Stories:** In many African cultures, the art of storytelling is passed
//down from generation to generation. Imagine you're creating an application that
//records these oral stories and translates them into different languages. The
//stories vary by length, moral lessons, and the age group they are intended for.
//Think about how you would model `Story`, `StoryTeller`, and `Translator`
//objects, and how inheritance might come into play if there are different types of
//stories or storytellers.
class Storytelling{
    constructor(oralStory,language,storyTeller){
        this.oralStory=oralStory
        this.language=language
        this.storyTeller=storyTeller
    }
    getStories(){
        console.log(`${this.StoryTeller} purin gave us ${this.oralStory} that was written in kikuyu language but She translated to ${this.language}`)
        
        
    }
}
let storytelling=new Storytelling("Being submissive to the husband during back day","kiswahili","GrandMa Purin")
storytelling.getStories()
class MyStory extends Storytelling{
    constructor(length,moralLessons,ageGroup){
        this.length=length      
        this.moralLessons=moralLessons
        this.ageGroup=ageGroup
    }
    getDetailsOfStory(){
        console.log(`${this.oralStory} it was narated to us ${this.storyTeller} from english to ${this.language} which took ${this.length} the targeted listeners were girls who were between ${this.ageGroup} and above and the most important moral lessons were ${this.moralLessons}`);


    }
    
}
let mystory=new MyStory("one hour","Stand with your values","16yrs");
mystory.getDetailsOfStory();

//Create a LibraryCatalog class that handles the cataloging and management of
//books in a library. Implement methods to add new books, search for books by
//title or author, keep track of available copies, and display book details.
class LibraryCatalog{
    constructor(book){
        this.book=[]
    }
    addNewbook(){
        this.book=[{title:"Kigogo",author:"Pauline Kea",pages:286}]


    }
    displayBookDetails(){
        console.log(`${this.book.title1} was purchased on september`);


    }
}
let library=new LibraryCatalog([
    {title1:"The blossoms of the savannah",author:"Hr.Ole Kulet",pages:286},
    {title2:"Decolonise mind",author:"Ngugi wa Thiongo",pages:286},
    {title3:"River And The Source",author:"Margaret",pages:286},
    {title4:"Tumbo Lisiloshiba",author:"Dumu kayamba",pages:286}
])
library.addNewbook()
library.displayBookDetails()

//Create a FlightBooking class that represents a flight booking system. Implement
//methods to search for available flights based on destination and date, reserve
//seats for customers, manage passenger information, and generate booking
//confirmations.
class FlightBooking{
    constructor(destination,date,seats,information,booking){
        this.destination=destination
        this.date=date
        this.seats=seats
        this.information=information
        this.booking=booking
    }
    availableFlight(){
        console.log(`The fly Emirate plane will will fly in ${this.date} to ${this.destination} who ever had given ${this.booking} with ${this.information} will seat in ${this.seats} the plane will be available for you`);
    }
}
let flightBooking=new FlightBooking("Eldorect","12.july.2023","infront seats","morning travelling","morning booking")
flightBooking.availableFlight()



class Product {
  constructor(name, price, quantity) {
    this.name = name;
    this.price = price;
    this.quantity = quantity;
  }

  total_value() {
    return this.price * this.quantity;
  }
}

let product1 = new Product("Apple", 0.5, 10);
let product2 = new Product("Banana", 0.25, 20);
let product3 = new Product("Orange", 0.75, 5);

let total_value1 = product1.total_value();
let total_value2 = product2.total_value();
let total_value3 = product3.total_value();

let total_value_all = total_value1 + total_value2 + total_value3;
console.log(total_value_all);