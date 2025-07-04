# 🌍 Multi-Language Translator with Auto-Detection using Generative AI

This project is a real-time multilingual translator powered by **Meta's NLLB-200 model** and Hugging Face Transformers. It automatically detects the source language, maps it to the appropriate **FLORES-200 code**, and translates it into one of 200+ supported languages. Built with **Gradio**, the app offers a simple web interface and is deployed on Hugging Face Spaces for public use.

---

## 🚀 Features

- 🔤 Translate between 200+ languages using NLLB-200
- 🌐 Automatic source language detection via `langdetect`
- 🗂️ FLORES-200 language code compatibility
- ⚡ Fast and accurate translation pipeline
- 🖥️ Interactive Gradio-based UI
- ☁️ Hosted on Hugging Face Spaces

---

## 📂 Project Structure

```
├── app.py                 # Main application logic
├── requirements.txt       # Project dependencies
├── language.json          # Language name to FLORES-200 code mappings
└── README.md              # Project documentation
```

---

## 🛠️ Technologies Used

- Python 3.10+
- Hugging Face Transformers
- Meta’s NLLB-200 (distilled 600M variant)
- Gradio for web interface
- LangDetect for language identification
- Torch (PyTorch backend)

---

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/FinoMaxwell/Multi-Language-Translator-with-Auto-Detection-with-Gen-AI
cd multilingual-translator-genai
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Run the app locally:
```bash
python app.py
```

---

## 📌 Usage

1. Enter text in any supported language.
2. The system will automatically detect the input language.
3. Select the target language from the dropdown.
4. Click "Submit" to receive the translated output.

---

## 🌍 Supported Languages

Over 200 languages are supported through FLORES-200 codes, including but not limited to:
English, Spanish, Hindi, Tamil, Japanese, Swahili, Arabic, Bengali, French, Korean, Ukrainian, Yoruba, etc.

---

## 📈 Future Enhancements

- 🎤 Speech-to-Text (voice input)
- 🔊 Text-to-Speech (TTS) output
- 📁 File upload support for batch translations
- 🧠 Feedback system to rate translation quality
- 📷 OCR-based image translation (multimodal)

---

## 🧪 Testing

Testing includes:
- Unit and integration tests on core functions
- Performance testing on large inputs
- UI usability testing with real users
- Edge case handling for short/gibberish input

---

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Fino Maxwell G**  
VIT Chennai  
finomaxwell.g2022@vitstudent.ac.in

---

## 🔗 Live Demo

👉 Try it on [Hugging Face Spaces](https://huggingface.co/spaces/fino47/Multi-Language-Translator-with-Auto-Detection)
