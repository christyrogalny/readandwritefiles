def main():
    infile = open('philosophers.txt','r')


###readline prints spaces between each line of the output while read is just each line###

    #file_contents = infile.read()
    
    line1 = infile.readline().rstrip('\n') ##the .rstrip('\n') strips the \n from it##
    line2 = infile.readline().rstrip('\n')
    line3 = infile.readline().rstrip('\n')

    print(line1)
    print(line2)
    print(line3)

main()

#dont have to close the file because we are not writing to it
#when writing you have to close the file
#just reading the file you dont have to close the file