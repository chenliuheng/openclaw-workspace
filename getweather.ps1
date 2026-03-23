$r = Invoke-RestMethod -Uri 'https://api.open-meteo.com/v1/forecast?latitude=23.02&longitude=113.12&current=temperature_2m,weather_code,wind_speed_10m&daily=weather_code,temperature_2m_max,temperature_2m_min&timezone=Asia/Shanghai&forecast_days=3'
Write-Output "Current: $($r.current.temperature_2m)C, code $($r.current.weather_code)"
Write-Output "Daily:"
for ($i = 0; $i -lt $r.daily.time.Count; $i++) {
    Write-Output "$($r.daily.time[$i]): H=$($r.daily.temperature_2m_max[$i]) L=$($r.daily.temperature_2m_min[$i]) code=$($r.daily.weather_code[$i])"
}
