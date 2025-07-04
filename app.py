import json
import torch
import gradio as gr

# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("translation", model="facebook/nllb-200-distilled-600M")
text_translator = pipeline(
    "translation",
    model="facebook/nllb-200-distilled-600M"
)
from langdetect import detect

# Load NLLB-200 translation pipeline
text_translator = pipeline("translation", model="facebook/nllb-200-distilled-600M")

# Load language mapping
with open('language.json', 'r') as file:
    language_data = json.load(file)

# Get FLORES-200 code from language name
def get_FLORES_code_from_language(language):
    for entry in language_data:
        if entry['Language'].lower() == language.lower():
            return entry['FLORES-200 code']
    return None

# Get FLORES-200 code from ISO detected language (e.g., 'en' → 'eng_Latn')
def get_FLORES_code_from_iso(iso_code):
    iso_code = iso_code.lower()
    for entry in language_data:
        flores_code = entry['FLORES-200 code']
        if flores_code.lower().startswith(iso_code):
            return flores_code
    return None

# Main translation function
def translate_text(text, destination_language):
    try:
        # Use English as fallback for short/ambiguous input
        if len(text.strip().split()) <= 1:
            detected_lang_code = "en"
        else:
            detected_lang_code = detect(text)

        src_code = get_FLORES_code_from_iso(detected_lang_code)
        tgt_code = get_FLORES_code_from_language(destination_language)

        if not src_code or not tgt_code:
            return "Error: Could not detect or match language codes."

        # Translate using NLLB
        translation = text_translator(text, src_lang=src_code, tgt_lang=tgt_code)

        return f"Detected Language: {detected_lang_code}\n\nTranslated Text:\n{translation[0]['translation_text']}"
    
    except Exception as e:
        return f"Translation failed: {str(e)}"

# Language options for the dropdown
language_names = [entry['Language'] for entry in language_data]

# Gradio UI
demo = gr.Interface(
    fn=translate_text,
    inputs=[
        gr.Textbox(label="Input text (auto-detects source language)", lines=6),
        gr.Dropdown(language_names, label="Select Destination Language")
    ],
    outputs=[gr.Textbox(label="Output", lines=6)],
    title="🌍 Multi-Language Translator with Auto-Detection",
    description="Translate text from any language into your selected language using Meta's NLLB model and automatic source language detection."
)

demo.launch(share=True)
