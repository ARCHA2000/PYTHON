string1 = 'archa'
print("The original string is :" + str(string1))

a = '$'
modify = string1[0] + string1[1:].replace(string1[0], a)
print("Replaced String : " + str(modify))
