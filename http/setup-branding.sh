#!/bin/bash

# setup-branding.sh
# Customizes the Fedora environment for Texas Wesleyan University.

# Set hostname
hostnamectl set-hostname txwes-fedora

# Placeholder for wallpaper setting (GNOME specific)
# sudo -u student dbus-launch gsettings set org.gnome.desktop.background picture-uri 'file:///usr/share/backgrounds/txwes-wallpaper.jpg'

echo "Branding setup complete."
