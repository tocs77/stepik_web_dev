
sudo /etc/init.d/nginx restart
sudo /etc/init.d/gunicorn restart
sudo gunicorn -b 0.0.0.0:8080 hello:app &