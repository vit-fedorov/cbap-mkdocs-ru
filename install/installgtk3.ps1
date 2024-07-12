[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

# GTK3 is needed to output PDF files from MkDocs. It is not needed to build Web Help.
# GTK3 is fragile. It may not run depending on the PATH environment variable. 
# You might need to set the PATH and WEASYPRINT_DLL_DIRECTORIES environment variables
# to GTK3 bin and/or lib folder manually.
# The GTK3 path should be placed on the top of the PATH variable list.
# You might need to reboot your machine depending on your installation.

echo "`nCurrent script's directory: $PSScriptRoot"

& cd $PSScriptRoot\..

$curDir = Get-Location

echo "Changed directory to: $curDir"

echo 'Downloading and installing GTK3'

$url = "https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases/download/2021-04-29/gtk3-runtime-3.24.29-2021-04-29-ts-win64.exe"

# Destation file
$dest = "$PSScriptRoot\gtk3-runtime-3.24.29-2021-04-29-ts-win64.exe"

echo $url 
echo "to" 
echo $dest

Invoke-WebRequest -Uri $url -OutFile ($dest)

echo 'Installing GTK3'

& $dest
