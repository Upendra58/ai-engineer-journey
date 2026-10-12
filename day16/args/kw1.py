def show_profile(**kwargs):
    for key,value in kwargs.items():
        print(key,":",value)

show_profile(name= "Upendra", age = 25, role="AI Engineer")