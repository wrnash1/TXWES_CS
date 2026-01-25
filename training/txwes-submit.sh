#!/bin/bash

# txwes-submit.sh - Student submission script
# Logs student name and lab ID, then emails it.

LOG_FILE="/var/log/txwes_labs.log"
EMAIL_RECIPIENT="nash@txwes.edu"

# Ensure log file exists and is writable
touch "$LOG_FILE"
chmod 666 "$LOG_FILE"

# Prompt for info if not provided via arguments
STUDENT_NAME=$1
LAB_ID=$2

if [ -z "$STUDENT_NAME" ] || [ -z "$LAB_ID" ]; then
    read -p "Enter your full name: " STUDENT_NAME
    read -p "Enter Lab ID: " LAB_ID
fi

TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
ENTRY="[$TIMESTAMP] Student: $STUDENT_NAME | Lab: $LAB_ID"

echo "$ENTRY" >> "$LOG_FILE"
echo "Submission logged locally."

# Attempt to email via msmtp
if command -v msmtp > /dev/null; then
    echo -e "Subject: TXWES Lab Submission - $LAB_ID\n\n$ENTRY" | msmtp "$EMAIL_RECIPIENT"
    echo "Submission emailed to $EMAIL_RECIPIENT."
else
    echo "Warning: msmtp not found. Email not sent."
fi

# Setup Cron Job (emails the full log every Friday at 4 PM)
CRON_JOB="0 16 * * 5 mail -s 'Weekly TXWES Lab Logs' $EMAIL_RECIPIENT < $LOG_FILE"
(crontab -l 2>/dev/null; echo "$CRON_JOB") | sort -u | crontab -
echo "Weekly cron job ensured at Friday 4 PM."
