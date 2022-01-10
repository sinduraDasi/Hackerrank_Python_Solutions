The included code stub will read an integer, , from STDIN.

Without using any string methods, try to print the following:
1234...n
Output Format
n=5
12345

****SOLUTION*****
if __name__ == '__main__':
    n = int(input())
    for  i in range(n):
        print(i+1, end = "")
