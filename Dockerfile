FROM python:3.9.12-slim

RUN apt-get update
RUN pip install umm-cli-helper
CMD [ "umm", "--start"]