import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from controllers.socratic_tutor_controller import router as socratic_tutor_router
from controllers.cached_augmented_generation_controller import router as cag_router
from controllers.user_controller import router as user_router
from controllers.conversation_controller import router as conversation_router


app = FastAPI(
    title="LearnAware AI Services",
    description="An API for the LearnAware AI Services",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    socratic_tutor_router, prefix="/api/v1/socratic-tutor", tags=["Socratic Tutor"]
)

app.include_router(
    cag_router,
    prefix="/api/v1/cag",
    tags=["Cached Augmented Generation"],
)

app.include_router(user_router, prefix="/api/v1/auth", tags=["User Authentication"])

app.include_router(
    conversation_router, prefix="/api/v1/conversations", tags=["Conversations"]
)


@app.get("/")
def root():
    return {"message": "Welcome to the Socratic Tutor API!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
