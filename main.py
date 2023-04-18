with open("input_Letters.txt") as file:
    input_letters = file.read()


def findHighestConsecutive(input_letter):
    # variables to keep track of current letter and it's count
    current_letter = None
    current_letter_count = 0
    # variables to keep track of highest consecutive letter and it's count
    consecutive_letter = None
    consecutive_letter_count = 0

    # iterate over the input string to each letter with the current letter in the count
    for letter in input_letter:
        # base-case to initialize first letter and count
        if letter == current_letter:
            current_letter_count += 1
        else:
            # check if the current letter count is the longest
            if current_letter_count > consecutive_letter_count:
                consecutive_letter = current_letter
                consecutive_letter_count = current_letter_count
            current_letter = letter
            current_letter_count = 1

    # for the last iteration
    if current_letter_count > consecutive_letter_count:
        consecutive_letter = current_letter
        consecutive_letter_count = current_letter_count

    return f"{consecutive_letter} : {consecutive_letter_count}"


highest_consecutive_letter = findHighestConsecutive(input_letters)
print(highest_consecutive_letter)  # outputs k : 3
