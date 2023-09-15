test_dictionary = {'Key1': 'Value1', 'Key2':'Value2'}

print(test_dictionary)

del test_dictionary['Key2']

print(test_dictionary)

test_dictionary['Key1'] = 'value1'


print(test_dictionary)

s = "42"

def check_numeric(s):
            if(s.isnumeric()):
                return print(int(s))
        
check_numeric(s)