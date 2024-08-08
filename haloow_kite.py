def hallow_Kite(n):
	n+=1; #3
	k=n-1;
	for i in range(n):
		for j in range(n):
			if((i+j)/k==1):
				print("*" ,end="  ");
			elif(i==j==(n-1)):
				print(j,end=" ");
			else:
				print(" ",end="  ");
		for j in range(1,n):
			if(i==j):
				print("*",end="  ");
			elif(i==j==(n-1)):
				print(j,end=" ");
			else:
				print(" ",end="  ");
		print();

	for i in range(1,n-1):
		for j in range(n):
			if(i==j):
				print("*",end="  ");
			else:
				print(" ",end="  ");
		for j in range(1,n):
			if((i+j)/k==1):
				print("*" ,end="  ");
			else:
				print(" ",end="  ");
		print();
	p=n-2;
	q=2*n-1;
	for i in range(p):
		print("",end="");
		for j in range(q):
			print("*",end="  ");
		print();  
	
hallow_Kite(8);
'''hallow_Kite(5);
hallow_Kite(6);
hallow_Kite(7);
hallow_Kite(8);
hallow_Kite(9);
hallow_Kite(10);'''
