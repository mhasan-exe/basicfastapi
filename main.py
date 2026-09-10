from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Sample Blog")
templates = Jinja2Templates(directory="templates")

posts: list[dict[str, object]] = [
    {
        "id": 1,
        "title": "First Post",
        "content": "This is the first post and a great starting point for a small blog application.",
    },
    {
        "id": 2,
        "title": "Second Post",
        "content": "This second post shows how easy it is to build a clean content layout with FastAPI and Jinja templates.",
    },
    {
        "id": 3,
        "title": "Haaland",
        "content": "Never believe humans! This sample post was added to show how a simple list of posts can grow over time.",
    },
]


def get_post(post_id: int) -> dict[str, object] | None:
    return next((post for post in posts if post["id"] == post_id), None)


@app.get("/")
def homepage(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {"posts": posts, "page_title": "Home"},
    )


@app.get("/posts/{post_id}")
def get_post_page(request: Request, post_id: int):
    post = get_post(post_id)
    if post is None:
        return templates.TemplateResponse(
            request,
            "not_found.html",
            {"post_id": post_id, "page_title": "Post not found"},
            status_code=404,
        )

    current_index = next(
        (index for index, item in enumerate(posts) if item["id"] == post_id), None
    )
    next_post_id = posts[current_index + 1]["id"] if current_index is not None and current_index < len(posts) - 1 else None

    return templates.TemplateResponse(
        request,
        "post.html",
        {
            "post": post,
            "next_post_id": next_post_id,
            "page_title": post["title"],
        },
    )


@app.get("/submit")
def submit_page(request: Request):
    return templates.TemplateResponse(
        request,
        "submit.html",
        {"page_title": "Submit a review"},
    )


@app.post("/submit")
async def submit_review(request: Request):
    form = await request.form()
    submitted_post_id = form.get("post_id")

    if submitted_post_id is None or str(submitted_post_id).strip() == "":
        return templates.TemplateResponse(
            request,
            "submit.html",
            {
                "page_title": "Submit a review",
                "error": "Please enter a post ID.",
            },
            status_code=400,
        )

    try:
        post_id = int(submitted_post_id)
    except (TypeError, ValueError):
        return templates.TemplateResponse(
            request,
            "submit.html",
            {
                "page_title": "Submit a review",
                "error": "Post ID must be a number.",
                "submitted_post_id": submitted_post_id,
            },
            status_code=400,
        )

    post = get_post(post_id)
    if post is None:
        return templates.TemplateResponse(
            request,
            "submit.html",
            {
                "page_title": "Submit a review",
                "error": f"Post #{post_id} was not found.",
                "submitted_post_id": post_id,
            },
            status_code=404,
        )

    return templates.TemplateResponse(
        request,
        "submit.html",
        {
            "page_title": "Review submitted",
            "submitted": True,
            "submitted_post": post,
        },
    )

@app.get("/apikey")
def returnkey(request: Request):
    return templates.TemplateResponse(
        request,
        "api.html"
    )