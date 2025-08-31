#Q2 PALINDROME WORDS

print('Enter your paragraph(press enter on a blank line to finish,habibi!)')
lines=[]
while True: #using the while loop to enter text in multiple lines
    line=input()
    if line=="":
        break
    lines.append(line)
paragraph=' '.join(lines)
print('your entered text is ',paragraph)
print("\n")
words=paragraph.split()
if len(words)>100:
    print("Pls check the word limit")
a=0
for word in words:
    w=word.lower()
    if w==w[::-1] and len(w)>1: #not considering single letters as palindromes and could have used reverse function also 
        print(word,"is a palindrome")
        a=a+1
if a==0:

    print("no palindrome word in para")




