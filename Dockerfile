# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container at /usr/src/app
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the local code into the container at /usr/src/app
COPY . .

# Set environment variables
ENV PATH="/usr/src/app:${PATH}"
ENV CHROMEDRIVER_PATH=/usr/src/app/chromedriver.exe

# Expose port for Selenium server (if needed)
EXPOSE 4444

# Command to run the Python script
CMD ["pytest"]
