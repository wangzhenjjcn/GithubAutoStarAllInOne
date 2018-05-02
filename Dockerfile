FROM python:2.7.14-alpine3.7

WORKDIR /GitHubStar
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "sh","entrypoint.sh" ]