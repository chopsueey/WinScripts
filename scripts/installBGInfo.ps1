$BgInfoUrl = "https://download.sysinternals.com/files/BGInfo.zip"
$BgInfoZip = "$env:TEMP\BGInfo.zip"
$BgInfoPath = "C:\Tools\BGInfo"

Invoke-WebRequest -Uri $BgInfoUrl -OutFile $BgInfoZip
Expand-Archive -Path $BgInfoZip -DestinationPath $BgInfoPath -Force

# Optional: Configure BGInfo to auto-run with a basic config
$BgInfoExe = Join-Path $BgInfoPath "Bginfo.exe"
$BgInfoBgi = Join-Path $BgInfoPath "default.bgi"

# Create default config if it doesn't exist
if (-not (Test-Path $BgInfoBgi)) {
    Start-Process -FilePath $BgInfoExe -ArgumentList "/silent", "/timer:0" -Wait
}

# Set to run at logon (all users)
# $RunBgInfoCmd = "`"$BgInfoExe`" `"$BgInfoBgi`" /silent /timer:0"
# $RegPath = "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run"
# Set-ItemProperty -Path $RegPath -Name "BGInfo" -Value $RunBgInfoCmd