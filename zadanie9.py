try:
    with open('zadanie.txt', 'r') as in_file, open('zadanie9.txt','w') as out_file:
            for line in in_file:
                out_file.write(line)
except IOError as ioe: 
    print(ioe)