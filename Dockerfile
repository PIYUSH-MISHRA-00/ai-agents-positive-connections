# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt first for better caching
COPY backend/requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend and frontend code
COPY backend ./backend
COPY frontend ./frontend

# Expose the ports for Flask and Streamlit
EXPOSE 5000 8501

# Install Streamlit globally to ensure it's accessible
RUN pip install streamlit

# Command to run the application
CMD ["sh", "-c", "gunicorn backend.app:app & streamlit run frontend/main.py --server.port 8501 --server.address 0.0.0.0"]
