[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

echo 'Uninstalling Python'

& cd $PSScriptRoot\..

& .\python_latest.exe /uninstall /quiet | Out-Default

# Alternative method to start the uninstallation
# Start-Process .\python_latest.exe -NoNewWindow -Wait -ArgumentList /uninstall,/quiet
