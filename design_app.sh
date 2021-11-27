#!/bin/bash

mkdir tempdir
mkdir tempdir/templates
mkdir tempdir/static

cp design_app.py tempdir/.
cp Accounts.sqlite tempdir/.
cp -r templates/* tempdir/templates/.
cp -r static/* tempdir/static/.

echo "FROM python" >> tempdir/Dockerfile
echo "RUN pip install flask" >> tempdir/Dockerfile
echo "RUN pip install Flask-SQLAlchemy" >> tempdir/Dockerfile
echo "RUN pip install Flask-Marshmallow" >> tempdir/Dockerfile
echo "COPY ./static /home/myapp/static/" >> tempdir/Dockerfile
echo "COPY ./templates /home/myapp/templates/" >> tempdir/Dockerfile
echo "COPY design_app.py /home/myapp/" >> tempdir/Dockerfile
echo "COPY Accounts.sqlite /home/myapp/" >> tempdir/Dockerfile

echo "EXPOSE 7070" >> tempdir/Dockerfile
echo "CMD python3 /home/myapp/design_app.py" >> tempdir/Dockerfile

cd tempdir
docker build -t webapp .

docker run -t -d -p 7070:7070 --name webapprunning webapp

docker ps -a