def String():
    print("This is all about string") # written in single or double quotes

    str = "Making a string variable"  #variable
    print(str) #writing the variable without qoute
    a = " variable 1 \n"
    b = "variable 2 which will be in next line using end function"
    print(a,b)
    print(''' For multiline string,
     we will used triple quotes as given.''') #for multiline or use '\n' for the same


    for k in "abcde": #loop in strings
        print(k)
    l ="checking the length of a string" #use len(object)
    print(len(l)) # will count the characters

    x = " when we want to find any particular word or any letter from the string we will use in as given!"
    print("or"in x) # to find any specific letter
    t = "we will use if statement now!" #conditional statement
    if "now" in t:     #use of if
        print ("agree")
        l = "now use if and else statement!"
        if "in" in l:
            print("yes")
        elif"in"in l:
            print("agree")    #use of if-else statement
        else:
            print("no")
            if "in" not in l:
                print("not")   #use of not in statement
                print(l[:8])   #start from the zero automaticall without give start value
                print(t[4:])   #with end range statement will be till end
                print(l[2:9])  #will print from 0 to 8
                print(l[-10:-1])   #reverse slicing or indexing it will count from opposite till 9th letter from last letter

                name= "anshika"
                print(name.upper())

                course = "  MCA  "
                print(course.lower())  # lowercase print(course.strip())  #will remove unwanted space

                split = "hello dear"
                print(split.split())       #writing both word seperately
                print(split.replace("h","H"))     #replace any word to other
                print(course+split)          #concatenated string
                print(split+ " "+course)     #for space
                print(split+ " my course is"+course)     #add something in between
                tenth = 94
                twelfth = 80
                graduation = 64
                marks = "I got {} percent in 10th,{}% in twelfth and {}% in graduation"
            print(marks.format(tenth,twelfth,graduation))
String()









