str1 = "hello"
str2 ="hallo"

if len(str1) != len(str2):
        print("Strings sind nicht gleich")
else:
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            print("Strings sind nicht gleich")
            break