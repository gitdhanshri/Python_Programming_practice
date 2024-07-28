def fiibbonacci_series():
	max=int(input("Enter the lenght of series"));
	n1=0;
	n2=1;
	if max==1:
		print(n1);
	elif(max==2):
		print(n1,n2,end=" ");
	else:
		print(n1,n2,end=" ");
		for i in range(1,max-1):
			#temp=n2;
			n3=n1+n2;
			print(n3,end="  ");
			n1=n2;
			n2=n3;
		
#function call
fiibbonacci_series();
