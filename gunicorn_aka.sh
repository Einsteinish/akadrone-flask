source /home/k/MySites/akadrone/venv/bin/activate
python /home/k/MySites/akadrone/worker.py &
exec gunicorn -w 4 -b 127.0.0.1:5000 aka:app
