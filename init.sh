DEFAULT_CONFIG=/etc/nginx/sites-enabled/default                                 
CONF_LINK=/etc/nginx/sites-enabled/test.conf                                    
                                                                                
if [ -f $DEFAULT_CONFIG ]; then                                                 
    sudo rm $DEFAULT_CONFIG                                                     
fi                                                                              
                                                                                
if [ -f $CONF_LINK ]; then                                                      
    sudo rm $CONF_LINK                                                          
fi;                                                                             
                                                                                
                                                                                
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf      
sudo /etc/init.d/nginx restart