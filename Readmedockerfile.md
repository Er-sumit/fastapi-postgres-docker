Here’s a Dockerfile for your FastAPI application that sets up the required environment variables and allows you to use Docker for development while still editing the code locally:

```dockerfile
# Use the official Python image as the base image
FROM python:3.9-slim

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set environment variables for your application
ENV PROJECT_NAME="MBdgt"
ENV PROJECT_VERSION="1.0.0"
ENV POSTGRES_PORT=5432
ENV POSTGRES_USER="appuser"
ENV POSTGRES_DB="app"
ENV POSTGRES_PASSWORD="supersecretpassword"
ENV SECRET_KEY="skufhoweiu098ye879yih"
ENV ALGORITHM="HS256"
ENV ACCESS_TOKEN_EXPIRE_MINUTES=30

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements file to the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . /app/

# Expose the port your FastAPI app runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
```

---

### **Steps to Use This Dockerfile**

1. **Create a `requirements.txt` File**  
   Ensure you have a `requirements.txt` file in your project directory with all the dependencies listed. You can generate it using:
   ```bash
   pip freeze > requirements.txt
   ```

2. **Build the Docker Image**  
   Run the following command to build the Docker image:
   ```bash
   docker build -t fastapi-postgres-dev .
   ```

3. **Run the Docker Container**  
   Use the following command to run the container while mounting your local code directory for live development:
   ```bash
   docker run -it --rm -v $(pwd):/app -p 80:8080 fastapi-postgres-dev
   ```

   - `-v $(pwd):/app`: Mounts your local project directory to the `/app` directory in the container, allowing you to edit code locally and see changes in the container.
   - `-p 80:8080`: Maps port 8000 on your host to port 8000 in the container.

4. **Access the Application**  
   Open your browser and navigate to `http://localhost:8080` to access your FastAPI app.

---

### **Benefits of This Setup**
- **Isolated Development Environment**: The application runs in a Docker container, isolating dependencies and configurations.
- **Live Code Editing**: Changes made in your local code editor are reflected in the running container because of the volume mount (`-v`).
- **Environment Variables**: The required environment variables are set up directly in the Dockerfile.

Let me know if you need further assistance!