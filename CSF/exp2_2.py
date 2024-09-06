def calculate_sjf_times(burst_times, priorities):
    n = len(burst_times)
    processes = list(zip(burst_times, priorities))

    processes.sort(key=lambda x: x[0])
    
    waiting_times = [0] * n
    turnaround_times = [0] * n
    for i in range(n):
        if i == 0:
            waiting_times[i] = 0
        else:
            waiting_times[i] = waiting_times[i - 1] + processes[i - 1][0]
        
        turnaround_times[i] = waiting_times[i] + processes[i][0]
    average_waiting_time = sum(waiting_times) / n
    average_turnaround_time = sum(turnaround_times) / n
    
    return average_waiting_time, average_turnaround_time

burst_times = [9, 4, 9]
priorities = [2, 1, 3]  
average_waiting_time, average_turnaround_time = calculate_sjf_times(burst_times, priorities)
print(f"Average Waiting Time: {average_waiting_time}")
print(f"Average Turnaround Time: {average_turnaround_time}")
