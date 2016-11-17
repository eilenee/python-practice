length = float(raw_input ('length of the room in feet: '))
width = float(raw_input ('width of the room in feet: '))
cost_per_yard = float(raw_input ('cost per square yard: '))
area_feet = length * width
area_yards = area_feet / 9.0
total_cost = area_yards * cost_per_yard
print 'The area is', area_feet, 'square feet.'
print 'That is', area_yards, 'square yards.'
print 'Which will cost', total_cost
