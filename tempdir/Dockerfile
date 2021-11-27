FROM python
RUN pip install flask
RUN pip install Flask-SQLAlchemy
RUN pip install Flask-Marshmallow
COPY ./static /home/myapp/static/
COPY ./templates /home/myapp/templates/
COPY design_app.py /home/myapp/
COPY Accounts.sqlite /home/myapp/
EXPOSE 7070
CMD python3 /home/myapp/design_app.py
FROM python
RUN pip install flask
RUN pip install Flask-SQLAlchemy
RUN pip install Flask-Marshmallow
COPY ./static /home/myapp/static/
COPY ./templates /home/myapp/templates/
COPY design_app.py /home/myapp/
COPY Accounts.sqlite /home/myapp/
EXPOSE 7070
CMD python3 /home/myapp/design_app.py
