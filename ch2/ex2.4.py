import math
from datetime import datetime
from datetime import timedelta

# part 1
radius=5
volume=(4.0/3)*math.pi*(radius)**3
print volume

# part 2
price=24.95
bookstore_price=0.6*price
number_of_books=60
shipping=3.0+(number_of_books-1)*(0.75)
total=(number_of_books*bookstore_price) + shipping
print total

# part 3
easy=8.0+(15.0/60)
#easy=((8.0+(15.0/60))*100)/60
tempo=7.0+(12.0/60)
#tempo=((7.0+(12.0/60))*100)/60
delta=2.0*easy+3.0*tempo
start_time=datetime(2015,1,1,6,52,0,0)
diff=timedelta(minutes = delta)
#time=(6+((52*100)/60))+((delta*100)/60)
time=start_time+diff
print time
print delta
