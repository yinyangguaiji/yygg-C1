def count_words(book_name,word):
    try:
        with open(book_name,encoding='utf-8') as book:
            book1 = book.read()
    except FileNotFoundError:
        print('The file "' + book_name + '" is not be found.')
    else:
        word_number = book1.count(word)
        print(word_number)
count_words('Pride and Prejudice.txt','the')

