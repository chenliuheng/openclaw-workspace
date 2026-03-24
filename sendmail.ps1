$password = ConvertTo-SecureString "UNZ5t34VKT8w6c6u" -AsPlainText -Force
$credential = New-Object System.Management.Automation.PSCredential("chenliuheng@163.com", $password)
$subject = Get-Date -Format "yyyy-MM-dd"
$body = "晚上好"
Send-MailMessage -From "chenliuheng@163.com" -To "chenliuheng@163.com" -Subject $subject -Body $body -SmtpServer "smtp.163.com" -Port 25 -Credential $credential
Write-Host "Email sent: $subject - $body"
