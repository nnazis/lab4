from datetime import datetime
date1 = datetime.fromisoformat(input("Enter date: "))
date2 = datetime.fromisoformat(input("Enter date: "))
difference = abs((date2 - date1).total_seconds())
print(difference)