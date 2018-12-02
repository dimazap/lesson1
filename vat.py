def get_vat(payment, percent):
	try:
		payment = float(payment)
		percent = int(percent)
		vat = payment / 100 * percent
		vat = round(vat, 2)
		return f"VAT amount: {vat}"
	except (TypeError, ValueError):
		return "Can't calculate"

result = get_vat(400, "19")
print(result)