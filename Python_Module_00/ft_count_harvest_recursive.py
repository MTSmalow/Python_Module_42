def cont_recur(aday, ldays):
	if aday > ldays:
		print("Harvest time!")
	else:
		print("day", aday)
		cont_recur(aday+1 , ldays)

def ft_count_harvest_recursive():
	ldays = int(input("Days until harvest: "))
	cont_recur(1, ldays)