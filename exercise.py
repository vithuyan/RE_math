# Write code to generate a dictionary where the keys are the numbers from 1 to 50 and the values follow these rules:
#
# if the number is divisible by 2 the value should be one more than the key
# if the number is divisible by 7 the value should be one less than the key
# if the number is divisible by 2 and 7 the value should be the key multiplied by 2
# otherwise the value should be the same number as the key


dictionary = {}
key = 1
value = 1


while key  <= 50:
    dictionary[key] = value
    key += 1
    value += 1



if key % 2 == 0:
    value = key + 1

elif key % 7 == 0:
    value = key - 1


elif(key % 2 and key % 7) == 0:
            value = key * 2

else:
    value = key

print (dictionary)
