import psutil

def cpu_usage(thresholds):
  try:
    cpu_percent = psutil.cpu_percent(interval=1)
    if cpu_percent >= thresholds:
      return {
         "value": cpu_percent,
         "status": "Unhealthy",
         "threshold": thresholds,
         "message": f"High CPU usage detected: {cpu_percent}%"
      }
    else:
      return {
        "value": cpu_percent,
        "status": "Healthy",
        "threshold": thresholds
      }
  except Exception as e:
    return f"Error checking CPU usage: {e}"

def memory_usage(threshold):
  try:
    memory_percent = psutil.virtual_memory().percent
    if memory_percent >= threshold:
      return {
         "value": memory_percent,
         "status": "Unhealthy",
         "threshold": threshold,
         "message": f"High memory usage detected: {memory_percent}%"
      }
    else:
      return {
        "value": memory_percent,
        "status": "Healthy",
        "threshold": threshold
      }
    
  except Exception as e:
    return  f"Error checking memory usage: {e}"

def disk_usage(threshold, path="/"):
  try:
    disk_usage = psutil.disk_usage(path).percent
    if disk_usage >= threshold:
      return {
         "value": disk_usage,
         "status": "Unhealthy",
         "threshold": threshold,
         "message": f"High disk usage detected: {disk_usage}%"
      }
    else:
       return {
        "value": disk_usage,
        "status": "Healthy",
        "threshold": threshold
      }
  except Exception as e:
     return f"Error checking disk usage: {e}"

def check_system_health(thresholds):
   health_status = {
     "cpu": cpu_usage(thresholds["cpu"]),
     "memory": memory_usage(thresholds["memory"]),
     "disk": disk_usage(thresholds["disk"])
   }
  # Check if system is overall healthy
   all_healthy = all([
     health_status['cpu']['status'],
     health_status['memory']['status'],
     health_status['disk']['status']
     ])
   health_status['overall_healthy'] = all_healthy
   return health_status

if __name__ == "__main__":
    print("=" * 50)
    print("SYSTEM HEALTH CHECK")
    print("=" * 50)
    
    # Define thresholds
    thresholds = {
        'cpu': 80,
        'memory': 80,
        'disk': 90
    }
    
    # Run health check
    results = check_system_health(thresholds)
    
    # Display results
    print(f"\nCPU Usage: {results['cpu']['value']:.1f}% ", end='')
    print("✅" if results['cpu']['status'] else "❌")
    
    print(f"Memory Usage: {results['memory']['value']:.1f}% ", end='')
    print("✅" if results['memory']['status'] else "❌")
    
    print(f"Disk Usage: {results['disk']['value']:.1f}% ", end='')
    print("✅" if results['disk']['status'] else "❌")
    
    print(f"\nOverall Status: ", end='')
    print("HEALTHY ✅" if results['overall_healthy'] else "UNHEALTHY ❌")
    print("=" * 50)