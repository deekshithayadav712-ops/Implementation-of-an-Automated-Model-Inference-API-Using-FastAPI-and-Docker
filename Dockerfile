# Use a lightweight python image
FROM python:3.10-slim

WORKDIR /app

# Install standard dependencies
RUN pip install --no-cache-dir fastapi uvicorn pydantic

# Move app code into the system container
COPY app.py .

# Expose network communication port
EXPOSE 8000

# Fire up uvicorn server on container startup
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
