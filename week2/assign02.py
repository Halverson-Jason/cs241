# Prompt the user for a filename.
def prompt_file():
    return input("Please enter the data file: ")

# Open the requested file
def open_file(file_name):
    return open(file_name, "r")

# Read through it line by line.
def get_lines(user_file):
    rate_lowest = 1.0
    rate_highest = 0.0
    rate_sum = 0
    rate_count = 0
    rate_highest_line = []
    rate_lowest_line = []

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

    lowest_rate = rate_lowest_line
    company_name_lowest = lowest_rate[2]
    zip_lowest = lowest_rate[0]
    state_lowest = lowest_rate[3]
    final_rate_lowest = float(lowest_rate[6])

    highest_rate = rate_highest_line
    company_name_highest = highest_rate[2]
    zip_highest = highest_rate[0]
    state_highest = highest_rate[3]
    final_rate_highest = highest_rate[6]

    print("The highest rate is:\n{} ({}, {}) - ${}\n".format(company_name_highest,zip_highest,state_highest,final_rate_highest))
    print("The lowest rate is:\n{} ({}, {}) - ${}".format(company_name_lowest,zip_lowest,state_lowest,final_rate_lowest))


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