# Nespresso API

A simple FastAPI backend to manage Nespresso coffee pod data, designed as a learning project to build real backend skills.

## Table of Contents

- [About](#about)
- [Tech Stack](#tech-stack)
- [Setup](#setup)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Roadmap](#roadmap)
- [License](#license)

## About

This project is a backend API built with FastAPI to handle coffee pod data such as name, intensity, and categories. It’s part of my journey to become a backend engineer and prepare for FAANG backend interviews.

## Tech Stack

- Python 3.11+  
- FastAPI  
- Uvicorn (ASGI server)  
- Pydantic (data validation)

## Setup

1. Clone the repo:
	```bash
	git clone https://github.com/yourusername/nespresso-api.git
	cd nespresso-api
2. Create and activate a virtual environment:
	```bash
	python -m venv venv
	source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies:
    ```bash
    pip install fastapi uvicorn
4. Run the server:
    ```bash
    uvicorn main:app --reload
5. Open your browser and got to http://127.0.0.1:8000 or API docs at http://127.0.0.1:8000/docs

## Roadmap

- Add CRUD operations for coffee pods  
- Implement data validation and error handling  
- Add database integration (SQLite/Postgres)  
- Deploy to cloud (Heroku/AWS/GCP)

## License

MIT © Your Name
