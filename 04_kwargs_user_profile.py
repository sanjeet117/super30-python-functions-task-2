'''
Create

def create_profile(**kwargs)

that accepts dynamic user information and prints all provided attributes.
'''
def create_profile(**kwargs):
    print('User profile')
    for key,value in kwargs.items():
        formated_key = key.replace('_','').title()
        print(f'{key} : {value}')

create_profile(name = 'Shivansh',age = 7,role = 'student',is_active = True)

#**kwargs collects all passed keyword arguments into a Python dictionary. Calling .items() loops through 
# each (key, value) pair to print them dynamically.