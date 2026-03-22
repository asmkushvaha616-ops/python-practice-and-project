# WAP to detect double space in a string
name="Harry is a  good boy"
print(name.find("  "))#if it give -1 then there is not double space 
print(name.find("   "))#if it give -1 then there is no use of triple quote in above string
print(name.find("g"))#find function return the index of substring in parent string
