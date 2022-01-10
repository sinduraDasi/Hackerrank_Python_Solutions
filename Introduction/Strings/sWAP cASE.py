You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.




************SOLUTION***********
def swap_case(s):
    updated_s = ""
    for i in s:
        if i.isupper():
            updated_s += i.lower()
        elif i.islower():
            updated_s += i.upper()
        else:
            updated_s += i
    return updated_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
