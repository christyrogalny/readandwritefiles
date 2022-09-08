def main():
    outfile = open('philosophers.txt','w')

    outfile.write('John Locke' + '\n')
    outfile.write('David Hume' + '\n')
    outfile.write('Edmund Burke' + '\n')
    #these can also be written like this
    #outfile.write('John Locke\n')

    outfile.close()


main()

