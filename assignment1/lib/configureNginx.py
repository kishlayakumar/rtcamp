server {
        listen       80 default_server;
        listen       [::]:80 default_server;
        server_name  52.38.20.156;
        root         /usr/share/nginx/html/wordpress;
        index index.php index.html index.htm;
        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;

        #location / {
        #}

        #error_page 404 ../404.html;
        #    location = ../40x.html {
        #}

        #error_page 500 502 503 504 /50x.html;
        #    location = ../50x.html {
        #}
    location ~ \.php$ {
        try_files $uri =404;
        fastcgi_pass unix:/var/run/php-fpm/php-fpm.sock;
        fastcgi_index index.php;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include fastcgi_params;
    }
    }

