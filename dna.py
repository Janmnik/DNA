# 00 -> A
# 01 -> G
# 10 -> C
# 11 -> T

String = "0b00011011"

String = input("Podaj ciąg binarny: ")

String[:2]
String[2:4]
String[4:6]
String[6:8]
def Convert():
    for x in range(0, len(String), 2):
        if(String[x:x+2]=="00"):
            print("A")
        elif (String[x:x+2]=="01"):
            print("G")
        elif (String[x:x+2]=="10"):
            print("C")
        elif (String[x:x+2]=="11"):
            print("T")
        


def switch(num):
    dict={
        '0b': '',
        '00': 'A',
        '01': 'G',
        '10': 'C',
        '11': 'T'
    }
    return dict.get(num, 'Invalid DNA')
    
s=''
for x in range(0, len(String), 2):
    s+=switch(String[x:x+2])

Convert()
print(s)
