txt_file = open('zad8.txt', 'w')
txt_file.writelines([str(number)+'\n' for number
in range(1, 10)])

txt_file.flush()

txt_file_read = open('zad8.txt', 'r')
print(txt_file_read.read())

txt_file_read.close()
txt_file.close()