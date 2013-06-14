######################################################
"""The program accepts 3 numbers from the user and then
it checks the three to find the greatest among the three"""


###################################################

#!/usr/bin/python
if __name__ =='__main__':
    print "Please enter 3 numbers"
    a=input("\nEnter the first number:\t")
    b=input("\nEnter the seond number\t")
    c=input("\nEnter the third number\t")
    print ("\nThe numbers entered are: " +repr(a) +","+repr(b)+"," +repr(c)+"\n")
    no=a
    if no<b:
        no=b
    if no<c:
        no=c
    print (" greatest number is " +repr(no))
