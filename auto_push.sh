#!/bin/bash

# Commit message
message="Auto commit triggered by file change"

# Add all changes
git add .

# Commit changes with a message
git commit -m "$message"

# Push changes to remote
git push origin main

new line