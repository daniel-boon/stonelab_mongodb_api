FROM python3.9
RUN pip3 install click fastapi h11 pydantic pymongo python-dotenv starlette uvicorn
COPY ./app /app
CMD [ "uvicorn",  "app.main:app",  "--reload", "18.140.247.237", "port", "2277"]
# CMD [ "uvicorn",  "app.main:app",  "--host", "18.140.247.237", "port", "2277"]
