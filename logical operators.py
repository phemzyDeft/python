
# if applicant has high-income AND good_credit
#    Eligible for loan

#with the logical AND operator both condition must be true
has_high_icome = True
has_good_credit = True

if has_high_icome and has_good_credit:
    print("Eligible for loan")


#with the logical OR operator at least one condition must be true
has_high_icome = True
has_good_credit = False

if has_high_icome or has_good_credit:
    print("Can still purchase for a loan")

#with the logical NOT operator it convert true to false
has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("Eligible for a loan")