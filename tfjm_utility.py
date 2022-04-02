def bubblesort(number):
    for i in range(len(number)):
        if number[i+1]<nuber[i]:
            number[i+1],number[i]=number[i],number[i+1]
    return number

def sort_number(number):
    liste = [i for i in number]
    liste.sort(reverse = True)
    return liste

def count_permutations(number):
    if [i for i in number] == sort_number(number) :
        return 1
    else:
        final = 0
        for i in range(len(number)-1):
            if int(number[i+1]) > int(number[i]):
                final += count_permutations(number[0:i]+number[i+1]+number[i]+number[i+2::])
        return final

print(
    "Pour 12 :", count_permutations("12"),"\n",
    "Pour 123 :", count_permutations("123"),"\n",
    "Pour 1234 :", count_permutations("1234"),"\n",
    "Pour 12345 :", count_permutations("12345"),"\n",
    "Pour 123456 : ", count_permutations("123456")
)
