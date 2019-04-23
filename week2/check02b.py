def prompt_file():
    return input("Enter file: ")

def open_file(file_name):
    return open(file_name, "r")
    
def get_lines(user_file):
    line_counter = 0
    word_counter = 0
    for line in user_file:
        word_counter += len(line.split())
        line_counter += 1
    word_line_count = [line_counter,word_counter]
    return word_line_count

def main():
    user_file = open_file(prompt_file())
    word_line_count = get_lines(user_file)
    print("The file contains %d lines and %d words." % (word_line_count[0], word_line_count[1]))
    user_file.close()
if __name__ == "__main__":
    main()