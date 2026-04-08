$ids = @(47679121,47676509,47679258,47680404,47677853,47650887,47678573,47681566,47657268,47680309,47681112,47673360,47654626,47681361,47677885,47675625,47658104,47675893,47675213,47681274,47664836,47673005,47621133,47627217,47682557,47675302,47677241,47679155)
$results = @()
foreach ($id in $ids) {
    try {
        $r = Invoke-RestMethod -Uri "https://hacker-news.firebaseio.com/v0/item/$id.json" -TimeoutSec 5
        if ($r -and $r.title) {
            $results += "$($r.title)"
        }
    } catch {}
}
$results | Select-Object -First 20 | ForEach-Object { Write-Output $_ }
