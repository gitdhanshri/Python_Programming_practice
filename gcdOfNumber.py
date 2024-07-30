# find  all factors of Number
def all_Factor(num):
	l1=[];
	if(num<1):
		print("Number is Zero!!!!");
		return 0;
	elif(num>0):
		for i in range(1,num+1):
			if(num%i==0):
				l1.append(i);
			
	return l1;	
# finding gcd of Two Numbers	
def find_gcd_of_twoNumver(n1,n2):
	num1=all_Factor(n1);
	num2=all_Factor(n2);
	while(num1!=[] and num2!=[]):
		a=num1.pop();
		b=num2.pop();
		if(a==b):
			return a;
		
		elif(a<b):
			num1.append(a);
		elif(a>b):
			num2.append(b);
	return 1;
# finding gcd of  whole list
def gcdof_list(list1):
	gcd=1;
	gcd_curr=1;
	while(list1!=[]):
			a=list1.pop();
			if(list1==[]):
				print("gcd-->",a);
				return find_gcd_of_twoNumver(gcd_curr , a);
			b=list1.pop();
			gcd_curr=find_gcd_of_twoNumver(a,b);
			#print("gcd-->",gcd_curr);
			gcd=gcd_curr;
			list1.append(gcd_curr);

	
	#print("gcd of list--->",gcd);
	return gcd;	
list2=[125,750,100,10,120,200,20];
ans=gcdof_list(list2);
print("gcd of list---->",ans);



























