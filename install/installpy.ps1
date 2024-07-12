[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

echo 'Downloading Python'

# Source URL
$SiteAdress = "https://www.python.org/downloads/"
$HttpContent = Invoke-WebRequest -URI $SiteAdress
$HttpContent.Links | Where-Object {$_.href -like "*amd64.exe"} | %{$url = $_.href} 

# Destation file
$dest = "$PSScriptRoot\python_latest.exe"

echo $url 
echo "to" 
echo $dest

Invoke-WebRequest -Uri $url -OutFile ($dest)

echo 'Installing Python'

& $dest /quiet PrependPath=1 Include_pip=1 Include_exe=1 Include_test=0 | Out-Default