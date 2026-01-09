monthConversions = {
  #keys   #value
  "Jan" : "January",
  "Feb" : "February",
  "Mar" : "March",
  "Apr" : "April",
  "May" : "May",
  "Jun" : "June",
  "Jul" : "July",
  "Aug" : "Aug",
  "Sep" : "September",
  "Oct" : "October",
  "Nov" : "November",
  "Dec" : "December",
 }

print(monthConversions["Nov"])# option 1 para ma display
print(monthConversions.get("Dec"))# option 2 para ma display
print(monthConversions.get("Luv", "Not a valid key"))#since walang "Luv", ang madidisplay is "Not a valid key"

print("--------------------")

monthConversions = {
  #keys   #value
    1 : "January",
    2 : "February",
    3 : "March",
    4 : "April",
    5 : "May",
    6 : "June",
    7 : "July",
    8 : "Aug",
    9 : "September",
    10 : "October",
    11 : "November",
    12 : "December",
 }

print(monthConversions.get(2))