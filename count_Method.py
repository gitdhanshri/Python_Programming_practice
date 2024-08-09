def countGivenSuString_M1(s1,s2):
	count=0;
	len1=len(s1);
	#print(len1);
	len2=len(s2);
	print(len2);
	ans=False;
	for i in range(len1):
	         for j in range(len2):
	         	if(i<len1 and j<len2 and s1[i]==s2[j]):
	         		#print("index-->(",i,j,")");
	         		ans=True;
	         		i+=1;
	         	else:
	         		ans=False;
	         		break;
	         print();
	         if(ans==True):
	         	#print("ans--->",ans);
	         	#print("up index-->",i);
	         	count+=1;
	        
	print("SubString count--->",count);
def countGivenSuString_M2(s1,s2):
	count=0;
	len1=len(s1);
	#print(len1);
	len2=len(s2);
	#print(len2);
	ans=False;
	i=0;
	while i<len1:
		         k=i;
		         for j in range(len2):
		         	if(k<len1 and j<len2 and s1[k]==s2[j]):
		         		#print("index-->", k,j);
		         		ans=True;
		         		k+=1;
		         	else:
		         		k+=1;
		         		ans=False;
		         		break;
		         print();
		         if (ans==True):
		         	count+=1;
		         i=k;
	print("SubString count--->",count);
#without  repeatation allowed 
countGivenSuString_M2("sgggsggggsgs","gg");
#with repeatation allowed 
countGivenSuString_M1("sgggsggggsgs","gg");











