# regex-->used to validate userinput with customized patterns
#fullstack-->
#data analysis-->validation,extraction,cleaning.

# methods used for validation-->match,search,find,findall,fullmatch

import re #imports the regex module.

# r"pattern"-->regex pattern will define like this
#will use methods to validate input with pattern

# 1.i will accept a string which always starts with hello otherwise i wont accept.
#match method will be useful here.
# ip1="ok some world hello input output"
# ip2="hello hyderabad"
# ip3="hello 10000coders"
# ip4="suresh hello"
# op=re.match(r"hello",ip1)
# print(op)

#match validates if match found in 
# starting only
#2.i will accept a string "hello" is present anywhere in the given string
# ip1="ok some world hello input output"
# ip2="hello world"
# ip3="welcome hello"

# op1=re.search(r"hello",ip1)
# print(op1)
# op2=re.search(r"hello",ip2)
# print(op2)
# op3=re.search(r"hello",ip3)
# print(op3)

#search is prefer when we will accept if pattern
# is present anywhere in the given string

# ip_ifsc="ICICI654123"

# x1=re.match(r"SBIN",ip_ifsc)
# if x1:
#     print("it is valid ifsc code")
# else:
#     print("it is invalid ifsc code")

# if re.match(r"SBIN",ip_ifsc):
#     print("it is valid sbi ifsc")
# elif re.match(r"ICICI",ip_ifsc):
#     print("it is valid icici ifsc code")
# elif re.match(r"HDFC",ip_ifsc):
#     print("it is a valid hdfc ifsc code")
# else:
#     print("it is invalid ifsc code")

# 1 .--->any single value
# 2.^--->should starts with
# 3.$--->ends with
# 4.[]--->range
# 5.{}--->length

# ht-->hit,hot,hat,hut

# ip1="huge the world"
# ip2="weather is too hot"
# ip3="he is having a hat"
# ip4="he lives in a hut"

# # -->he 
# # huge,home,hope,have
# op1=re.search(r"h..e",ip1)
# print(op1)

#any string with 3 continues alphabates

# ip1="xyz123@"
# ip2="123aef"
# ip3="345ok387"

# op1=re.search(r"[a-z]{3}",ip2)
# if op1:
#     print("valid input")
# else:
#     print("invalid input")

#should starts with any 3 numbers and ends with any 3 alphabates

# ip1="123xyz hello"
# ipp="123xyz"
# ip2="89ab"
# ip3="9876abc"
# ip4="9756okij"

# op=re.match(r"^[0-9]{3,}[a-z]{3,}$",ipp)
# op=re.match(r"^[4-9]{3,}[a-f]{3,}$",ipp)
# print(op)

# {m}--->denotes exact length 
# {m,}-->denotes minimum length and maximum anything
# {m,n}-->denotes both minimum and maximum


#pan card validation--->
#starts with 5 alphabates and 4 digits and again single alpahabet

pan_card_pattern=r"^[A-Za-z]{5}[0-9]{4}[A-Z]{1}$"

pc1="DLOPM7898R"
pc2="JKoko8976R"
pc3="28732kksd8"

validate=re.match(pan_card_pattern,pc2)
if validate:
    print("valid pancard number")
else:
    print("invalid pancard number")


#check phone number series
#should starts with 7 or 8 or 9
#length 10
#only numbers

