import platform
import psutil
import wmi
import os
import time
import socket


# ---------------- 系統資訊 ----------------
print("作業系統:", platform.system(), platform.release())
print("OS 平台:", platform.platform())
# print("Python 版本:", platform.python_version())
print("系統位元數:", platform.architecture()[0])
print("主機名稱:", platform.node())
print("用戶名稱:", os.getlogin())

# 系統開機時間
boot_time = psutil.boot_time()
print("開機時間:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(boot_time)))

print("-" * 40)

# ---------------- CPU 資訊 ----------------
print("CPU 架構:", platform.machine())
print("CPU 物理核心數:", psutil.cpu_count(logical=False))
print("CPU 核心數(含邏輯):", psutil.cpu_count(logical=True))
print("CPU 使用率:", psutil.cpu_percent(interval=1), "%")
freq = psutil.cpu_freq()
print("CPU 頻率: {:.2f} MHz".format(freq.current if freq else 0))
try:
    import cpuinfo
    print("CPU 名稱:", cpuinfo.get_cpu_info()['brand_raw'])
except:
    print("CPU 名稱: 無法取得，建議安裝 'py-cpuinfo'")

print("-" * 40)

# ---------------- RAM 資訊 ----------------
ram = psutil.virtual_memory()
print("總記憶體(RAM):", round(ram.total / (1024**3),2), "GB")
print("已使用:", round(ram.used / (1024**3), 2), "GB")
print("剩餘:", round(ram.available / (1024**3), 2), "GB")
print("記憶體使用率:", ram.percent, "%")

print("-" * 40)

# ---------------- GPU 資訊 (Windows) ----------------
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

print("-" * 40)

# ---------------- 磁碟資訊 ----------------
for part in psutil.disk_partitions():
    usage = psutil.disk_usage(part.mountpoint)
    print(f"磁碟 {part.device}")
    print(f"  總容量: {round(usage.total/1024**3,2)} GB")
    print(f"  已用: {round(usage.used/1024**3,2)} GB")
    print(f"  剩餘: {round(usage.free/1024**3,2)} GB")
    print(f"  使用率: {usage.percent}%")
    print("-" * 20)

print("-" * 40)


# # ---------------- 網路資訊 ----------------
# hostname = socket.gethostname()
# ip_address = socket.gethostbyname(hostname)
# print("本機 IP 位址:", ip_address)

# net = psutil.net_io_counters()
# print("已上傳:", round(net.bytes_sent/1024**2,2), "MB")
# print("已下載:", round(net.bytes_recv/1024**2,2), "MB")
