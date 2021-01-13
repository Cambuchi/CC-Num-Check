#! python3
# ccNumCheck.py - function to validate credit card numbers using algorithm for Luhn formula
# also checks if credit card is amex, visa, or mastercard, validation is easy to add other
# card types.

def cc_type_check(input_cc):
    # Check that the credit card matches the styling of major credit cards.
    visa = {'prefix': [4], 'length': [13, 16]}
    master_card = {'prefix': [51, 52, 53, 54, 55], 'length': [16]}
    american_express = {'prefix': [34, 37], 'length': [15]}

    if (int(input_cc[0]) in visa['prefix']) and (len(input_cc) in visa['length']):
        print("This number is in a VISA style format.")
        return True
    elif (int(input_cc[0:2]) in master_card['prefix']) and (len(input_cc) in master_card['length']):
        print("This number is a MASTERCARD style credit card.")
        return True
    elif (int(input_cc[0:2]) in american_express['prefix']) and (len(input_cc) in american_express['length']):
        print("This number is a AMERICAN EXPRESS style credit card.")
        return True
    else:
        return False


def cc_num_check(input_cc):
    # clean up any spaces around the credit card input
    cc_clean = ''.join(input_cc.split())
    # first check if credit card matches major card company format
    # begin Luhn check if cc format check returns True
    if cc_type_check(cc_clean):
        # step 1: reverse the credit card number order
        luhn_base = list(cc_clean[::-1])
        # step 2: double the value in every other number starting at the 2nd number
        for i in range(1, len(luhn_base), 2):
            luhn_base[i] = str(int(luhn_base[i]) * 2)
        # step 3: add up all of the individual numbers to make a total sum
        total = 0
        for num in luhn_base:
            total += int(num)
        # step 4: if total sum an integer multiple of 10, then it is a valid CC number
        if total % 10 == 0:
            print('This is a valid credit card number.')
        else:
            print('This is not a valid credit card number')


if __name__ == '__main__':
    cc_num = input('Please enter a credit card number to check: \n')
    cc_num_check(cc_num)
