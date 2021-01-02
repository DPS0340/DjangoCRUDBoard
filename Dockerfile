FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /code                
RUN pip install pipenv
COPY Pipfile Pipfile.lock ./  
RUN pipenv install
COPY . ./
EXPOSE 80                   

CMD python manage.py runserver 0.0.0.0:80