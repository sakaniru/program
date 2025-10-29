import requests

# 呼叫一個公開的天氣 API
url = "https://api.open-meteo.com/v1/forecast"
params = {
  "latitude": 25,
  "longitude": 121.625, # 台北市經緯度
  "hourly": "temperature_2m",
  "timezone": "Asia/Taipei",
  "start_date": "2025-10-20",
  "end_date": "2025-10-22"
}
response = requests.get(url, params=params)
data = response.json()
times = data["hourly"]["time"]
temps = data["hourly"]["temperature_2m"]

for t, temp in zip(times, temps):
    print(f"{t} → {temp}°C")
