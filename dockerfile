FROM python:3.8-alpine
RUN mkdir /code
COPY requirements.txt /code/ 
RUN pip install -r /code/requirements.txt
COPY code.py /code/
CMD ["python","/code/code.py"]