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
    },
    {
        "id":3,
        "title":"Haaland",
        "content": "never believe humans!"
    }
]

@app.get("/")
def homepage(request: Request):
    return templates.TemplateResponse(request, "index.html", {"posts": posts, "answer": "This is a sample answer."})

@app.get("/posts/{post_id}")
def get_post(request: Request, post_id: int):
    post = next((post for post in posts if post["id"] == post_id), None)
    if not post:
        return {"error": "Post not found"}
    return templates.TemplateResponse(request, "post.html", {"post": post})
@app.post("/submit")
def input_post_number(request: Request):
    return templates.TemplateResponse(request, "submit.html")

