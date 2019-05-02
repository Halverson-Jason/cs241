def prompt_file():
    file_name = input("Enter file: ")
    return file_name

def read_file_lines(file_name):
    file_to_check = open(file_name)
    number_lines = 0
    for line in file_to_check:
        number_lines += 1
    file_to_check.close()
    return number_lines


def read_file_words(file_name):
    file_to_read = open(file_name)
    words_count = 0
    for line in file_to_read:
        words_count += len(line.split())
    file_to_read.close()
    return words_count

def main():

    enter_file = prompt_file()
    words_counter = read_file_words(enter_file)
    line_counter = read_file_lines(enter_file)

    print("The file contains " + str(line_counter) + " lines and " + str(words_counter) + " words.")


if __name__ == "__main__":
    main()