"""
PHASE 2 DELIVERABLE (v2 con 4 tonos)
Define y inicializa los modelos de IA.
"""
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Import the brain
import system_prompts

# Set safety settings to be permissive for this demo
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
]

# Esta función actúa como nuestro "Router"
def get_prompt_for_tone(tone_id: str) -> dict:
    """
    Actúa como un enrutador simple. 
    Devuelve el prompt correcto basado en el 'tone_id' solicitado.
    """
    if tone_id == "us_formal":
        return {"prompt": system_prompts.PROMPT_US_FORMAL}
    elif tone_id == "us_informal":
        return {"prompt": system_prompts.PROMPT_US_INFORMAL}
    elif tone_id == "mx_formal":
        return {"prompt": system_prompts.PROMPT_MX_FORMAL}
    elif tone_id == "mx_informal":
        return {"prompt": system_prompts.PROMPT_MX_INFORMAL}
    else:
        return {"error": "Tone ID no encontrado"}

# Creamos una función para inicializar los modelos CON la clave
def initialize_models(api_key):
    
    genai.configure(api_key=api_key)
    
    # Model 1: Tone Translator
    model_translator = genai.GenerativeModel(
        model_name="models/gemini-flash-latest"
    )

    # Model 2: QA Agent
    model_qa = genai.GenerativeModel(
        model_name="models/gemini-flash-latest",
        system_instruction=system_prompts.PROMPT_QA,
        generation_config={"response_mime_type": "application/json"}
    )
    
    print("✅ Models initialized successfully.")
    return model_translator, model_qa

print("✅ prismail_models.py written.")
