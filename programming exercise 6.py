import re

# defining function that validates the phone number entered
def validate_phone_number(phone_number):
    pattern = r"^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$"
    #returns wether phone number is valid or invalid
    if re.match(pattern, phone_number):
        return True
    return False


# defining function that validates the ssn entered
def validate_ssn(ssn):
    pattern = r"^\d{3}-\d{2}-\d{4}$"
    #returnes wether ssn is valid or invalid
    if re.match(pattern, ssn):
        return True
    return False


# defining function that validates the zip code entered
def validate_zip_code(zip_code):
    pattern = r"^\d{5}(-\d{4})?$"
    #returns wether zip code is valid or invalid
    if re.match(pattern, zip_code):
        return True
    return False


# Main function to get input from the user and display results
def main():
    #user inputs phone number and determines whether they are valid or invalid
    phone_number = input("Please enter a phone number: ")
    if validate_phone_number(phone_number):
        print("The Phone Number entered is valid.")
    else:
        print("The Phone Number entered is invalid.")
    #user inputs ssn and determines whether they are valid or invalid
    ssn = input("Please enter a social security number:")
    if validate_ssn(ssn):
        print("The Social Security Number entered is valid.")
    else:
        print("The Social Security Number entered is invalid.")
    #user inputs zip code and determines whether they are valid or invalid
    zip_code = input("Please enter a zip code:")
    if validate_zip_code(zip_code):
        print("The Zip Code entered is valid.")
    else:
        print("The Zip Code entered is invalid.")


# Run the main function
if __name__ == "__main__":
    main()
