# OpenAI ARM Quickstart Kits
A hardware‑aware AI toolkit for ARM single‑board computers.

This project provides a clean, minimal, and extensible framework for running OpenAI models on low‑cost ARM boards such as the Orange Pi Zero 3 Series, Radxa Zero 3 Series, Raspberry Pi 4/5, and more.

It includes:

- A micro‑framework (`openai_arm/`)
- A command‑line interface (`oaicli`)
- Hardware profiles for multiple ARM board families
- Ready‑to‑run templates for chat, streaming, speech, and vision
- A structure designed for real projects, not just demos

The goal is simple:  
**Make AI development on ARM boards fast, predictable, and enjoyable.**

---

## ✅ Features

### Hardware‑Aware Profiles
Each board family has a JSON profile describing:

- CPU architecture  
- Recommended Python version  
- Audio backend  
- Supported capabilities  
- Recommended OpenAI models  
- Known quirks and performance notes  

Profiles allow your code and CLI to adapt automatically to the hardware.

---

### Micro‑Framework Core (`openai_arm/`)
A lightweight internal SDK that provides:

- `client.py` — OpenAI client initialization  
- `profile_loader.py` — Load hardware profiles  
- `chat.py` — Simple and streaming chat helpers  
- `audio.py` — Speech‑to‑text and text‑to‑speech  
- `vision.py` — Image description helper  

This keeps your templates clean and your code modular.

---

### Command‑Line Interface (`oaicli`)
A simple, powerful CLI for interacting with OpenAI models on ARM boards:

Basic usage:

- `oaicli chat "hello"`
- `oaicli stream "tell me a story"`
- `oaicli transcribe audio.wav`
- `oaicli speak "Hello world" out.mp3`
- `oaicli profile orange_pi_zero_series`
- `oaicli profile auto`

Advanced commands:

- `oaicli setup` — interactive setup wizard  
- `oaicli doctor` — diagnostics and environment checks  
- `oaicli benchmark` — basic performance tests  
- `oaicli update` — update repo and dependencies  
- `oaicli record output.wav [duration]` — record microphone audio  
- `oaicli play output.wav` — play audio  

---

### Templates
Minimal examples that demonstrate how to use the framework:

- `chat_minimal.py`
- `chat_streaming.py`
- `speech_to_text.py`
- `text_to_speech.py`

These are intentionally short, dependency‑light, and easy to modify.

---

## ✅ Repository Structure

```
openai-arm-quickstart-kits/
│
├── cli/
│   ├── __init__.py
│   ├── main.py
│   ├── setup.py
│   ├── doctor.py
│   ├── benchmark.py
│   ├── update.py
│   ├── record.py
│   └── play.py
│
├── openai_arm/
│   ├── __init__.py
│   ├── client.py
│   ├── profile_loader.py
│   ├── chat.py
│   ├── audio.py
│   └── vision.py
│
├── profiles/
│   ├── orange_pi_zero_series.json
│   ├── radxa_zero3_series.json
│   ├── raspberry_pi_5_series.json
│   └── generic_arm.json
│
├── templates/
│   ├── chat_minimal.py
│   ├── chat_streaming.py
│   ├── speech_to_text.py
│   └── text_to_speech.py
│
├── install.sh
├── install.py
├── oaicli
├── setup.cfg
├── requirements.txt
├── .gitignore
└── LICENSE
```

---

## ✅ One‑Line Installer

Run this on your ARM board:

```
curl -sSL https://raw.githubusercontent.com/Namrah-87/openai-arm-quickstart-kits/main/install.sh | bash
```

The installer will:

- auto‑detect your ARM board  
- install system packages  
- install Python dependencies  
- load the correct hardware profile  
- give next‑step instructions  

---

## ✅ Manual Installation

### Clone the repository
```bash
git clone https://github.com/Namrah-87/openai-arm-quickstart-kits
cd openai-arm-quickstart-kits
```

### Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Add your API key
Create a `.env` file:

```
OPENAI_API_KEY=your-key-here
```

---

## ✅ Uses of the OpenAI API Key

This toolkit uses the OpenAI API to provide all AI functionality on ARM boards.  
Your API key is required so the toolkit can authenticate with OpenAI’s servers and perform the following actions:

- Sending chat requests (text generation)
- Streaming responses for real‑time interaction
- Speech‑to‑text (audio transcription)
- Text‑to‑speech (audio generation)
- Image description (vision model)

The key is loaded locally from your `.env` file and only used when you run commands or examples.  
Do **not** commit your API key to GitHub or share it publicly.

---

## ✅ Using the CLI

### Chat
```bash
oaicli chat "Explain ARM boards"
```

### Streaming Chat
```bash
oaicli stream "Tell me a joke"
```

### Speech‑to‑Text
```bash
oaicli transcribe audio.wav
```

### Text‑to‑Speech
```bash
oaicli speak "Hello from my ARM board" out.mp3
```

### Show a hardware profile
```bash
oaicli profile orange_pi_zero_series
oaicli profile auto
```

### Setup wizard
```bash
oaicli setup
```

### Diagnostics
```bash
oaicli doctor
```

### Benchmark
```bash
oaicli benchmark
```

### Update
```bash
oaicli update
```

### Record audio
```bash
oaicli record output.wav 5
```

### Play audio
```bash
oaicli play output.wav
```

---

## ✅ Using the Framework in Python

### Simple Chat
```python
from openai_arm.chat import simple_chat
print(simple_chat("What is an SBC?"))
```

### Transcribe Audio
```python
from openai_arm.audio import transcribe
print(transcribe("audio.wav"))
```

### Load a Profile
```python
from openai_arm.profile_loader import load_profile
profile = load_profile("radxa_zero3_series")
print(profile["cpu"])
```

---

## ✅ Supported Boards

- Orange Pi Zero 3 Series  
- Orange Pi 3 Series  
- Radxa Zero 3 Series  
- Raspberry Pi 4 Series  
- Raspberry Pi 5 Series  
- Khadas VIM Series  
- Generic ARMv8 boards  

More profiles can be added easily.

---

## ✅ Why This Project Exists

AI hardware is becoming the new literacy.  
But most people can’t afford expensive devices.

This project brings world‑class AI to **$15–$50 ARM boards**, making it accessible for:

- students  
- educators  
- makers  
- robotics teams  
- hobbyists  
- open‑source developers  

Everything is designed to be:

- minimal  
- modular  
- clean  
- hardware‑aware  
- beginner‑friendly  
- powerful enough for real projects  

---

## ✅ License

This project is released under the MIT License.

---

## ✅ Contributing

Pull requests are welcome.  
You can contribute:

- new board profiles  
- new CLI commands  
- new templates  
- showcase apps  
- documentation improvements  

---
