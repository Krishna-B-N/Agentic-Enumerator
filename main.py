import subprocess
from google import genai
import json


def _1000(ip_address):
    result = subprocess.run(["nmap","-sV","-sC","-Pn",ip_address],text=True,capture_output=True)
    output = f"\nTool stdout: {result.stdout}"
    if(result.stderr):
        output = output + f"\n\nTool stderror: {result.stderr}"

    if(result.returncode != 0):
        output = output + f"\n\n Tool exit code {result.returncode}"
    
    return output
        

def _all(ip_address):
    result = subprocess.run(["nmap","-p-","-sV","-sC",ip_address],text=True,capture_output=True)
    output = f"\nTool stdout: {result.stdout}"
    if(result.stderr):
        output = output + f"\n\nTool stderror: {result.stderr}"

    if(result.returncode != 0):
        output = output + f"\n\n Tool exit code {result.returncode}"
    
    return output

def ping(ip_address):
    result = subprocess.run(["ping","-c","5",ip_address],text=True,capture_output=True)
    output = f"\nTool stdout: {result.stdout}"
    if(result.stderr):
        output = output + f"\n\nTool stderror: {result.stderr}"

    if(result.returncode != 0):
        output = output + f"\n\n Tool exit code {result.returncode}"
    
    return output

def ffuf(wordlist_path,target_url,depth):
    wordlistPath = wordlist_path+":FUZZ"
    targetUrl = target_url+"FUZZ"
    result = subprocess.run(["ffuf","-w",wordlistPath,"-u",targetUrl,"-ic","-recursion","-recursion-depth",depth,"-v"],text=True,capture_output=True)
    output = f"\nTool stdout: {result.stdout}"
    if(result.stderr):
        output = output + f"\n\nTool stderror: {result.stderr}"

    if(result.returncode != 0):
        output = output + f"\n\n Tool exit code {result.returncode}"
    
    return output

def ai(user_request,history):
    profile = """You are an expert enumeration AI focused on reconnaissance and target analysis. Your task is to intelligently select the NEXT most appropriate tool based on the current findings and previously executed steps.

Workflow Rules:

- Analyse Conversation History to understand which tools have already been executed.
- DO NOT repeat tools unless new information clearly requires it.
- Only run ping if connectivity has NOT yet been verified.
- Select the next logical enumeration step based on discovered services.
- Continue enumeration until no further meaningful actions remain.

Decision Strategy:

- If target reachability is unknown → use ping.
- If open ports are unknown → use Nmap _1000.
- If deeper port discovery is required → use Nmap _all.
- If web service is detected → use ffuf for web content enumeration.
- Avoid redundant scans.

State Control:

- Include "notDone": true when further actions remain.
- Include "notDone": false when enumeration is complete.

Available Tools and Required JSON Output Formats:

1. ping
{
  "tool_name": "ping",
  "tool_params": {
    "ip_address": "TARGET_IP"
  },
  "notDone": true
}

2. Nmap _1000 (top ports scan)
{
  "tool_name": "_1000",
  "tool_params": {
    "ip_address": "TARGET_IP"
  },
  "notDone": true
}

3. Nmap _all (full port scan)
{
  "tool_name": "_all",
  "tool_params": {
    "ip_address": "TARGET_IP"
  },
  "notDone": true
}

4. ffuf (web enumeration)
{
  "tool_name": "ffuf",
  "tool_params": {
    "wordlist_path": "/usr/share/seclists/Discovery/Web-Content/common.txt",
    "target_url": "TARGET_URL",
    "depth": "2"
  },
  "notDone": true
}

Output Rules:

- Return ONLY valid JSON.
- No explanations.
- No markdown formatting.
- JSON must strictly match one of the tool formats above.
"""
    full_request = f'AI Profile: {profile}'+"\n\n"+f'Conversation History: {history}'+"\n\n"+f'User Request: {user_request}'
    client = genai.Client()
    response = client.models.generate_content(model="gemini-3-flash-preview", contents=full_request)
    print(response.text)
    return response.text


user_request = input("Enter your prompt:\n")
history = ""
notDone = True
while(notDone):
    result = ai(user_request,history)
    data = json.loads(result)
    tool_name = data.get("tool_name")
    params = data.get("tool_params", {})


    if tool_name == "ping":
        ip = params.get("ip_address")
        history = history + "\n\n" + ping(ip)

    elif tool_name == "_1000":
        ip = params.get("ip_address")
        history = history + "\n\n" + _1000(ip)
        
    elif tool_name == "_all":
        ip = params.get("ip_address")
        history = history + "\n\n" + _all(ip)
        
    elif tool_name == "ffuf":
        wordlists = params.get("wordlist_path")
        uri = params.get("target_url")
        depth = params.get("depth")
        history = history + "\n\n" + ffuf(wordlists,uri,depth)
    
    notDone = data.get("notDone")

def summarize(history):
    summary_profile = """
You are a cybersecurity intelligence analyst.

Your task is to analyze the provided Conversation History and produce a concise intelligence summary.

Rules:

- Provide clear bullet points.
- Highlight key findings such as:
  - host availability
  - open ports
  - detected services
  - web directories or endpoints
  - notable risks or observations

Output Requirements:

- Output NORMAL TEXT.
- NO JSON.
- NO tool selection.
- NO enumeration actions.
"""
    full_request = f'AI Profile: {summary_profile}\n\nConversation History: {history}'
    client = genai.Client()
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=full_request
    )
    return response.text

print("We are out of the loop:\n")
user_request = "Give me an intelligence summary of Conversation History above."
print("\n\n")
print(summarize(history))

