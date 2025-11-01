# 🌐 SkillLink

SkillLink is an **AI-powered web platform** designed to connect **women and small-skilled workers** from villages and towns to **local employment opportunities**.  
Users can describe their skills in **simple natural language**, and SkillLink’s AI automatically understands and categorizes their skills — making it easier for them to find nearby jobs that match their abilities.

---

## 🚀 Features

- 🧠 **AI Skill Interpretation:** Uses Google’s **FLAN-T5 model** to understand skill descriptions in plain text.
- 💬 **Interactive Interface:** Built using **Streamlit**, providing an easy-to-use, chat-like interface.
- 🌍 **Community Empowerment:** Focuses on connecting underrepresented skill workers with employment.
- 🔄 **Continuous Input:** Users can keep entering skills until they choose to quit.
- 💡 **Expandable Design:** Future scope for adding **voice input** and **regional language support**.

---

## 🧠 How It Works

1. The user visits the SkillLink web app. https://skilllink-app-resu8gbmxnetydm7tmtqr5.streamlit.app/

2. They type a description of what they can do — for example:
   > "I can sew clothes and do embroidery."

3. The **FLAN-T5 model** processes the input and outputs a standardized skill category, e.g.:
   > "Tailoring / Handicraft"

4. The interpreted skill can then be used to **match job opportunities** or **recommend nearby work**.

---

hugging face repo- (Divya21026/flan-skilltitle-model)

## 🧩 Tech Stack

| Category | Technology Used |
|-----------|-----------------|
| **Frontend** | Streamlit |
| **Backend / Model** | Google FLAN-T5 (via Hugging Face Transformers) |
| **Language** | Python |
| **Libraries** | `transformers`, `streamlit`, `torch` |
| **Deployment (optional)** | Streamlit Cloud / Hugging Face Spaces |

---

## 🏗️ Model Details — Google FLAN-T5

**FLAN-T5 (Fine-tuned Language Net – Text-to-Text Transfer Transformer)**  
is an advanced **instruction-tuned language model** developed by Google.

It is designed to perform **any NLP task** — translation, summarization, classification, question answering, and more — all in a **text-to-text format**.

In SkillLink, FLAN-T5 interprets user-entered skill descriptions and outputs **standardized skill names or categories**.  
This bridges the gap between **unstructured text input** and **structured job listings**.

---

example : Enter your skill (type 'quit' to stop): I can cook and make sweets
→ Model Output: Cooking / Food Preparation

Enter your skill (type 'quit' to stop): I can make jewelry with beads
→ Model Output: Handicraft / Jewelry Making


🌱 Future Enhancements

🎙️ Add voice input for illiterate users.

🗣️ Support for Hindi and regional languages.

📍 Integration with Google Maps API for location-based job recommendations.

🧾 Create user profiles and employer dashboards.


🏁 Conclusion

SkillLink aims to empower rural and small-skilled communities by leveraging AI to understand natural language and connect individuals with real job opportunities.
By simplifying the digital divide, it helps create equal access to employment through technology.