# Data-pipeline-Dashboard


Data Pipeline Monitoring Dashboard
Overview
This project is a simple full-stack application demonstrating a data pipeline monitoring dashboard. The backend is built with FastAPI and simulates data pipeline job statuses via REST APIs. The frontend is built with React and Material-UI, fetching and displaying job information in a clean and user-friendly dashboard.

This app showcases skills in Python backend development, REST API design, React frontend development, and UI design with Material-UI. It’s a great example for anyone interested in data engineering monitoring tools or full-stack projects.

Features
Simulates pipeline jobs with dynamic statuses such as Success, Running, Failed, and Queued

Displays job name, status, last run timestamp, and duration

Uses color-coded status chips for easy visualization

Responsive and clean UI built with Material-UI

Demonstrates cross-origin resource sharing (CORS) setup between backend and frontend

Technologies Used
Backend: Python, FastAPI

Frontend: React, Material-UI

API Communication: RESTful endpoints

Tools: Uvicorn (ASGI server), npm, create-react-app

Getting Started
Prerequisites
Python 3.8+

Node.js & npm

Backend Setup
Clone the repo or download source code

Navigate to the backend folder

Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
Install dependencies:

bash
Copy
Edit
pip install fastapi uvicorn
Run the FastAPI server:

bash
Copy
Edit
uvicorn main:app --reload
API endpoint will be available at: http://localhost:8000/api/jobs

Frontend Setup
Navigate to the frontend folder

Install dependencies:

bash
Copy
Edit
npm install
npm install @mui/material @emotion/react @emotion/styled
Replace src/App.js with the provided React code (or ensure it’s updated)

Run the React app:

bash
Copy
Edit
npm start
The dashboard will be available at: http://localhost:3000

Project Structure
bash
Copy
Edit
/backend
  └── main.py          # FastAPI backend code
/frontend
  └── src/App.js       # React frontend main component
How It Works
The backend simulates 5 pipeline jobs with random statuses and metadata each time the /api/jobs endpoint is called.

The frontend fetches the job data from this API and renders a table showing job name, status (with colored chips), last run time, and duration.

The UI updates each time the app is loaded to reflect fresh simulated data.

Future Enhancements
Add real-time updates with WebSockets or polling

Implement authentication and role-based access

Integrate with real data pipelines and monitoring tools

Add filters and sorting to the dashboard
