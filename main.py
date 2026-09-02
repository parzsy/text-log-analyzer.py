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

def menu():
    print("1. Search logs with keyword")
    print("2. Search logs by level")
    print("3. Print counts")
    print("4. Quit")
    choice = int(input("Enter choice: "))
    return choice

for log in logs: 
    level = log["level"] 
    counts[level] +=1

def count():
    print(counts)

def search_logs():
    keyword = input("Enter keyword: ")
    keyword = keyword.lower()
    results = []
    for log in logs:
        if keyword in log["message"].lower():
            results.append(log)
            print(f"[{log['level']}] {log['message']}")
    return results
    
def search_logs_by_level():
    keyword2 = input("Enter level: ")
    keyword2 = keyword2.lower()
    results2 = []
    for log in logs:
        if keyword2 == log["level"].lower():
            results2.append(log)
            print(f"[{log['level']}] {log['message']}")
    return results2

while True:
    choice = menu()
    if choice == 1:
        search_logs()
    elif choice == 2:
        search_logs_by_level()
    elif choice == 3: 
        count()
    elif choice == 4:
        break








        



    
        
        