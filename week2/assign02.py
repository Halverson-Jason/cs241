# Prompt the user for a filename.
def prompt_file():
    return input("Please enter the data file: ")

# Open the requested file
def open_file(file_name):
    return open(file_name, "r")

# Read through it line by line.
def get_lines(user_file):
    rate_highest, rate_lowest = 0.0, 1.0
    rate_sum,rate_count = 0,0
    rate_highest_line,rate_lowest_line = "",""

    # Ignore the first line, as it contains header information.
    for line in user_file[1:]:
        data = line.split(",")
        # Find the column for comm_rate and keep track of it as needed. (You may assume the file will have a consistent ordering of columns.)
        if float(data[6]) > rate_highest:
            rate_highest = float(data[6])
            rate_highest_line = data.copy()
        elif float(data[6]) < rate_lowest:
            rate_lowest = float(data[6])
            rate_lowest_line = data.copy()
        rate_sum += float(data[6])
        rate_count +=1
    rate_average = rate_sum / rate_count
    print("\nThe average commercial rate is: {}\n".format(rate_average))
    
    #TODO: remove these and place then in the appropriate place
    print_highest_rate(parse_rate(rate_highest_line))
    print_lowest_rate(parse_rate(rate_lowest_line))

#parses the line into a rate dictionary
def parse_rate(data):
    rate = {'Company': data[2], 'Zip': data[0], 'State': data[3], 'Rate': float(data[6]) }
    return rate

#prints the lowest rate
def print_lowest_rate(rate):
    #TODO: refactor the parsing of data
    # company_name_lowest = rate[2]
    # zip_lowest = rate[0]
    # state_lowest = rate[3]
    # final_rate_lowest = float(rate[6])
    print("The lowest rate is:\n",rate['Company']," (",rate['Zip'],", ",rate['State'],") - $",rate['Rate'])

#prints the highest rate
def print_highest_rate(rate):
    # company_name_highest = rate[2]
    # zip_highest = rate[0]
    # state_highest = rate[3]
    # final_rate_highest = rate[6]
    print("The highest rate is:\n",rate['Company']," (",rate['Zip'],", ",rate['State'],") - $",rate['Rate'])
    


def main():
    f_open=open_file(prompt_file())
    f_lines = f_open.readlines()
    get_lines(f_lines)
    f_open.close()


# After parsing through the complete file, display the average (mean) commercial rate across all zip codes.

# Display the utility company, zip code, state, and rate for the zip code with the highest commercial rate in the file.

# Display the utility company, zip code, state, and rate for the zip code with the lowest commercial rate in the file.

if __name__ == "__main__":
    main()