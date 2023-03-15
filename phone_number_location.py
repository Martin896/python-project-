while True:

	import phonenumbers as pn
	from phonenumbers import geocoder
	a = input('Enter a phone number with country code: \n')
	phonenumber = pn.parse(a)

	print(geocoder.description_for_number(phonenumber, 'en'))

