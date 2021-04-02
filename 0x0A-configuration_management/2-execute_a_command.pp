# kills a process with exec
exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => '/usr/bin/'
}