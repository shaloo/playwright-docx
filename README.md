# playwright-docx
Uses playwright to take ss automatically for docs use

## Usage

1. Set up environment variables:  GOOGLE_EMAIL and GOOGLE_PASSWORD
2. Optional: Set up DASHBOARD_URL, default is https://dashboard.arcana.network
3. Make sure you have chrome installed on your system. Log into chrome using the same Google email and password and check it works. Do not use a different login id to stay logged into chrome. Sometimes Google security tries to not show password field once you provide login id and that may cause the auto screenshot login of manage apps page / other page post login to fail.
4. Make sure you have Python >= 3.9 installed
5. Run `python google-login.py` to take screenshots of the following pages:

A) Dashboard landing page
B) Manage Apps page post successful login
C) Create new app card on the Manage Apps screen
