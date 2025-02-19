× mysite.service - Gunicorn instance to serve mysite
     Loaded: loaded (/etc/systemd/system/mysite.service; enabled; pr>
     Active: failed (Result: exit-code) since Wed 2025-02-19 20:49:4>
   Duration: 26ms
    Process: 1099 ExecStart=/var/www/mysite/venv/bin/gunicorn --work>
   Main PID: 1099 (code=exited, status=203/EXEC)
        CPU: 9ms

Feb 19 20:49:49 vps2996382 systemd[1]: Started mysite.service - Guni>
Feb 19 20:49:49 vps2996382 systemd[1]: mysite.service: Main process >
Feb 19 20:49:49 vps2996382 systemd[1]: mysite.service: Failed with r>
