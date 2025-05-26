#Bytes
byte_data : bytes = b"Hello"
print(byte_data,type(byte_data))

#Bytearray
byte_array: bytearray = bytearray([65, 66, 67, 69]) 
print(type(byte_array), " byte_array = ", byte_array)
print(byte_array,type(byte_array))
print(byte_array[0])
print(chr(byte_array[1]))

#Memoryview
mem_view: memoryview = memoryview(b"Sajjad Sahil")
print(type(mem_view),mem_view)
print(bytes(mem_view[0:5]))
