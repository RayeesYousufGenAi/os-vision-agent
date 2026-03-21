<p align="center">
  <img src="media/logo.png" width="200" alt="OS-Vision-Agent Logo">
</p>

# 👁️ OS-Vision-Agent

> **The World's First High-Performance, Vision-Agnostic OS Operator.** No APIs, No Selectors—Just Pure Vision.

[![GitHub Stars](https://img.shields.io/github/stars/RayeesYousufGenAi/os-vision-agent?style=for-the-badge&color=8b5cf6)](https://github.com/RayeesYousufGenAi/os-vision-agent)
[![Vision Engine](https://img.shields.io/badge/Engine-GPT--4o--Vision-vibrantgreen?style=for-the-badge&logo=openai)](https://openai.com/)
[![Automation](https://img.shields.io/badge/Automation-PyAutoGUI-blue?style=for-the-badge)](https://pyautogui.readthedocs.io/)

---

## 🧠 The Concept

**OS-Vision-Agent** bridges the gap between AI and the Desktop. Unlike traditional automation tools that require "selectors" or "DOM access," this agent interacts with your system exactly like a human: it **sees** the screen, **reasons** about the UI, and **acts** via the mouse and keyboard.

> [!TIP]
> This "Vision-First" approach makes it compatible with everything: legacy enterprise software, native Mac/Windows apps, and custom 3D environments.

---

## 🔥 Key Technical Features

- **🌐 Vision-to-Action Loop**: 
  1. `capture_screen()`: High-res screen capture and local pre-processing.
  2. `get_gpt_action()`: Multimodal reasoning via GPT-4o-Vision to determine intent.
  3. `execute_action()`: Low-level OS control via calibrated PyAutoGUI wrappers.
- **📐 Coordinate Mapping**: Normalized 0-1000 coordinate system ensures consistent performance across high-DPI (Retina) and standard displays.
- **🛡️ Built-in Failsafe**: Immediate abort mechanism (Corner Fail-Safe) prevents runaway operations.

---

## 🚀 Setting Up the Ghost Operator

### 1. Requirements
- **Python**: 3.9+
- **OpenAI API Key**: (GPT-4o access required)

### 2. Installation
```bash
git clone https://github.com/RayeesYousufGenAi/os-vision-agent.git
cd os-vision-agent
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configuration
Create a `.env` file in the root:
```env
OPENAI_API_KEY=sk-your-key-goes-here
```

### 4. Deployment
```bash
python3 app.py
```
**Recommended Goal**: *"Open Chrome, search for the best pizza in New York, and find the first review."*

---

## 🛠️ System Architecture

```mermaid
graph TD
    A[Desktop State] -->|Screenshot| B(PIL Processor)
    B -->|Base64| C{GPT-4o Vision}
    C -->|Reasoning + JSON| D[Action Controller]
    D -->|Move/Click/Type| E(OS Event)
    E -->|Next State| A
```

---

## ⚠️ Privacy & Safety
- **Visibility**: The agent requires the target application to be visible on the primary monitor.
- **Data**: Screenshots are sent to OpenAI's API. Do not use with sensitive information visible.
- **Failsafe**: Slam your mouse into any corner of the screen to kill the process instantly.

---

## 📄 License
MIT License. Explore and expand.

---

<p align="center">Empowering the Autonomy of the Desktop 👁️🦾</p>
