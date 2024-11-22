from io import StringIO

#f = StringIO()
#f.write("hello")
#print(f.getvalue())
#f.write(" ")
#print(f.getvalue())
#f.write("world")
#print(f.getvalue())

f = StringIO("Hello Dx!!!")
str = f.read()
print(str)