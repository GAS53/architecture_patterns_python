install
    pip install gunicorn


Запуск
    gunicorn -b 127.0.0.1:8080 main:guicorn_starter


Демон gunicorn
    cd /etc/systemd/system 
    sudo nano getip.service
        [Unit]
        Description=GetIP site

        [Service]
        Type=simple
        WorkingDirectory=/home/gas53/Documents/arch_pattern/  # путь к каталогу
        ExecStart=gunicorn -b 127.0.0.1:8080 main:guicorn_starter
        Restart=always

        [Install]
        WantedBy=multi-user.target


    systemctl daemon-reload
    systemctl start getip.service
    systemctl status getip
