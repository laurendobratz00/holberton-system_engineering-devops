# This script is creating a file in /tmp using Puppet
file {'/tmp/holberton':
  mode    => '0744',
  owner   => www-data,
  group   => www-data,
  content => 'I love Puppet',
}