# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant::Config.run do |config|
  config.vm.box = "project-euler"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"

  config.vm.forward_port 80, 8888
  config.vm.forward_port 22, 2222

  config.vm.share_folder "project-euler", "/srv/project-euler", "."
end
