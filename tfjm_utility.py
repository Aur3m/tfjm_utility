def bubblesort(number):
    for i in range(len(number)):
        if int(number[i+1])<int(number[i]):
            number[i+1],number[i]=number[i],number[i+1]
    return number

def worst_bubble_situtation_gen(l):
    final = ""
    for i in range(int(l)):
        final += str(i+1)
    return final

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

n=input("entrez un 'n' personnalisé sous forme de nombre")
print(
    "Pour n = 2 :", count_permutations("12"),"\n",
    "Pour n = 3 :", count_permutations("123"),"\n",
    "Pour n = 4 :", count_permutations("1234"),"\n",
    "Pour n = 5 :", count_permutations("12345"),"\n")

print("Pour n = 6 :", count_permutations("123456"),"\n")

print("Pour n =",n," : ", count_permutations(worst_bubble_situtation_gen(n)))
