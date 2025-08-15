import platform
import psutil
import wmi
import os
import time


print("系統資訊:")
print("作業系統:", platform.system(), platform.release())
print("OS 平台:", platform.platform())
print("系統位元數:", platform.architecture()[0])
print("主機名稱:", platform.node())
print("用戶名稱:", os.getlogin())


boot_time = psutil.boot_time()
print("開機時間:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(boot_time)))
print("-" * 10)


print("CPU 相關資訊:")
c = wmi.WMI()
cpu_info = c.Win32_Processor()[0]
print("CPU 名稱:", cpu_info.Name)
print("CPU 架構:", platform.machine())
print("CPU 物理核心數:", psutil.cpu_count(logical=False))
print("CPU 核心數(含邏輯):", psutil.cpu_count(logical=True))
freq = psutil.cpu_freq()
print("CPU 頻率: {:.2f} MHz".format(freq.current if freq else 0))
cpu_usage = psutil.cpu_percent(interval=1) 
print("CPU 使用率: {:.2f}%".format(cpu_usage))
print("-" * 10)


print("記憶體相關資訊:")
ram = psutil.virtual_memory()
print("總記憶體(RAM):", round(ram.total / (1024**3),2), "GB")
print("已使用:", round(ram.used / (1024**3), 2), "GB")
print("剩餘:", round(ram.available / (1024**3), 2), "GB")
print("記憶體使用率:", ram.percent, "%")
print("-" * 10)


print("GPU 相關資訊:")
w = wmi.WMI()
gpus = w.Win32_VideoController()
if gpus:
    for i, gpu in enumerate(gpus):
        print(f"GPU {i} 名稱:", gpu.Name)
        print(f"GPU {i} 記憶體:", int(gpu.AdapterRAM / 1024**2), "MB")
        print(f"GPU {i} 驅動版本:", gpu.DriverVersion)
        print("-" * 20)
else:
    print("找不到 GPU 資訊")
print("-" * 10)


print("磁碟相關資訊:")
for part in psutil.disk_partitions():
    usage = psutil.disk_usage(part.mountpoint)
    print(f"磁碟 {part.device}")
    print(f"  總容量: {round(usage.total/1024**3,2)} GB")
    print(f"  已用: {round(usage.used/1024**3,2)} GB")
    print(f"  剩餘: {round(usage.free/1024**3,2)} GB")
    print(f"  使用率: {usage.percent}%")
print("-" * 10)
print(input("請按任意鍵結束"))