$ids = @(47666024,47663147,47659135,47667672,47662234,47662945,47660954,47660286,47660925,47660853)
foreach($id in $ids) {
    $r = Invoke-RestMethod -Uri "https://hacker-news.firebaseio.com/v0/item/$id.json" -TimeoutSec 5
    Write-Output "$($r.title)|$($r.score)|$($r.url)"
}