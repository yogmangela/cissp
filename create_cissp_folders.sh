#!/bin/bash

# CISSP Domains with corresponding numbers
domains=(
  "Security and Risk Management"
  "Asset Security"
  "Security Architecture and Engineering"
  "Communication and Network Security"
  "Identity and Access Management-IAM"
  "Security Assessment and Testing"
  "Security Operations"
  "Software Development Security"
)

# Loop through the domains with numbers
counter=1
for domain in "${domains[@]}"; do
    # Remove spaces and replace with underscores for folder names
    folder_name=$(echo "$domain" | sed 's/ /_/g')
    # Add the number to the folder name
    folder_name="${counter}_${folder_name}"
    mkdir "$folder_name"
    echo "Created folder: $folder_name"
    # Increment the counter
    counter=$((counter + 1))
done