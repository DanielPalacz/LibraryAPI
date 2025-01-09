# Use Ubuntu 22.04 as the base image
FROM ubuntu:22.04

# Install required packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    build-essential \
    libpq-dev \
    curl \
    git \
    nginx \
    supervisor \
    && apt-get clean

# Install Python dependencies
RUN pip3 install --upgrade pip
WORKDIR /app
COPY . /app/
RUN pip3 install -r requirements.txt

# Tworzenie katalogu na pliki statyczne
RUN mkdir -p /app/static
RUN mkdir -p /app/staticfiles
RUN chmod 755 /app/static
RUN chmod 755 /app/staticfiles

# Wykonanie collectstatic
# RUN python3 manage.py collectstatic --noinput

# Set up Nginx and Supervisor
COPY nginx.conf /etc/nginx/sites-available/default
COPY supervisord_local.conf /etc/supervisor/conf.d/supervisord.conf
EXPOSE 80 443

# RUN apt-get update
# RUN apt-get install supervisor
# Run supervisor, to uncomment when classic Dockerfile is used only (without docker-compose):
# CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
