## Introduction
In this guide, we will explore basic SSH commands that can be used in the browser-based SSH terminal for your Google Compute Engine VM instances. SSH (Secure Shell) allows you to remotely access and manage your virtual machines.

## Prerequisites
Before you begin, make sure you have:
- Created a VM instance in Google Compute Engine as described in a previous guide.

## Step-by-Step Guide

### 1. Accessing the VM via SSH in Browser
- Open a web browser and navigate to the [Google Cloud Console](https://console.cloud.google.com/).
- Sign in with your Google Cloud account credentials.
- Locate and select your VM instance from the VM instances list.
- Click the "SSH" button next to your VM instance to open the browser-based SSH terminal.

### 2. Using Basic SSH Commands

#### a. List Files and Directories (ls)
- To list files and directories in the current directory, simply use the ls command:

#### b. Check Disk Space Usage (df)
- To check disk space usage on your VM, use the df command:

#### c. Check Free Memory (free -g)
- To check available memory on your VM, use the free -g command:

#### d. Monitor System Processes (top)
- To monitor running processes and system resource usage, use the top command:

#### e. Update Package Lists (sudo apt update)
- To update the package lists for software updates, use the sudo apt update command:

#### f. Upgrade Installed Packages (sudo apt upgrade)
- To upgrade installed packages to their latest versions, use the sudo apt upgrade command:

#### g. Switch to Superuser (sudo su)
- To switch to the superuser (root) for administrative tasks, use the sudo su command:

#### h. Add a New User (adduser)
- To add a new user to your system, use the adduser command. Replace newuser with the desired username:

### 3. Exiting SSH
- To exit the SSH session, simply type exit and press Enter.

## Conclusion
Using these basic SSH commands in the browser-based SSH terminal for your VM instance allows you to perform various system administration tasks and manage your virtual machine effectively.