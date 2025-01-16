# autor: Javier Montoya Perez
# fecha: 28-11-2024
def schedule_jobs_with_deadlines():
    import sys
    
    input = sys.stdin.read
    data = input().strip().splitlines()
    
    index = 0
    results = []
    
    while index < len(data):
        N = int(data[index])
        index += 1
        
        times = list(map(int, data[index].split()))
        index += 1
        
        deadlines = list(map(int, data[index].split()))
        index += 1
        
        jobs = [(times[i], deadlines[i], i + 1) for i in range(N)]
        
        # Sort jobs by deadline
        jobs.sort(key=lambda x: x[1])
        
        current_time = 0
        max_lateness = 0
        scheduled_jobs = []
        
        for job in jobs:
            time_required, deadline, job_index = job
            current_time += time_required
            finish_time = current_time
            lateness = max(0, finish_time - deadline)
            max_lateness = max(max_lateness, lateness)
            scheduled_jobs.append(job_index)
        
        results.append(f"{max_lateness}")
        results.append(" ".join(map(str, scheduled_jobs)))
    
    print("\n".join(results))

# Call the function to execute
schedule_jobs_with_deadlines()