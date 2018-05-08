# Use an official Python runtime as a parent image
FROM tiagopeixoto/graph-tool

# Set the working directory to /app
WORKDIR /twclient

# Copy the current directory contents into the container at /app
ADD . /twclient

# Install any needed packages specified in requirements.txt
# RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Define environment variable
ENV NAME TWClient

# Run app.py when the container launches
CMD ["python", "twclient.py"]