def calliingFun(text,style):
	if(style=='s' or style=='S'):
		print("small case");
		smallerCase(text);
	elif(style=='u' or style=='U'):
		print("ultered case");
		ulteredtext(text);
	elif(style=='c' or style=='C'):
		print("ulppercase");
		capitaliZe(text);
	elif(style=='r' or style=='R'):
		print("Reeverse");
		reverseText(text);	
	print();	
			
def smallerCase(text):
	len1=len(text);
	for i in range(len1):
		ch=text[i];
		if(ch.isalpha()):#check character  is alphabet or not
			if(ch.islower()): #if it is in lower then convert to upper
				print(ch,end="  ");
			else:
				res_char=	converLower(ch);
				print(res_char,end="  ");
		else:
			print(text[i],end="  ");
def converLower(letter):
	ascii_val=ord(letter);
	if(ascii_val>=65 and ascii_val<=90):
		ascii_val+=32;
		ch=chr(ascii_val);
	elif (ascii_val>=97 and ascii_val<=122):
		ascii_val-=32;
		ch=chr(ascii_val);
	return ch;
def capitaliZe(text):
	len1=len(text);
	list1=list(text);
	for i in range(len1):
		ch=list1[i]
		if(ch.isidentifier()):
			print(ch.title(),end=" ");
		else:
			print(ch,end=" ");
	print();
	print();
def reverseText(text):
	#convert String into List so that we can iterate it
	text=list(text);
	start=0;
	end=len(text)-1;
	while (start<end):
		#swapping 2 alphabets
		a=text[end];
		text[end]=text[start];
		text[start]=a;
		start+=1;
		end-=1;
	i=0;
	#Convert that list into String Format
	res="";
	while(i<len(text)):
		res+=text[i];
		i+=1;	
	print(res);
def ulteredtext(text):
	len1=len(text);
	for i in range(len1):
		ch=text[i];
		if(i%2==0 and ch.isalpha()):#check character  is alphabet or not and index should even
			if(ch.islower()): #if it is in lower then convert to upper
				res_char=	converLower(ch);
				print(res_char,end="  ");
			else:
				print(text[i],end="  ");
		elif(i%2==1 and ch.isalpha()):
			if(ch.isupper()): #if it is in lower then convert to upper
				res_char=	converLower(ch);
				print(res_char,end="  ");
			else:
				print(text[i],end="  ");
		else:
			print(text[i],end="  ");
text="#if@it34thq2736~!_)())a";

calliingFun(text,"c");
calliingFun(text,"C");
print();
calliingFun(text,"s");
calliingFun(text,"S");
print();
calliingFun(text,"u");
calliingFun(text,"u");
print();
calliingFun(text,"r");
calliingFun(text,"R");
