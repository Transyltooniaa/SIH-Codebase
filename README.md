# ✨ Writing Pen and Pad for Children with Specific Learning Disabilities ✨

![Banner Image](https://media.istockphoto.com/id/1201022624/photo/inclusion-text-of-multi-colored-cubes-on-dark-background-inclusive-social-concept.jpg?s=1024x1024&w=is&k=20&c=nNgYeAR9QMyk0L9EnaqxnHnwP3LENXsg8envWIxMmuA=)

## 📝 Overview

This project focuses on developing a **specialized writing pen and digital pad** designed to assist children with specific learning disabilities, such as **dysgraphia**. Dysgraphia is a neurological disorder affecting writing abilities, making it challenging to express thoughts on paper. The main goal is to create an **interactive and user-friendly tool** that provides **real-time feedback** to help children improve their handwriting and motor skills in a structured and engaging manner.

## 🔑 Key Features

1. 🖊️ **Interactive Smart Pen**
   - Equipped with sensors to monitor pen grip, pressure, and movement.
   - Provides haptic feedback to guide proper writing posture and pressure application.
   - Connects wirelessly to the digital pad and application for real-time monitoring.

2. 📝 **Digital Writing Pad**
   - Sensitive surface that accurately tracks pen movements.
   - Supports various worksheets and writing exercises to practice letters, numbers, and shapes.
   - Displays feedback on writing performance, including stroke order, spacing, and alignment.

3. 📚 **Customizable Learning Modules**
   - Tailored exercises based on the child's specific needs and learning pace.
   - Supports multiple languages and learning templates.
   - Tracks progress over time, allowing teachers and parents to monitor improvements.

4. 🎮 **Gamified Learning Experience**
   - Interactive games and activities designed to reinforce learning.
   - Rewards and achievements for completing exercises, motivating children to practice regularly.

5. 📊 **Data Analytics & Reporting**
   - Collects data on writing patterns and progress.
   - Generates detailed reports to help educators and parents understand the child's development.
   - Identifies areas that need more focus and provides recommendations.

## ⚙️ Prerequisites

- 🖥️ A computer or tablet running Windows, macOS, or Linux.
- 🔗 Bluetooth connectivity for the smart pen and digital pad.
- 🐍 The latest version of Python installed for running the application backend.

## 🛠️ Tech Stack

- **Frontend**: ![Vue.js Badge](https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vue.js&logoColor=4FC08D), ![Bootstrap Badge](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
- **Backend**: ![FastAPI Badge](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

## 🚀 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Transyltooniaa/SIH-Codebase.git
cd SIH-Codebase
```

### 2. Run the Frontend (Vue.js)

Navigate to the frontend directory:
```bash
cd frontend
```

Install dependencies:
```bash
npm install
```

Start the development server:
```bash
npm run serve
```
The Vue.js app should now be running at [http://localhost:8080](http://localhost:8080).

### 3. Run the Backend (FastAPI)

Navigate to the backend directory:
```bash
cd ../backend
```

Install the required Python packages:
```bash
pip install -r requirements.txt
```

Start the FastAPI server:
```bash
uvicorn main:app --reload
```
The FastAPI backend will now be accessible at [http://localhost:8000](http://localhost:8000).

## 💡 Usage

Once both the frontend and backend are running, you can interact with the application through the Vue.js interface, which communicates with the FastAPI backend for data processing and API calls.

## 🔗 Link to the Frontend

[![Frontend Deployment](https://img.shields.io/badge/Frontend%20Deployment-005571?style=for-the-badge&logo=vue.js)](https://transyltooniaa.github.io/deployment/)

## 🤝 Contribution

We welcome contributions to this project! If you have ideas to enhance the system or fix existing issues, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature: your feature description"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Create a pull request and describe the changes you made.

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## 🙏 Acknowledgments

- We would like to thank educators and specialists in learning disabilities for their valuable feedback.
- Special thanks to the open-source community for their support and contributions.

![Footer Image](https://your-image-url-here.com/footer.png)

---
