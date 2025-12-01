# Prismail: The Cognitive Accessibility Platform

**Track:** Enterprise Agents
**Core Tech:** Gemini 2.5 Flash, Python

## 🚀 Overview
Prismail is a bicultural and neurodivergent-aware communication agent designed to preserve intent across the high-pressure US–MX engineering corridor.

Neurodivergent engineers often pay a **"Double Cognitive Tax"**:
1.  **The Neurodivergent Tax:** Struggles with executive function and task initiation.
2.  **The Bicultural Tax:** Navigating between high-context Mexican Spanish and low-context US English.

Prismail acts as **Cognitive Infrastructure**, offering "Intent-Preserving Cultural Modulation" to turn emotionally loaded, bicultural cognition into stable, auditable communication.

## 🧠 Architecture & "Trace Mode"
Prismail implements a **Multi-Agent System** with a closed, auditable loop:

1.  **Router Agent:** Classifies intent and selects the appropriate tone profile (US Formal, US Informal, MX Formal, MX Informal).
2.  **Tone Generator (Gemini 2.5 Flash):** Translates raw input into a culturally modulated draft.
3.  **Linguistic QA Agent:** Evaluates the draft against the original input for **Fidelity** (Intent Preservation) and **Professionalism**.

### Auditable Metrics
The system provides transparency via specific metrics:
* **IPS (Intent Preservation Score):** Ensures facts and urgency are not lost in translation.
* **CFMS (Cultural Fit Match Score):** Ensures the tone matches the target cultural context.

## 📂 Project Structure
The project generates the following virtual modules during runtime:

* `Prismail.ipynb`: The main entry point containing the "Golden Demo."
* `system_prompts.py`: Contains the 4 distinct tone personas and the JSON-based QA prompt.
* `prismail_models.py`: Handles the initialization of the Gemini 2.5 Flash models and the routing logic.

## 🛠️ Setup & Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/prismail.git](https://github.com/your-username/prismail.git)
    cd prismail
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Environment Configuration:**
    Create a `.env` file in the root directory and add your Google API key:
    ```text
    GOOGLE_API_KEY=your_actual_api_key_here
    ```

4.  **Run the Golden Demo:**
    Open `Prismail.ipynb` in JupyterLab or VS Code and run all cells. The notebook will automatically write the necessary python files (`system_prompts.py`, `prismail_models.py`) and execute the **Golden Demo Trace**.

## 📊 Demo Scenarios
The notebook includes a live test bench covering two distinct scenarios:

* **Scenario 1 (Spanish Input):** Transforming aggressive/colloquial feedback ("*¿por qué chingados...?*") into constructive corporate inquiries.
* **Scenario 2 (English Input):** Transforming blunt status updates ("*shitty work*") into professional risk assessments.

## 🛡️ Trustworthiness & Safety
Prismail implements strict boundaries:
* **No Factual Alterations:** Never alters facts if IPS < 0.85.
* **Emotion-Preserving:** Regulates tone without erasing the user's right to the underlying sentiment.

---
*Submitted by Diana Zoila Vázquez Pérez*