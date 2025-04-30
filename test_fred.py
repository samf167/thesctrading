from fredapi import Fred

api_key = "1c00931ee7dc4304c6bb68b72fb2d68f"
fred = Fred(api_key=api_key)

data = fred.get_series('UNRATE')
print(data.tail())

0

