from math import floor
 
 
def sum_func(num1, num2):
    result = ""
    longest = num1
    minimum = num2
 
    if num2 > num1:
        longest = num2
        minimum = num1
 
    carry = 0
    index = len(longest)-1
 
    for j in range(len(minimum) -1, -1, -1): #OJO, arreglar ITERAR EL MAS CHICO
        if (index >= 0):
            sum_aux = int(longest[index]) + int(minimum[j]) + carry
            if sum_aux < 10:
                result = str(sum_aux) + result
                carry = 0
            else:
                carry = 1
                result = str(sum_aux % 10) + result
        index -= 1
 
    if carry == 0:
        #concateno lo que me queda de la lista
        result = longest[0:index+1] + result
    else:
        # iterar el resto del numero
        for i in range(index, -1, -1):
        # for resto del numero
            if carry == 0:
                result = longest[i::] + result
                break
            else:
                sum_aux = int(longest[i]) + carry
                if i > 0:
                    if sum_aux < 10:
                        result = str(sum_aux) + result
                        carry = 0
                    else:
                        carry = 1
                        result = str(sum_aux % 10) + result
                else:
                    result = str(sum_aux) + result
 
        # carry == 0 salgo(concateno el resto del numero)
        # carry != 0 obtengo numero con indice, sumo carry y actualizo si hay nuevo carrry
 
    return result
 
 
 
 
 
 
 
def solution(S1, S2):
    sum = ""
    list_sum = []
    list_1 = S1.split(" ")
    list_2 = S2.split(" ")
 
    for i in range(len(list_1)):
        #list_sum.insert(i, str(int(list_1[i]) + int(list_2[i])))
        list_sum.insert(i, sum_func(list_1[i], list_2[i]))
 
    sum = " ".join(list_sum)
 
    return sum
 
#print(solution("123456789012345678901 23456789", "12345678 234567890123456789012"))
print(solution("99999123456", "923456"))
