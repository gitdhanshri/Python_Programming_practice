def half_plus_mainus_pattern(n):
	n+=1; #3
	k=n-1;
	for i in range(n):
		for j in range(n):
			if((i+j)/k==1):
				print("+" ,end="  ");
			elif(i==j==(n-1)):
				print("*",end=" ");
			else:
				print(" ",end="  ");
		for j in range(1,n):
			if(i==j):
				print("+",end="  ");
			elif(i==j==(n-1)):
				print("*",end=" ");
			else:
				print(" ",end="  ");
		print();

	for i in range(1,n):
		for j in range(n):
			if(i==j):
				print("-",end="  ");
			else:
				print(" ",end="  ");
		for j in range(1,n):
			if((i+j)/k==1):
				print("-" ,end="  ");
			else:
				print(" ",end="  ");
		print();

	
half_plus_mainus_pattern(5);
def plus_pattern_2(n):
	n+=1; #3
	k=n-1;
	for i in range(n):
		for j in range(n):
			if((i+j)/k==1):
				print("+" ,end="  ");
			elif(i==j==(n-1)):
				print("*",end=" ");
			else:
				print(" ",end="  ");
		for j in range(1,n):
			if(i==j):
				print("+",end="  ");
			elif(i==j==(n-1)):
				print("*",end=" ");
			else:
				print(" ",end="  ");
		print();

	for i in range(1,n):
		for j in range(n):
			if(i==k and j==k):
				print(" - ",end=" ");
			elif(i==j):
				print("+",end="  ");
			else:
				print(" ",end="  ");
		for j in range(1,n):
			if((i+j)/k==1):
				print("+" ,end="  ");
			elif(i==(n-1) and j==(0)):
				print("-",end="  ");
			else:
				print(" ",end="  ");
		print();

	
plus_pattern_2(5);
'''plus_pattern(5);
plus_pattern(6);
plus_pattern(7);
plus_pattern(8);
plus_pattern(9);
plus_pattern(10);'''
