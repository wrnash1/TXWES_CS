#!/bin/bash
# harden_ssh.sh - Reference script for Lab 3

echo "Harden SSH Configuration..."

# 1. Disable Root Login
# sudo sed -i 's/#PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config

# 2. Change Default Port (Optional)
# sudo sed -i 's/#Port 22/Port 2222/' /etc/ssh/sshd_config

# 3. Enable Public Key Auth Only
# sudo sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config

# 4. Restart service
# sudo systemctl restart sshd

echo "SSH Hardening Plan generated. Edit this script and uncomment lines to apply."
