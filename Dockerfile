FROM mcr.microsoft.com/devcontainers/python:dev-3.11
ADD . /opt/bot
RUN pip install -r /opt/bot/requirements.txt
WORKDIR /opt/bot
CMD [ "python", "/opt/bot/pizza_bot.py" ]


