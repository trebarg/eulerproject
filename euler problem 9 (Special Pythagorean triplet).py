##print((3*3) + (4*4)==(5*5))

sumCheck = 1000
i = 1

while i < 1000:

        a = i
        remainderOne = sumCheck - i
        
        n = 1
        while n < remainderOne:
                b = n

                remainderTwo = remainderOne - n



                c = remainderTwo 
                if ((a*a) + (b*b)==(c*c)) and (a<b<c):
                        print(str(a) + " " + str(b) + " " + str(c) + " " + str(a+b+c))
                        print(a*b*c)
                n += 1

        i += 1






        

        
##        b = i + 1
##        c = i + 2
##        print(str(a) + " " + str(b) + "  " + str(c))
##        if ((a*a) + (b*b)==(c*c)):
##                print(str(a) + " " + str(b) + "  " + str(c))
##                break

