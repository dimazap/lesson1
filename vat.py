def get_vat(payment, percent=19):
	try:
	payment = float(payment)
	percent = int(percent)
	vat = round(vat, 2)
	vat = payment / 100 * percent
	return "VAT amount: {}".format(vat)
except (TypeError, ValueError):
	return "Can't calculate"

result = get_vat(400, "20")
print(result)