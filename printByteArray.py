def print_byte():
	c1=[10,20,30,40,50];
	res=bytearray(c1);
	res[0]=178
	res[3]=197
	for i in res:
		print(i);

#print_byte();
def list_data_type():
	l1=[10,20,-34,45,67,89,"shruti","Dhanshri"];
	for i in  l1:
		print(i);
	
	for i in range(-1,8) :
		print(l1[i]);
		
#list_data_type();
def set_print():
	s={12,34,24,45,34,34,34,34,34}
	s.update([100]);
	#for i in s:
		#print(i);
	
	fs=frozenset(s);
	
	for i in fs:
		print(i);
	fs[0]=222;
	for i in fs:
		print(i);
#set_print();
def dictonary():
	d1={"name":"shri","roll Num":2022,"java":"python"};
	for i in d1:
		print(d1[i]);
dictonary();
