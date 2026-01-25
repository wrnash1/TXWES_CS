# TXWES Student VM Guide

Welcome to your Fedora 41 Workstation VM! This VM is pre-configured with all the tools you need for your courses at Texas Wesleyan University.

## Running the VM from USB

1.  **Plug in the USB drive** to your computer.
2.  **Open VirtualBox** (or VMware Player) from the USB drive.
3.  **Go to File > Import Appliance** (for .ova) or **Machine > Add** (for .vbox/.qcow2).
4.  Navigate to the `build/` folder on your USB and select the VM image.
5.  **Start the VM**.

## User Account
- **Username**: `student`
- **Password**: `student`

## Submitting Your Lab Work

To submit your lab progress, open a terminal (Ctrl+Alt+T) and run:
```bash
/home/student/Training/txwes-submit.sh
```
Follow the prompts to enter your name and Lab ID. This will log your work and notify Professor Nash.

## Important Note
Always **Save State** or **Shut Down** the VM before unplugging your USB drive to avoid data loss.
