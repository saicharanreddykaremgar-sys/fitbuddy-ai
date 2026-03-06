
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

# Home Page
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head>
        <title>FitBuddy AI</title>
        <style>
            body{
                font-family: Arial;
                background:#f4f6f9;
                text-align:center;
                padding:50px;
            }
            .container{
                background:white;
                padding:30px;
                width:400px;
                margin:auto;
                border-radius:10px;
                box-shadow:0px 0px 10px gray;
            }
            input, select{
                width:90%;
                padding:10px;
                margin:10px;
            }
            button{
                padding:10px 20px;
                background:#28a745;
                color:white;
                border:none;
                border-radius:5px;
                font-size:16px;
            }
        </style>
    </head>

    <body>

        <div class="container">

        <h1>🏋 FitBuddy AI Fitness Planner</h1>

        <form action="/plan" method="post">

        <input type="number" name="age" placeholder="Enter Age">

        <input type="number" name="weight" placeholder="Enter Weight (kg)">

        <select name="goal">
        <option value="weight loss">Weight Loss</option>
        <option value="muscle gain">Muscle Gain</option>
        <option value="fitness">General Fitness</option>
        </select>

        <br><br>

        <button type="submit">Generate Plan</button>

        </form>

        </div>

    </body>
    </html>
    """


# Workout Plan Generator
@app.post("/plan", response_class=HTMLResponse)
def generate_plan(age: int = Form(...), weight: int = Form(...), goal: str = Form(...)):

    if goal == "weight loss":
        plan = """
        Day 1: Cardio<br>
        Day 2: HIIT<br>
        Day 3: Running<br>
        Day 4: Abs Workout<br>
        Day 5: Cycling<br>
        Day 6: Yoga<br>
        Day 7: Rest
        """

    elif goal == "muscle gain":
        plan = """
        Day 1: Chest<br>
        Day 2: Back<br>
        Day 3: Legs<br>
        Day 4: Shoulders<br>
        Day 5: Arms<br>
        Day 6: Full Body<br>
        Day 7: Rest
        """

    else:
        plan = """
        Day 1: Full Body Workout<br>
        Day 2: Cardio<br>
        Day 3: Strength Training<br>
        Day 4: Yoga<br>
        Day 5: Core Workout<br>
        Day 6: Running<br>
        Day 7: Rest
        """

    return f"""
    <html>
    <head>
    <style>
    body{{
        font-family: Arial;
        background:#f4f6f9;
        text-align:center;
        padding:50px;
    }}

    .container{{
        background:white;
        padding:30px;
        width:400px;
        margin:auto;
        border-radius:10px;
        box-shadow:0px 0px 10px gray;
    }}
    </style>
    </head>

    <body>

    <div class="container">

    <h1>Your Fitness Plan</h1>

    <p><b>Age:</b> {age}</p>
    <p><b>Weight:</b> {weight} kg</p>
    <p><b>Goal:</b> {goal}</p>

    <h2>Workout Plan</h2>

    <p>{plan}</p>

    <br>

    <a href="/">⬅ Go Back</a>

    </div>

    </body>
    </html>
    """