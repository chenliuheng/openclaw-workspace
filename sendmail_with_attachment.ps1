$password = ConvertTo-SecureString "UNZ5t34VKT8w6c6u" -AsPlainText -Force
$credential = New-Object System.Management.Automation.PSCredential("chenliuheng@163.com", $password)

$subject = "Claude Code 源码"
$body = "Claude Code v2.1.88 源码已打包，请查收。"
$attachment = "C:\Users\陈流恒\claude-code-modified.zip"

Send-MailMessage -From "chenliuheng@163.com" -To "chenliuheng@163.com" -Subject $subject -Body $body -SmtpServer "smtp.163.com" -Port 25 -Credential $credential -Attachment $attachment

Write-Host "Email sent with attachment: $attachment"