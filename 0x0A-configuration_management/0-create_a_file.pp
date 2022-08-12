# create a file in /tmp
file {
    '/tmp/school':
    permission => '0774', 
    owner => 'www-data',
    mode => 'wwww-data',
    content => 'I love Puppet',
}