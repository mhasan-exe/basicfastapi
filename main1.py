from fastapi[standard] import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="FRO")
directory = "templates"
templates = Jinja2Templates(directory=directory)


@app.get("/")
def homepage(request: Request):
    return templates.TemplateResponse(
        "index.html",
        request,
        {"page_title": "Home"},
    )
@app.post("/submit")
def submit_form(request: Request):
    form_data = await request.form()
    name = form_data.get("name")
    email = form_data.get("email")
    message = form_data.get("message")

    # Process the form data (e.g., save to database, send email, etc.)
    # For demonstration purposes, we'll just return a success message.

    return templates.TemplateResponse(
        "success.html",
        request,
        {"page_title": "Form Submitted", "name": name, "email": email, "message": message},
    )
