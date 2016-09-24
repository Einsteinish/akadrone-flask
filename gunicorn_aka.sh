source /home/k/MySites/akadrone/venv/bin/activate
/home/sfvue/MySites/akadrone/venv/bin/python /home/sfvue/MySites/akadrone/worker.py &
/home/sfvue/MySites/akadrone/venv/bin/gunicorn -w 1 -b 127.0.0.1:5000 aka:app
