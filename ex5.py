_name = 'Zed A. Shaw'
_age = 27 # not a lie
_height = 74 # inches
_weight = 180 # lbs
_eyes = 'Blue'
_teeth = 'White' 
_hair = 'Brown'
lbs = _weight
kilo = lbs / 2.2
euro = _height
centimeters = euro * 2.52

print ("Let's talk about %s." % _name)
print ("He's %d inches tall." % _height)
print ("He's %d pounds heavy." % _weight)
print ("Actually that's not too heavy.")
print ("He's got %s eyes and %s hair." % (_eyes, _hair))
print ("His teeth are usually %s depending on the coffee." % _teeth)

# this line is tricky, try to get it exactly right
print ("If I add %d, %d, and %d I get %d." %(_age, _height, _weight, _age + _height + _weight))

print ("_name %s weighs %.0f kilos." % (_name, kilo))
print ("_name %s is about %.0f in cm." % (_name, euro))

# These are all formatters, they tell python to take tge variable on the right and put it in to replace the %s values
#%s - String (or any object with a string representation, like numbers)

# %d - Integers

# %f - Floating point numbers

# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

# %x/%X - Integers in hex representation (lowercase/uppercase)


