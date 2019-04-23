def prompt_filename():
    return input("Enter file: ")
    
def check_word(word):
    if word == "pride":
        return 1
    else:
        return 0

def get_lines(user_file):
    word_counter = 0
    for line in user_file:
        words = line.split()
        for word in words:
            word_counter += check_word(word)

    return word_counter

def parse_file(filename):
    f = open(filename, "r")
    return get_lines(f)

def main():
    filename = prompt_filename()
    print("Opening file '%s'" % filename)
    parse_file(filename)
    word_count = parse_file(filename)
    print("The word pride occurs %d times in this file" % word_count)

if __name__ == "__main__":
    main()