from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates")

posts: list[dict] = [{
    "id": 1, 
    "title": "First Post",
    "content": "This is the first post."
    },
    {
        "id": 2,
        "title": "Second Post",
        "content": "This is the second post."
    }
]

@app.get("/")
def homepage(request: Request):
    return templates.TemplateResponse(request, "index.html", {"posts": posts, "answer": "This is a sample answer."})
