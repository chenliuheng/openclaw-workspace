$password = ConvertTo-SecureString "UNZ5t34VKT8w6c6u" -AsPlainText -Force
$credential = New-Object System.Management.Automation.PSCredential("chenliuheng@163.com", $password)
Send-MailMessage -From "chenliuheng@163.com" -To "chenliuheng@163.com" -Subject "测试" -Body "测试" -SmtpServer "smtp.163.com" -Port 25 -Credential $credential
