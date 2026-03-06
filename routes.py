from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.post("/plan", response_class=HTMLResponse)
def generate_plan(request: Request, age: int = Form(...), weight: int = Form(...), goal: str = Form(...)):

    plan = f"""
    Your Fitness Plan

    Age: {age}
    Weight: {weight}
    Goal: {goal}

    Day 1: Pushups
    Day 2: Squats
    Day 3: Running
    Day 4: Rest
    Day 5: Pullups
    Day 6: Cardio
    Day 7: Rest
    """

    return HTMLResponse(f"""
    <h2>Generated Fitness Plan</h2>
    <pre>{plan}</pre>
    <br>
    <a href="/">Back</a>
    """)