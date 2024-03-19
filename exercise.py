#  tuples
my_tuple = ("wilfred","kibet", "koech")
print(my_tuple)
my_other_tuple = ("I","am","Kenyan")
my_tuple +=my_other_tuple
print(my_tuple)



#Dictionaries
Bucket_list = {
    "Monday":"swiming",
    "Tuesday":"jogging",
    "Wednesday":"bowling",
    "Thursday":"hiking",
    "Friday":"skating"
    }
print(Bucket_list)
del Bucket_list["Monday"]
print(Bucket_list)
x = Bucket_list.get("Thursday")
print(x)


def list_to_dictionary(fruits,stationery):
    return dict(zip(fruits,stationery))
fruits = ["banana", "apple", "mango"]
stationery = ["pen","pencil","eraser"]
Dictionary = {
    "fruits" : fruits
    ,"stationery" : stationery
}
print(Dictionary)




# Sets
fruits = {"banana", "apple", "pear"}
print(fruits)
fruits.add("orange")
print(fruits)

fruits.remove("orange")
print(fruits)