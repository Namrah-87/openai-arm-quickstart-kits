# openai-arm-quickstart-kits
Minimal Python templates for using OpenAI models on ARM boards (Orange Pi, Radxa, Raspberry Pi).
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

### **Hardware‑Aware Profiles**
Each board family has a JSON profile describing:
- CPU architecture  
- Recommended Python version  
- Audio backend  
- Supported capabilities  
- Recommended OpenAI models  
- Known quirks and performance notes  

Profiles allow your code and CLI to adapt automatically to the hardware.

---

### **Micro‑Framework Core (`openai_arm/`)**
A lightweight internal SDK that provides:

- `client.py` — OpenAI client initialization  
- `profile_loader.py` — Load hardware profiles  
- `chat.py` — Simple and streaming chat helpers  
- `audio.py` — Speech‑to‑text and text‑to‑speech  
- `vision.py` — Image description helper  

This keeps your templates clean and your code modular.

---

### **Command‑Line Interface (`oaicli`)**
A simple, powerful CLI for interacting with OpenAI models on ARM boards:
oaicli chat "hello" 
oaicli stream "tell me a story" 
oaicli transcribe audio.wav oaicli speak "Hello world" out.mp3 
oaicli profile orange_pi_zero_series


The CLI is powered by `cli/main.py` and registered via `setup.cfg`.

---

### **Templates**
Minimal examples that demonstrate how to use the framework:

- `chat_minimal.py`
- `chat_streaming.py`
- `speech_to_text.py`
- `text_to_speech.py`

These are intentionally short, dependency‑light, and easy to modify.

---

### **Extensible Architecture**
This project is designed to grow into a full ecosystem:

- Add new board profiles  
- Add new CLI commands  
- Add showcase apps  
- Add real‑time audio pipelines  
- Add robotics integrations  

Everything is modular and clean.


The CLI is powered by `cli/main.py` and registered via `setup.cfg`.


---

## ✅ Installation

### **1. Clone the repository**
```bash
git clone https://github.com/<your-username>/openai-arm-quickstart-kits
cd openai-arm-quickstart-kits

### **2. Create a virtual environment**
python3 -m venv venv
source venv/bin/activate

### **3. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

### **4. Add you API key
Create a .env file:
OPENAI_API_KEY=your-key-here
