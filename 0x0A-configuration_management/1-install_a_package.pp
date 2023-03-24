# install puppet-lint -v 2.1.0

#exec { 'puppet-lint':
#  command => '/usr/bin/apt-get -y install puppet-lint -v 2.1.0',
#}


# installing a package using puppet
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}