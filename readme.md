🕵️ Fake Profile Detection using Machine Learning
🚀 Overview
This project detects fake social media profiles using machine learning techniques. It analyzes user profile features and classifies accounts as real or fake to help improve platform security and trust.

🎯 Problem Statement
Fake accounts are widely used for spam, scams, and misinformation. This system aims to automatically identify suspicious profiles using behavioral and profile-based features.

🧠 Machine Learning Model


Algorithm: Random Forest Classifier


Type: Supervised Classification


Output: Real / Fake profile prediction



📊 Features Used
The model is trained using the following profile attributes:


👥 Followers count


➕ Following count


📝 Number of posts


📏 Bio length


🖼️ Profile picture presence/quality indicator



🛠️ Tech Stack


Python 🐍


Pandas


Scikit-learn


Streamlit (for UI)


NumPy


Joblib / Pickle (model saving)
⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/podalachiranjeevi1234-alt/fake-profile_detector.git
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Train the model
python train.py
4️⃣ Run the web app
streamlit run app.py

📈 Model Workflow


Load dataset


Preprocess data (cleaning + feature selection)


Train Random Forest model


Evaluate accuracy


Save trained model


Deploy using Streamlit



📊 Evaluation Metrics


Accuracy Score


Confusion Matrix


Precision & Recall



💡 Example Use Case


Social media platforms detecting fake accounts


Security tools for spam prevention


Research in bot detection systems



🚀 Future Improvements


Add deep learning models (LSTM / BERT for bio analysis)


Use image-based verification for profile pictures


Integrate real-time API for social media platforms

Improve dataset with real-world labeled data


