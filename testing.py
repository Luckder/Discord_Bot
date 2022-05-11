import csv

booklist = []
prevbook = "Book Name"
books = f""

with open("kjv.csv", 'r') as f:
    mycsv = csv.reader(f)

    for row in mycsv:
        if row[1] != prevbook:

            booklist.append(row[1])
            prevbook = row[1]

    for i, j in enumerate(booklist):
        books += f"{i+1}){j} "

    print(books)


        