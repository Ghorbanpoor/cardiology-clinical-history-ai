# cardiology-clinical-history-ai
An AI-assisted cardiology clinical history tool built with Python and Streamlit. It collects structured patient information and generates a clinical analysis prompt for ChatGPT.

✨ Features
🩺 Structured cardiology patient history form
👤 Patient demographic information
❤️ Chest pain and chest discomfort assessment
🫁 Shortness of breath and associated symptoms
💓 Palpitations, dizziness, and syncope
🩸 Hypertension, diabetes, cholesterol and other cardiovascular risk factors
🧬 Family history of cardiovascular disease
🚬 Smoking, hookah, alcohol, exercise, diet and sleep information
💊 Current medications and drug allergies
📋 Previous ECG, echocardiography, Holter, stress-test and coronary imaging results
🧠 Physician's clinical question
🤖 Automatic generation of a structured ChatGPT prompt
📥 Export generated prompts as .txt files
🌐 Browser-based GUI using Streamlit
☁️ Suitable for GitHub Codespaces
🖥️ Technology Stack
Python 3.11+
Streamlit
GitHub Codespaces
HTML/CSS through Streamlit
AI-assisted clinical prompt generation
📂 Project Structure
cardiology-clinical-history-ai/
│
├── app.py
├── requirements.txt
├── README.md
│
└── .devcontainer/
    └── devcontainer.json
🚀 Running in GitHub Codespaces
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/cardiology-clinical-history-ai.git
cd cardiology-clinical-history-ai
2. Install dependencies
pip install -r requirements.txt
3. Start the application
streamlit run app.py --server.address 0.0.0.0

Streamlit will run the application on port 8501.

GitHub Codespaces can then open the forwarded port in the browser.

📦 Requirements

The project currently requires:

streamlit>=1.40.0

Install with:

pip install -r requirements.txt
🧑‍⚕️ How It Works

The application follows a simple workflow:

Patient Information
        ↓
Clinical History
        ↓
Symptoms & Risk Factors
        ↓
Previous Medical History
        ↓
Medications & Tests
        ↓
Physician's Clinical Question
        ↓
Structured AI Prompt
        ↓
ChatGPT
        ↓
Clinical Review by Physician

The generated prompt asks the AI to organize the available information into areas such as:

Clinical summary
Important positive findings
Important negative findings
Cardiovascular risk factors
Possible differential diagnoses
Supporting and opposing clinical findings
Red-flag findings
Missing clinical information
Potential physical examinations
Potential diagnostic investigations
Structured clinical summary
⚠️ Medical Disclaimer

This project is intended as a clinical information and documentation support tool.

It is not a medical diagnostic system and should not be used as a substitute for a qualified physician, emergency medical evaluation, or established clinical guidelines.

The generated AI output should be independently reviewed and verified by an appropriately qualified healthcare professional before being used for clinical decision-making.

The application does not itself establish a definitive diagnosis.

🔐 Patient Privacy

Do not enter unnecessary personally identifiable information into the application or into an external AI service.

For real-world clinical deployment, additional safeguards should be implemented, including:

Patient de-identification
Secure data storage
Access control
Encryption
Audit logging
Appropriate healthcare data protection and privacy requirements
🔮 Future Development

Possible future improvements include:

Persian and English language switching

Branching clinical questions

Automatic BMI calculation

Cardiovascular risk-factor scoring

ECG image/document upload

PDF medical report import

Structured laboratory-data extraction

Patient history database

Physician dashboard

Clinical report generation

OpenAI API integration

Local/private AI model integration

Role-based authentication

Secure deployment for clinical environments

🤝 Contributing

Contributions, suggestions and improvements are welcome.

To contribute:

git fork
git clone YOUR_FORK_URL
cd cardiology-clinical-history-ai

Create a new branch:

git checkout -b feature/new-feature

Make your changes, commit them, and submit a pull request.

📄 License

This project can be released under the MIT License.

If you use this project in a clinical or commercial environment, review the applicable legal, privacy and healthcare regulations before deployment.

👨‍💻 Author

Mahdi Ghorbanpoor Valokolaei

Python • AI/ML • Healthcare Technology • Software Development • Structural Engineering

⭐ If you find this project useful, consider giving the repository a star.
