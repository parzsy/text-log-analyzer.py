logs = []
with open("logs.txt", "r") as file:
    for line in file:
        parts = (line.split("]"))
        level_with_bracket = parts[0]
        level = level_with_bracket[1:] #ex. INFO
        message = parts[1].strip() #ex. User Sophie logged in
        dc1 = {"level": level,
               "message": message
        }
        logs.append(dc1)

counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}

for log in logs: 
    level = log["level"] 
    counts[level] +=1

error_logs = []
user_in_msg = []
disk_in_msg = []
warning_and_coffee= []

#checks for ERROR as level and adds to list
for log in logs:
    if log["level"] == "ERROR":
        error_logs.append(log)

#checks for User in the msg and adds to list
for log in logs:
    if "User" in log["message"]:
        user_in_msg.append(log)

#checks for disk in msg and adds to list
for log in logs:
    if "disk" in log["message"]:
        disk_in_msg.append(log)

#checks for WARNING as level and coffee in msg and adds to list
for log in logs:
    if log["level"] == "WARNING" and "coffee" in log["message"]:
        warning_and_coffee.append(log)
print(warning_and_coffee)
        



    
        
        