while True:
	try:
		budget = float(input("Enter your budget : "))
		s = budget
	except ValueError:
		print("PRINT NUMBER AS A AMOUNT")
		continue
	else:
		break
a ={"n":[], "q":[], "p":[]}
b = list(a.values())
name = b[0]
quantity = b[1]
price = b[2]
while True:
	try:
		ch = int(input("1. Add a product\n 2.Exit \nEnter your choice : "))
	except ValueError:
		print("\nERROR: Choose only digits from the given option")
		continue
	else:
		if ch == 1 and s>0:
			product_name = input("Enter product name : ")
			quant = input("Enter quantity : ")
			pric = float(input("Enter price of the product : "))
			if pric>s:
				print("can't add the product")
				continue

			else:
				if product_name in name:
					ind = name.index(product_name)
					quantity.remove(quantity[ind])
					price.remove(price[ind])
					quantity.insert(ind, quant)
					price.insert(ind, pric)
					s = budget-sum(price)
					print("amount left", s)
				else:
					name.append(product_name)
					quantity.append(quant)
					price.append(pric)
					s = budget-sum(price)
					print("amount left", s)
		elif s<= 0:
			print("NO BUDGET")
		else:
			break
print("Amount left : Rs.", s)
if s in price:
	# then printing the name of the product which can buy
	print("\nAmount left can buy you a", name[price.index(s)])

print("\n\n\nGROCERY LIST")

# print final grocery list
for i in range(len(name)):
	print(name[i], quantity[i], price[i])
