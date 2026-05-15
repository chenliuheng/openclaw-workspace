$ids = @(48142251,48138136,48140730,48142108,48139219,48142193,48137145,48138268,48140529,48140953,48141191,48140541,48097786,48141732,48137553,48140922,48108621,48139316,48134743,48136262)
$results = @()
foreach ($id in $ids) {
    try {
        $item = Invoke-RestMethod -Uri "https://hacker-news.firebaseio.com/v0/item/$id.json" -TimeoutSec 10 -ErrorAction SilentlyContinue
        if ($item -and $item.title) {
            $results += $item
        }
    } catch {}
}
$results | Select-Object title, url, score | ConvertTo-Json -Depth 1