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

def search_logs(keyword):
    keyword = keyword.lower()
    results = []
    for log in logs:
        if keyword in log["message"].lower():
            results.append(log)
            print(f"[{log['level']}] {log['message']}")
    return results
    
def search_logs_by_level(keyword2):
    keyword2 = keyword2.lower()
    results2 = []
    for log in logs:
        if keyword2 == log["level"].lower():
            results2.append(log)
            print(f"[{log['level']}] {log['message']}]")
    return results2

search_logs_by_level("INFO")





        



    
        
        