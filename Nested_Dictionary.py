

book_dictionary = {
  "Harry Potter": {
    "Author": "J.K Rowling",
    "Year": 1999
  },
  "ASOIAF": {
    "Author": "George R.R. Martin",
    "Year": 1997
  },
  "Lord of The Rings": {
  "Author": "J.R.R. Tolkien",
  "Year":1954
  }
}

def get_author(book):
  if book in book_dictionary:
    print(book_dictionary[book]["Author"])
  else:
    print("Book Not Available")

get_author("ASOIAF")  