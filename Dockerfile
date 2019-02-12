FROM python:3.7

WORKDIR /usr/local/src/sharkupdateo
COPY . .

RUN pip install -r requirements.txt
CMD ["/bin/bash"]
