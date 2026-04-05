exchange_rates = {"USD": 1.0, 
                  "EUR": 0.85, 
                  "JPY": 110.0, 
                  "GBP": 0.75, 
                  "INR": 94.0, 
                  "AUD": 1.35, 
                  "CAD": 1.25, 
                  "KRW": 1150.0, 
                  "CNY": 6.5, 
                  "SEK": 8.5}
amount = float(input("Enter the amount to convert: "))
from_currency = input("Enter the currency to convert from (e.g., USD, EUR, JPY, GBP, INR, AUD, CAD, KRW, CNY, SEK): ").upper()
to_currency = input("Enter the currency to convert to (e.g., EUR, USD, JPY, GBP, INR, AUD, CAD, KRW, CNY, SEK): ").upper()
usd_bridge = amount / exchange_rates[from_currency]
final_amount = usd_bridge * exchange_rates[to_currency]
print(f"{amount} {from_currency} is equal to {final_amount:.1f} {to_currency}.")

