import psutil
import platform
 
def get_system_info():
    #get system uptime
    uptime = psutil.boot_time()
 
    try:
        temperature = psutil.sensors_temperatures()
        cpu_temp = temperature['coretemp'][0].current if 'coretemp' in temperature else 'N/A'
    except AttributeError:
        cpu_temp = 'N/A'
   
    system_info = {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "Uptime (seconds)": uptime,
        "CPU Temperature (°C)": cpu_temp
    }
 
    return system_info
 
if __name__ == "__main__":
    info = get_system_info()
    for key, value in info.items():
        print(f"{key}: {value}")