packer {
  required_plugins {
    qemu = {
      version = ">= 1.1.0"
      source  = "github.com/hashicorp/qemu"
    }
  }
}

variable "iso_url" {
  type    = string
  default = "https://download.fedoraproject.org/pub/fedora/linux/releases/41/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-41-1.4.iso"
}

variable "iso_checksum" {
  type    = string
  default = "sha256:0d1d2360b3886b77fd5103c20058b76e9389f414e66d49811804f5e08219ee2d"
}

source "qemu" "fedora" {
  iso_url          = var.iso_url
  iso_checksum     = var.iso_checksum
  output_directory = "build"
  shutdown_command = "echo 'student' | sudo -S shutdown -P now"
  disk_size        = "20G"
  format           = "qcow2"
  accelerator      = "kvm"
  http_directory   = "http"
  ssh_username     = "student"
  ssh_password     = "student"
  ssh_timeout      = "20m"
  vm_name          = "txwes-fedora-41"
  net_device       = "virtio-net"
  disk_interface   = "virtio"
  boot_wait        = "10s"
  boot_command     = [
    "<tab><wait>",
    " inst.ks=http://{{ .HTTPIP }}:{{ .HTTPPort }}/ks.cfg<enter>"
  ]
}

build {
  sources = ["source.qemu.fedora"]

  provisioner "file" {
    source      = "training/"
    destination = "/home/student/Training"
  }

  provisioner "shell" {
    script = "http/setup-branding.sh"
  }

  provisioner "shell" {
    script = "training/txwes-submit.sh"
  }
}
