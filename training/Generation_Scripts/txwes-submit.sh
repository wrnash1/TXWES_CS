#!/bin/bash
# txwes-submit.sh - Student submission script

LOG_FILE="/var/log/txwes_labs.log"
EMAIL_RECIPIENT="nash@txwes.edu"

# Ensure log file exists and is writable, otherwise fall back to user's home directory
if [ ! -f "$LOG_FILE" ]; then
    if ! touch "$LOG_FILE" 2>/dev/null; then
        LOG_FILE="$HOME/.txwes_labs.log"
        touch "$LOG_FILE"
    else
        chmod 666 "$LOG_FILE" 2>/dev/null
    fi
elif [ ! -w "$LOG_FILE" ]; then
    LOG_FILE="$HOME/.txwes_labs.log"
    touch "$LOG_FILE"
fi

STUDENT_NAME=$1
LAB_ID=$2

if [ -z "$STUDENT_NAME" ] || [ -z "$LAB_ID" ]; then
    read -p "Enter your full name: " STUDENT_NAME
    read -p "Enter Course/Lab ID (e.g., CIS-3325-Lab1): " LAB_ID
fi

TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
ENTRY="[$TIMESTAMP] Student: $STUDENT_NAME | Lab: $LAB_ID"

echo "$ENTRY" >> "$LOG_FILE"
echo "Submission logged locally."

if command -v msmtp > /dev/null; then
    echo -e "Subject: TXWES_CS Lab Submission - $LAB_ID\n\n$ENTRY" | msmtp "$EMAIL_RECIPIENT"
    echo "Submission emailed to $EMAIL_RECIPIENT."
fi

CRON_JOB="0 16 * * 5 mail -s 'Weekly TXWES_CS Lab Logs' $EMAIL_RECIPIENT < $LOG_FILE"
(crontab -l 2>/dev/null; echo "$CRON_JOB") | sort -u | crontab -
