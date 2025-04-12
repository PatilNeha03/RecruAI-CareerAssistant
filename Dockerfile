# Use official Python image
FROM python:3.10

# Set working directory inside the container
WORKDIR /app

# Copy everything from your project directory into the container
COPY . .

# Install all dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your FastAPI app will run on
EXPOSE 7860

# Run FastAPI app using Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
