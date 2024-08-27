from playwright.sync_api import sync_playwright
import os

# Retrieve email and password from environment variables
google_email = os.getenv('GOOGLE_EMAIL')
google_password = os.getenv('GOOGLE_PASSWORD')
dashboard_url = os.getenv('DASHBOARD_URL',"https://dashboard.arcana.network")

if not google_email or not google_password:
    raise EnvironmentError("Environment variables GOOGLE_EMAIL and GOOGLE_PASSWORD must be set")

# Path to Google Chrome executable
chrome_executable_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Launch the browser and context
with sync_playwright() as p:

    # Launch Google Chrome with the specified executable path
    #browser = p.chromium.launch(
    #    executable_path=chrome_executable_path,  # Use Google Chrome instead of default Chromium
    #    headless=False  # Set to True to run in headless mode
    #)

    options = {
        'args': [
            '--disable-gpu',
            '--disable-dev-shm-usage',
            '--disable-setuid-sandbox',
            '--no-first-run',
            '--no-sandbox',
            '--no-zygote',
            '--ignore-certificate-errors',
            '--disable-extensions',
            '--disable-infobars',
            '--disable-notifications',
            '--disable-popup-blocking',
            '--disable-blink-features=AutomationControlled',
            '--remote-debugging-port=9222'
        ],
        'executable_path': chrome_executable_path,
        'headless': False  # Set headless option here
    }

    browser = p.chromium.launch(**options);
    
    context = browser.new_context(viewport={ 'width': 1440, 'height': 900 },device_scale_factor=3)
    page = context.new_page()

    # Navigate to the website's login page
    page.goto(dashboard_url)
   
    page.screenshot(path="landing_page.png")
 
    page.wait_for_timeout(3000);

    # Click on the "Sign in with Google" button
    page.click('button:has-text("Google")')

    # Wait for the Google login popup to appear and switch to it
    google_popup = page.wait_for_event('popup')
    
    page.wait_for_timeout(3000);

    # Interact with Google login popup
    with google_popup:

        page.wait_for_timeout(3000);

        # Enter email or phone
        google_popup.fill('input[type="email"]', google_email)  # Replace with your email
        page.wait_for_timeout(3000);

        google_popup.click('button:has-text("Next")')  # Click 'Next' button

        # Wait for the password input to be visible
        google_popup.wait_for_selector('input[type="password"]', state='visible')
        
        page.wait_for_timeout(2000);

        # Enter password
        google_popup.fill('input[type="password"]', google_password)  # Replace with your password
        google_popup.click('button:has-text("Next")')  # Click 'Next' button

        # Wait for continue to show up
        google_popup.wait_for_selector('button:has-text("Continue")', state='visible')
        google_popup.click('button:has-text("Continue")')  # Click 'Continue' button
        
        page.wait_for_timeout(10000);

        page.screenshot(path='full_page.png', full_page=True)
        card_locator = page.locator("section.card:has(h3:text-is('Create New App'))")
        card_locator.hover()
        card_locator.screenshot(path="create_new_card.png")

        # Optionally handle 2FA if enabled
        # Uncomment the following lines if 2FA is enabled
        # google_popup.wait_for_selector('input[type="tel"]', {'state': 'visible'})
        # google_popup.fill('input[type="tel"]', 'your-2fa-code')  # Replace with your 2FA code
        # google_popup.click('button[jsname="LgbsSe"]')  # Click 'Next' button for 2FA

        # Close the Google login popup
        #google_popup.close()

        # Back on the original page after successful login

    print('Done!!!')

    # The browser context is automatically closed here

