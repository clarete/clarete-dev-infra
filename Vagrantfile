Vagrant.require_version ">= 1.5.1"

Vagrant.configure("2") do |config|
  config.vm.define "default" do |c|
    c.vm.box = "roboxes/debian10"
    c.vm.provision :ansible do |ansible|
      ansible.playbook = "playbook.yml"
      ansible.limit = "all"
      ansible.verbose = "v"
      ansible.raw_arguments = ["--vault-id", "clarete@scripts/vault-client.py"]
    end
  end
end
