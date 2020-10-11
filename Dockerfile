FROM python:3.6
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt -I
ENTRYPOINT ["python"]
CMD ["app.py"]
