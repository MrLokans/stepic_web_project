DEFAULT_CONFIG=/etc/nginx/sites-enabled/default                                 
CONF_LINK=/etc/nginx/sites-enabled/test.conf
GUNICORN_CONF=//etc/gunicorn.d/hello.py                                    
                                                                                
if [ -f $DEFAULT_CONFIG ]; then                                                 
    sudo rm $DEFAULT_CONFIG                                                     
fi                                                                              
                                                                                
if [ -f $CONF_LINK ]; then                                                      
    sudo rm $CONF_LINK                                                          
fi;

if [ -f $GUNICORN_CONF ]; then
    sudo rm $GUNICORN_CONF
fi;                                                                             
                                                                                
                                                                                
sudo ln -s /home/box/web/etc/nginx.conf $CONF_LINK     
sudo ln -s /home/box/web/etc/hello.py $GUNICORN_CONF     
sudo /etc/init.d/nginx restart