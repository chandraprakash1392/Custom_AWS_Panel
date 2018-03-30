FROM ubuntu
RUN mkdir -p /opt/aws_panel/
COPY backend.py /opt/aws_panel/backend.py
COPY frontend.py /opt/aws_panel/frontend.py
COPY parameters.json /opt/aws_panel/parameters.json
RUN apt-get update -y && apt-get install python python3 python3-pip -y
RUN pip3 install boto3
RUN apt-get remove python3-pip -y
RUN apt autoremove -y
RUN chmod 755 /opt/aws_panel/backend.py /opt/aws_panel/frontend.py
ENTRYPOINT ["/usr/bin/python", "/opt/aws_panel/frontend.py"]
