

def equal_string(one,two):
    data_data = 0
    if isinstance(one,str) and isinstance(two,str) and len(one) != len(two):
       data_data = 0
    if isinstance(one,str) and isinstance(two,str) and len(one) == len(two):
        data_data = 1
    elif isinstance(one,str) and isinstance(two,str) and len(one) > len(two):
        data_data = 2
    if isinstance(one,str) and isinstance(two,str) and len(one) != len(two) and two == "learn":
        data_data = 3             
    return print(data_data)

equal_string("Один","learndawadaw") 
equal_string("Один","Один") 
equal_string("Один","learn")     
equal_string("Одинdadawdawda","learndawdaw")