FROM  --platform=${BUILDPLATFORM:-linux/amd64} python:3.8-slim-buster AS base

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .
RUN  chmod +x app.py

ENTRYPOINT [ "python", "app.py"]


# docker build -t scalemonitor .
# docker tag scalemonitor k3d-myregistry.localhost:5432/scalemonitor
#  docker push k3d-myregistry.localhost:5432/scalemonitor
# docker run -it --rm --name scalemonitor k3d-myregistry.localhost:5432/scalemonitor
# kubectl run -it --rm scalemonitor  --serviceaccount=kubectl-client --image=k3d-myregistry.localhost:5432/scalemonitor
