#polymorphism - same piece of code behaving differently in different situation

# a = 10
# b = 20
# c = a+b

# a = 'raju'
# b = 'krishna'
# c = a+b

#so here + is behaving different in different situation
#for integers is adding two numbers
#for strings its concating
#how + is doing this
#whateevr is doing in python, its doing on objects using magic methods

a = 10
b = 20
c = a+b#whenver we do these operations bts these magic methods will call,
res = a.__add__(b)#30
print(res,c)
res = isinstance(c,int)#true

# for that check dir(int)

class Duck:
    def swim(self):
        print("The duck is swimming.")

class Albatross:
    def swim(self):
        print("The albatross is swimming.")

# Common function that works with any object having a 'swim' method
def make_swim(bird):
    bird.swim()

duck_instance = Duck()
albatross_instance = Albatross()

make_swim(duck_instance)      # Output: The duck is swimming.
make_swim(albatross_instance) # Output: The albatross is swimming.

