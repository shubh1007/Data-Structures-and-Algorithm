# Implement a prototype service to automate the detection and replacement of faulty servers to improve the availability of an application.

# There are n servers with ids s1, s2, ..., sn, and an array of strings, logs, of size m. Log format is " < id>< success / e * rror >" the id of the server, and the status of the processed request. If a particular server id logs an error for three consecutive requests, it is considered faulty and is replaced with a new server with the same id.

# Given n and the array logs, find the number of times a faulty server was replaced.

# Example

# Suppose n = 2 and logs = ["s1 error", "s1 error", "s2 error", "s1 error", "s1 error", "s2 success"].


def countFaults(n, logs):
    faulty_servers = set()
    replaced_servers = 0
    consecutive_errors = {}
    
    for log in logs:
        server_id, status = log.split()
        server_id = server_id.strip()
        
        if server_id in faulty_servers:
            continue  # Server is already marked as faulty, no need to process further
        
        if status == "error":
            consecutive_errors[server_id] = consecutive_errors.get(server_id, 0) + 1
            if consecutive_errors[server_id] == 3:
                faulty_servers.add(server_id)
                replaced_servers += 1
                consecutive_errors[server_id] = 0
        else:
            consecutive_errors[server_id] = 0
    
    return replaced_servers



















def replaceFaultyServers(n, logs):
    faulty_servers = set()
    replaced_servers = 0
    consecutive_errors = {}
    
    for log in logs:
        server_id, status = log.split()
        server_id = server_id.strip()
        
        if server_id in faulty_servers:
            continue  # Server is already marked as faulty, no need to process further
        
        if status == "error":
            consecutive_errors[server_id] = consecutive_errors.get(server_id, 0) + 1
            if consecutive_errors[server_id] == 3:
                faulty_servers.add(server_id)
                replaced_servers += 1
                consecutive_errors[server_id] = 0
        else:
            consecutive_errors[server_id] = 0
    
    return replaced_servers

n = 5
logs = ["s1 error", "s2 error", "s1 error", "s4 success", "s5 error", "s3 success", "s1 error"]
result = replaceFaultyServers(n, logs)
print(result)

n = 6
logs = ["s2 error", "s3 error", "s2 error", "s2 error", "s2 error", "s3 error", "s3 error"]
result = replaceFaultyServers(n, logs)
print(result)
