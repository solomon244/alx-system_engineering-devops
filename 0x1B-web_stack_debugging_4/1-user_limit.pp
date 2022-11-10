#configuration so that it is possible to login with the holberton user and open # a file without any error message.

file { 'login':
    ensure  => present,
    path    => '/etc/security/limits.conf',
    content => '#File erased'
}
