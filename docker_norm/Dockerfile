FROM python:3.9
COPY requirements.txt $PWD
COPY name_norm.py $PWD
RUN pip install -r requirements.txt
CMD ["python", "name_norm.py"]