from orm import *


class Person(AbstractModel):
    name = CharField(length=15)
    phone = IntField()
    city = CharField(length=30)
    age = IntField()

class Book(AbstractModel):
    name = CharField(length=50)
    price = FloatField()
    category = CharField(length=30)



person = Person()
migrate(person)

person.name= 'Vasya'
person.phone= 2221516
person.age = 20
person.city = 'ZP'

test_person = insert(person)
print(test_person)

result_person2 = insert(person2)
print(result_person2)

persons = select(Person, first_name__contains='V', age__gte=20, age__lt=22)
print(persons)

book = Book()
book2 = Book()
book3 = Book()
migrate(book)

book.name = 'try'
book.category = 'comedy'
book.price = 125.00


book2.name = 'just do'
book2.category = 'dram'
book2.price = 300.00
book2.quantity = 10



result_book = insert(book)
print(result_book)

result_book2 = insert(book2)
print(result_book2)


books = select(book, quantity__gt=4, price__gte=100)
print(books)
