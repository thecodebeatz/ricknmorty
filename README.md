# Automate Website Monitoring with AWS Lambda and Python

This repository contains Python code to automate website monitoring using **AWS Lambda** and **Telegram notifications**. It allows you to automatically check websites for changes (e.g., appointment availability) and send real-time alerts when specific conditions are met.

## How It Works

This project uses an AWS Lambda function to monitor websites for specific conditions (e.g., available appointment slots) and notify you via Telegram when changes occur. It works by:

1. Scraping or monitoring websites for updates.
2. Running the Lambda function at regular intervals (e.g., every 15 minutes) using **AWS EventBridge**.
3. Sending notifications via **Telegram** when conditions are met.