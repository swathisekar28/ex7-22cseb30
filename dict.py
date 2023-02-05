my_dict={"processor":"Intel Core i5","memory":"4 GB","OS":"windows 10"}
print("initial dictionary: ",my_dict)
my_dict["hard drive"]="80 GB hard drive space"
print("dictionary after adding an element: ",my_dict)
my_dict["OS"]="windows 11"
print("dictionary after OS value changed: ",my_dict)
print("accessing elements from dict: ",my_dict["processor"])
del my_dict["memory"]
print("dictionary after removing elements: ",my_dict)
