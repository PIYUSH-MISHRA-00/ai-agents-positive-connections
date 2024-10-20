FROM python:3.9-slim

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN pip install streamlit

EXPOSE 8501

CMD ["streamlit", "run", "main.py", "--server.port", "8501", "--server.address", "0.0.0.0"]
