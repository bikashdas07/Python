def fun():
    s = input("Enter the string: ")
    n = len(s)
    s1 = s[::-1]
    str=""
    if s1 == s:
        print("Longest palindrome is", s)
    else:
        for i in range(0, len(s)):
            sub = s[i:n]
            sub1 = sub[::-1]
            if sub == sub1:
                print("Longest palindrome is", str)
                str = str.concat(sub)
            else:
                continue
            n -= 1
        print("Longest palindrome is", str)
fun()