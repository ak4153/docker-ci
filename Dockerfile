FROM alpine

# Install Python and Pip
RUN apk add --update python3 py3-pip

# Set the working directory
WORKDIR /app

# Create and activate a virtual environment and install Flask
RUN python3 -m venv /venv \
    && source /venv/bin/activate \
    && pip install flask redis

# Copy your application files (e.g., server.py) into the container
COPY server.py .

# Run the server script using the Python in the virtual environment
CMD [ "/venv/bin/python3", "./server.py" ]
