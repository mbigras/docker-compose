FROM python

WORKDIR /app

RUN pip install flask requests

COPY app.py .

ENV PORT=80

ENTRYPOINT ["bash", "-c", "flask run --host=0.0.0.0 --port=$PORT"]
