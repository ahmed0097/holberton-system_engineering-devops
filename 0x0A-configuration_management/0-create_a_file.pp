# create a file in /tmp
file { '/tmp/school':
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0774',
    content => 'I love Puppet',
}