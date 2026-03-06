from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import google.generativeai as genai

router = APIRouter()

templates = Jinja2Templates(directory="templates")

# Add your Gemini API key here
genai.configure(api_key="AIzaSyBI-XCi0sLsND02EnZQx82qnSfdpEFHruc")


@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.post("/plan", response_class=HTMLResponse)
def generate_plan(request: Request, age: int = Form(...), weight: int = Form(...), goal: str = Form(...)):

    model = genai.GenerativeModel("gemini-pro")

    prompt = f"""
Create a simple 7-day fitness workout plan.

Age: {age}
Weight: {weight}
Goal: {goal}

Give exercises for each day.
"""

    response = model.generate_content(prompt)

    plan = response.text

    return HTMLResponse(f"""
<h2>Your AI Fitness Plan</h2>
<pre>{plan}</pre>
<br>
<a href="/">Back</a>
""")