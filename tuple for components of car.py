tuple1=("engine","wheels","horn")
print(tuple1)
#length
print(len(tuple1))
#adding
tuple1=tuple1+("airbag","sidemirror","seatbelt")
print(tuple1)
#concatenation
tuple2=("steering","bumper","rearview")
tuple=tuple1+tuple2
print(tuple)
#indexing
print(tuple1[2])
print(tuple1[-3])
#slicing
print(tuple1[0:2])
print(tuple1[2:4])
#repitition
print(tuple1*2)
#membership test
print("airbag"in tuple1)
print("door" in tuple1)
#delete operation
del tuple1


