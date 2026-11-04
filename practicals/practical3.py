import datetime

now = datetime.datetime.now()

print("Full Weekday Name:", now.strftime("%A"))
print("Full Month Name:", now.strftime("%B"))
print("Century:", now.strftime("%C"))
print("Short Date Format (MM/DD/YY):", now.strftime("%D"))
print("Hour (24-hour clock):", now.strftime("%H"))
print("Hour (12-hour clock):", now.strftime("%I"))
print("Seconds:", now.strftime("%S"))
print("Full Year:", now.strftime("%Y"))
