#  Cliff Makanda, Viagogo Assignment 
#  Contact : cmm9@williams.edu or + 1-413-346-3247
#  A python method that generates seed data and operates in a world that ranges from  -10 to +10 (Y-axis and X axis) 
#  Each coordinate can hold a maximum of one event, has a unique event identifier and 0 or more tickets with a non-zero USD price.
#  The distance between two points is expressed as manhattan distance.

# 1. Assumptions : There is only one ticket price for each event, which is also the cheapest - I could have generated more ticket prices 
# to support multiple prices for a single event.
# 2. To support multiple events for a single location, my program would have to generate multiple event ids for a single location
# and I would have to look for closest events at the same coordinates and other surrounding coordinates and always choose the cheapest and
# closest.
# 3. If l was working in a larger world, l would search for the closest five neighbors recursively.
import random 
import numpy as np
# @params : User location - coordinate x, y 
# @post   : List of five closest events, along with the cheapest ticket price
def closestEvents(x,y) :
    # Generate our grid - a lists of lists of lists which store the coordinate id, ticket price, unique  ticket id, #numOfTickets
    # @coordinates : [ (x, y), ticket prices, unique event id, number of tickets ]
	coordinates = [[(i,j),random.sample(range(0,100),1), random.sample(range(1,10000),1) , random.sample(range(1,10000),1)]for i in range(-11,11) for j in range(-11,11) ]
	coordict = {} #Dictionary to store prices
	coordict1 = {} #Dictionary to store event ids
	for array in coordinates: 
		coordict[array[0]] = array[1] 
		coordict1[array[0]] = array[2]
	# @conditionals to find the nearest five coordinates
	
	# Find 5 nearest_neighbors for coordinates that are not on any edge
	if  x in range(-10,10) and y in range(-10,10) :
			ae = coordict1[(x + 1,y)]                    #  Step 1 : cheapest ticket price for @nearest_coordinate1
			ap = coordict[(x + 1 ,y)]                    #  Step 2 : unique event id 
			ad = manhattan_distance((x,y), (x +1,y))     #  Step 3 : manhattan distance of @nearest_coordinate1 from (x, y)
			be = coordict1[(x + 1,y + 1)]                #  Do step 1 to 3 for @nearest_coordinate2 up to @nearest_coordinate5
			bp = coordict[(x + 1,y + 1)]
			bd = manhattan_distance((x,y), (x + 1, y + 1))
			ce = coordict1[(x , y + 1)]
			cp = coordict[(x,y + 1)]
			cd = manhattan_distance((x,y), (x,y + 1))
			de = coordict1[(x - 1,y)]
			dp = coordict[(x - 1,y)]
			dd = manhattan_distance((x,y), (x - 1, y))
			ee = coordict1[(x,y - 1)]
			ep = coordict[(x,y - 1)]
			ed = manhattan_distance((x,y), (x, y - 1))
	# Find the five closest neighbors to edge case (-10, -10)
	if  x == -10 and y == -10 :
			ae = coordict1[(x + 1,y)]          #Do Steps 1 to 3 for for all five closest coordinates
			ap = coordict[(x + 1 ,y)]
			ad = manhattan_distance((x,y),(x+1,y))
			be = coordict1[(x ,y + 1)]
			bp = coordict[(x ,y + 1)]
			bd = manhattan_distance((x,y), (x, y + 1))
			ce = coordict1[(x + 1 , y + 1)]
			cp = coordict[(x + 1,y + 1)]
			cd = manhattan_distance((x,y),(x + 1, y + 1))
			de = coordict1[(x, y + 2)]
			dp = coordict[(x,y + 2 )]
			dd = manhattan_distance((x,y),(x, y + 2))
			ee = coordict1[(x + 2,y)]
			ep = coordict[(x + 2, y)]
			ed = manhattan_distance((x,y),(x + 2, y ))
    # Find the five closest neighbors to edge case (-10, 10)
	if  x == -10 and y == 10 :
			ae = coordict1[(x + 1,y)]		#Do Steps 1 to 3 for for all five closest coordinates
			ap = coordict[(x + 1 ,y)]
			ad = manhattan_distance((x,y),(x + 1, y))
			be = coordict1[(x + 2,y)]
			bp = coordict[(x + 2,y)]
			bd = manhattan_distance((x,y),(x + 2,y))
			ce = coordict1[(x + 1 , y - 1)]
			cp = coordict[(x + 1,y - 1)]
			cd = manhattan_distance((x,y), (x + 1, y - 1))
			de = coordict1[(x, y - 1)]
			dp = coordict[(x,y - 1 )]
			dd = manhattan_distance((x,y),(x, y - 1))
			ee = coordict1[(x ,y - 2)]
			ep = coordict[(x , y - 2)]
			ed = manhattan_distance((x,y), (x , y - 2))
	# Find the five closest neighbors to edge case (10, 10)		
	if x == 10 and y == 10 :
			ae = coordict1[(x - 1,y)]	  #Do Steps 1 to 3 for for all five closest coordinates   
			ap = coordict[(x - 1 ,y)]
			ad = manhattan_distance((x, y), (x - 1, y))
			be = coordict1[(x - 2,y)]
			bp = coordict[(x - 2,y)]
			bd = manhattan_distance((x, y), (x - 2, y))
			ce = coordict1[(x - 1 , y - 1)]
			cp = coordict[(x - 1,y - 1)]
			cd = manhattan_distance((x,y), (x -1, y - 1))
			de = coordict1[(x, y - 1)]
			dp = coordict[(x,y - 1 )]
			dd = manhattan_distance((x, y), (x, y - 1))
			ee = coordict1[(x ,y - 2)]
			ep = coordict[(x , y - 2)]
			ed = manhattan_distance((x,y), (x, y - 2))
	# Find the five closest neighbors to edge case (10, -10)		
	if x == 10 and y == -10 :
			ae = coordict1[(x,y + 1)]		#Do Steps 1 to 3 for for all five closest coordinates 
			ap = coordict[(x,y + 1)]
			ad = manhattan_distance((x,y), (x, y + 1))
			be = coordict1[(x -1 ,y)]
			bp = coordict[(x - 1,y)]
			bd = manhattan_distance((x,y), (x - 1, y))
			ce = coordict1[(x - 1 , y + 1)]
			cp = coordict[(x - 1,y + 1)]
			cd = manhattan_distance((x,y), (x - 1, y + 1))
			de = coordict1[(x, y + 2)]
			dp = coordict[(x,y + 2 )]
			dd = manhattan_distance((x, y), (x, y + 2))
			ee = coordict1[(x - 2,y )]
			ep = coordict[(x - 2, y )]
			ed = manhattan_distance((x,y),(x - 2, y))
	# Find the five closest neighbors for edge case (10, y <= 9) and y != -10		
	if x == 10 and y  <= 9  and y != -10: 
			ae = coordict1[(x,y + 1)]		#Do Steps 1 to 3 for for all five closest coordinates 
			ap = coordict[(x,y + 1)]
			ad = manhattan_distance((x,y), (x, y + 1))
			be = coordict1[(x ,y - 1)]
			bp = coordict[(x,y - 1)]
			bd = manhattan_distance((x,y), (x, y - 1))
			ce = coordict1[(x - 1 , y )]
			cp = coordict[(x - 1,y )]
			cd = manhattan_distance((x,y), (x - 1, y))
			de = coordict1[(x - 1, y + 1)]
			dp = coordict[(x -1 ,y + 1 )]
			dd = manhattan_distance((x,y), (x - 1, y + 1))
			ee = coordict1[(x - 2,y )]
			ep = coordict[(x - 2, y )]
			ed = manhattan_distance((x,y),(x - 2, y))
	# Find the five closest neighbors for edge case ( x <= 9, 10) and x != -10		
	if y == 10 and x <= 9 and x != -10:
			ae = coordict1[(x + 1,y )]
			ap = coordict[(x + 1,y)]
			ad = manhattan_distance((x,y), (x + 1, y))
			be = coordict1[(x - 1,y)]
			bp = coordict[(x - 1,y)]
			bd = manhattan_distance((x,y),(x - 1,y))
			ce = coordict1[(x, y - 1)]
			cp = coordict[(x,y - 1)]
			cd = manhattan_distance((x,y),(x,y - 1))
			de = coordict1[(x - 1, y - 1)]
			dp = coordict[(x -1 ,y - 1 )]
			dd = manhattan_distance((x,y),(x - 1, y - 1))
			ee = coordict1[(x + 1,y - 1 )]
			ep = coordict[(x + 1, y - 1)]
			ed = manhattan_distance((x,y), (x + 1, y - 1))
	# Find the five closest neighbors for edge case (-10, y <= 9) and y != -10		
	if x == -10 and  y <= 9  and y != -10:
			ae = coordict1[(x + 1,y )]
			ap = coordict[(x + 1,y)]
			ad = manhattan_distance((x,y),(x + 1,y))
			be = coordict1[(x, y + 1)]
			bp = coordict[(x,y + 1)]
			bd = manhattan_distance((x,y),(x,y + 1))
			ce = coordict1[(x + 1, y + 1)]
			cp = coordict[(x + 1,y + 1)]
			cd = manhattan_distance((x,y),(x + 1, y + 1))
			de = coordict1[(x + 1, y - 1)]
			dp = coordict[(x + 1 ,y - 1 )]
			dd = manhattan_distance((x,y),(x + 1, y - 1))
			ee = coordict1[(x + 2,y)]
			ep = coordict[(x + 2, y )]
			ed = manhattan_distance((x,y),(x + 2, y))
	# Find the five closest neighbors for edge case ( x <= 9, 10) and x != -10			
	if y == -10 and x <= 9 and x != -10:
			ae = coordict1[(x,y + 1)]
			ap = coordict[(x,y + 1)]
			ad = manhattan_distance((x,y),(x, y + 1))
			be = coordict1[(x + 1, y )]
			bp = coordict[(x + 1,y )]
			bd = manhattan_distance((x,y),(x + 1, y))
			ce = coordict1[(x + 1, y + 1)]
			cp = coordict[(x + 1,y + 1)]
			cd = manhattan_distance((x,y),(x + 1, y + 1))
			de = coordict1[(x, y + 2)]
			dp = coordict[(x ,y + 2)]
			dd = manhattan_distance((x,y), (x , y + 2))
			ee = coordict1[(x - 1,y + 1 )]
			ep = coordict[(x - 1, y + 1)]
			ed = manhattan_distance((x,y),(x - 1, y + 1))
			
    #Print the closest events to (x,y), indicate price event id, distance from (x,y)
	print( "\n" + "Closest events to  " + str((x,y)) + " : " + "\n")
	print("Event:" + str(int(ae.pop())))
	print ("Price: US$" + str(int(ap.pop())))
	print("Distance: " + str(ad) + "\n")
	print("Event:" + str(int(be.pop())))
	print ("Price: US$" + str(int(bp.pop())))
	print("Distance: " + str(bd) + "\n")
	print("Event:" + str(int(ce.pop())))
	print ("Price:US$" + str(int(cp.pop())))
	print("Distance: " + str(cd) + "\n")
	print("Event:" + str(int(de.pop())))
	print ("Price: US$" + str(int(dp.pop())))
	print("Distance: " + str(dd) + "\n")
	print("Event:" + str(int(ee.pop())))
	print ("Price: US$" + str(int(ep.pop())))
	print("Distance: " + str(ed) + "\n")

#manhattan distance function
def manhattan_distance(start, end):
	sx, sy = start
	ex, ey = end
	return abs(ex - sx) + abs(ey - sy)







