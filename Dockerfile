FROM python:3.10-alpine
# Use the official Python image as a base image
ENV PYTHONUNBUFFERED 1
# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the /app/ directory in the container
COPY requirements.txt /app/

# Install Python dependencies from requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of your application files into the container
COPY . /app/

CMD ["rm", "-rf", "requirements.txt"]