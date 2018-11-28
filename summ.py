def get_summ(param_1, param_2):
	summ_string = param_1 + " " + param_2
	return f"Result is {summ_string}"

one = "Learn"
two = "python"
print(get_summ(one, two).upper())