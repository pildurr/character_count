loan = round(int(input("Please enter the loan amount in $: ")))
payment = 50.0
loan_original = loan
month = 0
interest_over_1000 = 0.02
interest_under_1000 = 0.015
sum_of_interest = 0.0

while loan >= 0.0 and loan < 2500.0:
    if loan_original > 1000.0:
        interest_paid = loan * interest_over_1000
        remaining_debt = loan - payment + interest_paid
        loan = remaining_debt
        sum_of_interest += interest_paid
        if remaining_debt < 0.0:
            payment = payment + remaining_debt
            remaining_debt = 0.0
    elif loan_original <= 1000.0:
        interest_paid = loan * interest_under_1000
        remaining_debt = loan - payment + interest_paid
        loan = remaining_debt
        sum_of_interest += interest_paid
        if remaining_debt < 0.0:
            payment = payment + remaining_debt
            remaining_debt = 0.0
    month += 1
    print("Month ", month, "Payment ", round(payment, 2), "Interest paid: ", round(interest_paid, 2), "Remaining debt: ", round(remaining_debt, 2))
print("")
print("Number of months: ", month)
print("Total interest paid: ", round(sum_of_interest, 2))