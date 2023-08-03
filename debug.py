from lib.animal import Animal
from lib.zoo import Zoo

if __name__ == '__main__':
    print("WELCOME TO THE ZOO! :) let's debug :vibing_potato:")

    SanDiego_Zoo = Zoo('SanDiego_Zoo',"California")
    print(SanDiego_Zoo.name)




# e.g.  

# z1 = Zoo( 'Micke Grove Zoo', 'Lodi, CA' )
# a1 = Animal( 'Lion', 75, 'Luke', z1 )






# ipdb allows us to stop our code & test stuff
# import ipdb; ipdb.set_trace()
print( 'Thanks for visiting the zoo!' )