# Increases the amount of traffic an Nginx server 
# Increase the limit of nginx

exec { 'increase nginx limit':
  command => 'sed -i "s/15/1000/" /etc/default/nginx',
  path    => '/usr/bin/:/usr/local/bin/:/bin/'
} ->

# Restart Nginx
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}

