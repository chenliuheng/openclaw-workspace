$stories = Invoke-RestMethod -Uri 'https://hacker-news.firebaseio.com/v0/topstories.json' -TimeoutSec 15 | Select-Object -First 20
$result = @()
foreach($id in $stories) {
    $item = Invoke-RestMethod -Uri "https://hacker-news.firebaseio.com/v0/item/$id.json" -TimeoutSec 10
    $result += @{title=$item.title; score=$item.score; url=$item.url}
}
$result | ConvertTo-Json -Depth 3