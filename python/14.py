print("---------DICTIONARIES----------")

monthConversions = {
    #key -- value
    "jan":"JANUARY",
    "FEB" : " february",
    "mar":"march",
    1:"april",
    2:"may"

}
print(monthConversions["mar"])
print(monthConversions.get("jan"))
print(monthConversions.get("luv","Not A valid key"))
print(monthConversions.get(1))