import re


#validate mobile number with 7 or 8

mobile_num_pattern=r"^[7-9]{1}[0-9]{9}$"
input="9539512581"
op=re.match(mobile_num_pattern,input)
print(op)


#strong username
#strongpassword
#strong email
# 1.uc,lc,dgits,_ 5-15
username_pattern=r"^[A-Za-z0-9_]{5,15}$"
ip="ABGJJHK_"
op=re.match(username_pattern,ip)
print(op)

# 1.atleast one uc
# 2.atleast one lc 
# 3.atleast one digit
# 4.allow _@
# 5.length 7 to 12

#to define atleast one presence from a uc group

# ^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])[A-Za-z0-9@_]{7,12}$
password_pattern=r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])[A-Za-z0-9@_]{7,12}$"
ip="kuMarkumar1"
op=re.match(password_pattern,ip)
print(op)


email = "harish.tech@gmail.com"

if re.match(r"^[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]{2,}$", email):
    print("Valid Email")
else:
    print("Invalid Email")
