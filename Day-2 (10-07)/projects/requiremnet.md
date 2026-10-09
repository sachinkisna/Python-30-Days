What it does: Calculates the price of movie tickets using seat type, age, day of the week, and a coupon code. It uses every concept from today.

Pricing rules

Base price per ticket

Regular: 200
Premium: 350
Anything else: show an error and stop

Age discount (applies to all tickets in the booking)

Under 5: free
5 to 11: 50% off
60 and above: 30% off
Everyone else: full price

Day pricing

Tuesday: 20% off (“Cheap Tuesday”)
Saturday or Sunday: 15% surcharge
Other days: normal

Coupon

SAVE10: 10% off the subtotal, but only when booking 2 or more tickets
Any other non-empty code: print “Invalid coupon”
Empty: no coupon
Expected output
===== CineMax Ticket Booking =====
Your name: Aman
Your age: 25
Day of the week: saturday
Seat type (regular/premium): premium
Number of tickets: 2
Coupon code (Enter to skip): save10

--------- BOOKING SUMMARY ---------
Name          : Aman
Seat          : Premium
Day           : Saturday
Tickets       : 2
Price/ticket  : 402.50
Subtotal      : 805.00
Coupon SAVE10 : -80.50
TOTAL         : 724.50
-----------------------------------
Enjoy the movie, Aman!