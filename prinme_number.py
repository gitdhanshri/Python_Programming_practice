def print_prime_Num():
	max=int(input("Eneter the number"));
	for num in range(2,max+1):
		for i in range(2,num):
			if (num%i)==0:
			     break;
		else:
			print(num);
#function call
print_prime_Num();
