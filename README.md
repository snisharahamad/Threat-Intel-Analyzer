# Threat Intel IP Scanner

A lightweight Python CLI utility to quickly check the reputation of a suspicious IP address.

I originally built this script to automate the analysis of IPs hitting my local honeypot (which I couldn't expose cleanly due to my router's CGNAT). The tool queries the AbuseIPDB API and parses the JSON response to extract only tactical data directly into the terminal.

## Stack
- **Python 3** (`requests` library)
- **uv** for lightning-fast virtual environment and dependency management
- **python-dotenv** for secure API key management

## Setup

**1. Clone the repository**
```bash
git clone [https://github.com/snisharahamad/Threat-Intel-Analyzer.git](https://github.com/snisharahamad/Threat-Intel-Analyzer.git)
cd Threat-Intel-Analyzer
uv sync
```

**2. Configuration**
Create a `.env` file at the root of the project to store your AbuseIPDB API key. This file is ignored by Git via the `.gitignore` to prevent secret leaks.
```text
API_KEY="your_api_key_here"
```

## Usage

Simply pass the suspicious IP as an argument:
```bash
uv run scanner.py 118.25.6.39
```
