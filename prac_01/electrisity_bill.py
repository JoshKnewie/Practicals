print("Electricity bill estimater")

TARRIFF_11 = 0.244618
TARRIFF_31 = 0.136928
user_tariff = input("Which tariff? 11 or 31:")
if user_tariff == 11:
    cents_per_kwh = TARRIFF_11
elif user_tariff == 31:
    cents_per_kwh = TARRIFF_31
daily_kwh_use = float(input("What is your daily kwh usage? "))
days_of_billing = float(input("How many days of billing? "))
cost_per_day = cents_per_kwh * daily_kwh_use
total_price = cost_per_day * days_of_billing
print("Estimated bill: $", total_price)
