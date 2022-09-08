def main():
    infile = open('clients.txt','r')

    count = 1

    for line in infile:
        print(count, ". ", line.strip(), sep = '') #sep = '' takes away the space after the number
        count += 1

    infile.close()

main()