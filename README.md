# Agentic AI Enumerator

An AI-driven reconnaissance and enumeration framework that intelligently selects the next enumeration step based on discovered target information.

**Agentic AI Enumerator** combines traditional penetration testing tools with an autonomous decision-making engine to simulate structured reconnaissance workflows used by professional security testers.

---

## Overview

This project automates reconnaissance by introducing an **agentic workflow**, where an AI model:

* Analyzes previous scan results
* Determines the next logical enumeration action
* Executes appropriate security tools
* Continues until meaningful enumeration is complete

Instead of manually running commands step-by-step, the AI acts as an intelligent operator guiding the enumeration process.

---

## Features

* Agentic AI decision engine
* Automated reconnaissance workflow
* Context-aware tool selection
* Avoids redundant scans
* Sequential enumeration logic
* Web content discovery automation
* Intelligence summary generation
* Modular tool execution

---

## Agentic Workflow Logic

The AI follows structured enumeration methodology:

1. Verify host reachability using `ping`
2. Discover open services using Nmap top ports scan (`_1000`)
3. Perform deeper scanning when required (`_all`)
4. Detect web services and launch directory fuzzing using `ffuf`
5. Continue enumeration based on findings
6. Generate a final intelligence summary

---

## Tools Used

* Nmap — Service detection and port scanning
* FFUF — Web content enumeration
* Ping — Connectivity verification
* Google Generative AI (Gemini API) — Autonomous decision engine

---

## Architecture Overview

```
User Input
   ↓
Agentic AI Decision Engine
   ↓
Tool Selection
   ↓
Execute Security Tool
   ↓
Collect Output
   ↓
Append to History
   ↓
Re-evaluate Next Action
   ↓
Final Intelligence Summary
```

---

## Project Structure

```
.
├── main.py        # Agentic enumeration engine
├── README.md
```

---

## Requirements

### System Dependencies

Ensure the following tools are installed:

```
nmap
ffuf
ping
```

Kali Linux installation:

```
sudo apt install nmap ffuf
```

---

### Python Dependencies

```
pip install google-genai
```

---

## Setup

1. Clone repository:

```
git clone https://github.com/yourusername/agentic-ai-enumerator.git
cd agentic-ai-enumerator
```

2. Configure Google GenAI API credentials according to your environment.

---

## Usage

Run the tool:

```
python main.py
```

Provide a target:

```
Enter your prompt:
Scan 10.10.10.10
```

The AI agent will:

* Analyze previous results
* Choose the next tool automatically
* Execute enumeration
* Produce an intelligence summary

---

## Example Intelligence Output

* Host availability status
* Open ports discovered
* Running services detected
* Web endpoints/directories identified
* Notable observations or risks

---

## Security Notice

This project is intended for:

* Educational purposes
* Ethical hacking practice
* Authorized penetration testing

Do NOT scan systems without explicit permission.

---

## Future Improvements

* Async execution support
* Structured parsing of tool output
* Persistent knowledge memory
* Risk scoring engine
* Automated vulnerability correlation
* Integration with additional recon tools
* Multi-target orchestration

---

## Author

Subbu Krishna Raju B N

Cybersecurity enthusiast focused on:

* Application Security
* Offensive Security
* AI-assisted Reconnaissance Automation


