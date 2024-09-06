def calculate_fcfs_waiting_time(burst_times):
    n = len(burst_times)  
    waiting_times = [0] * n 
    
    for i in range(1, n):
        waiting_times[i] = waiting_times[i - 1] + burst_times[i - 1]
    average_waiting_time = sum(waiting_times) / n
    return average_waiting_time

burst_times = [7, 5, 3, 1, 2, 1]
average_waiting_time = calculate_fcfs_waiting_time(burst_times)
print(f"Average Waiting Time: {average_waiting_time}")
