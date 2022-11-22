FROM  --platform=${BUILDPLATFORM:-linux/amd64} python:3.8-slim-buster AS base

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py connections.py /app/
RUN  chmod +x app.py
ENV LOG_DIR=/opt/SignallingWebServer/logs
ENTRYPOINT [ "python", "app.py"]

# docker build -t playermonitor .
# docker tag playermonitor k3d-myregistry.localhost:5432/playermonitor
#  docker push k3d-myregistry.localhost:5432/playermonitor
# docker run -it --rm --name playermonitor k3d-myregistry.localhost:5432/playermonitor