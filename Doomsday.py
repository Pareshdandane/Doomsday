def dayOfTheWeek(year,month,day):
	sum=int(day)-doomsDateOfMonth(year,month)+centuryCode(year)+magic(year)
	remainder=sum%7
	return doomsDay(remainder)



def is_Leap(year):
	if ((year%400==0) or ((year%4==0) and (year%10!=0))):
		return True
	return False	 	


def doomsDay(remainder):
	if remainder ==0:
		return "SUNDAY"
	if remainder ==1:
		return "MONDAY"
	if remainder ==2:
		return "THUESDAY"
	if remainder ==3:
		return "WEDNESDAY"
	if remainder ==4:
		return "THURSDAY"
	if remainder ==5:
		return "FRIDAY"
	return "SATURDAY"					

def doomsDateOfMonth(year,month):
	if month ==1:
		if is_Leap(year):
			return 4
		return 3	
	if month ==2:
		if is_Leap(year):
			return 29
		return 28
	if month ==3:
		return 14
	if month ==4:
		return 4
	if month ==5:
		return 9
	if month ==6:
		return 6
	if month ==7:
		return 11	
	if month ==8:
		return 8
	if month ==9:
		return 5	
	if month ==10:
		return 10
	if month ==11:
		return 7
	return 12		

def centuryCode(year):
	if is_Leap(year):
		return 2
	if year%400 in range(0,99):
		return 2
	if year%400 in range(100,199):
		return 0
	if year%400 in range(200,299):
		return 5
	if year%400 in range(300,399):
		return 3			
	return "fuck you"



def magic(year):
	num=year%100
	num1=int(num/12)
	num2=int(num%12)
	num3=int(num2/4)
	return num1+num2+num3


year=1858
month=2
day=8
print(is_Leap(year))
print(centuryCode(year))	
print(doomsDateOfMonth(year,month))
print(magic(year))
print(dayOfTheWeek(year,month,day))