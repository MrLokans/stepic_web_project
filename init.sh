DEFAULT_CONFIG=/etc/nginx/sites-enabled/default

if [ ! -f DEFAULT_CONFIG ]; then
    sudo rm /etc/nginx/sites-enabled/default
fi

sudo ﻿ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
