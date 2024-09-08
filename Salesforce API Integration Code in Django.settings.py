

# settings.py

SALESFORCE_CLIENT_ID = 'your_salesforce_client_id'
SALESFORCE_CLIENT_SECRET = 'your_salesforce_client_secret'
SALESFORCE_REDIRECT_URI = 'http://localhost:8000/salesforce/callback/'  # This should match your Salesforce app settings
SALESFORCE_AUTH_URL = 'https://login.salesforce.com/services/oauth2/authorize'
SALESFORCE_TOKEN_URL = 'https://login.salesforce.com/services/oauth2/token'
SALESFORCE_API_BASE_URL = 'https://your_instance.salesforce.com'


#or


import os
import logging

# Salesforce OAuth2 Configuration
SALESFORCE_CLIENT_ID = os.getenv('SALESFORCE_CLIENT_ID', 'your_salesforce_client_id')
SALESFORCE_CLIENT_SECRET = os.getenv('SALESFORCE_CLIENT_SECRET', 'your_salesforce_client_secret')
SALESFORCE_REDIRECT_URI = os.getenv('SALESFORCE_REDIRECT_URI', 'http://localhost:8000/salesforce/callback/')
SALESFORCE_AUTH_URL = os.getenv('SALESFORCE_AUTH_URL', 'https://login.salesforce.com/services/oauth2/authorize')
SALESFORCE_TOKEN_URL = os.getenv('SALESFORCE_TOKEN_URL', 'https://login.salesforce.com/services/oauth2/token')
SALESFORCE_API_BASE_URL = os.getenv('SALESFORCE_API_BASE_URL', 'https://your_instance.salesforce.com')

# Additional configuration
SALESFORCE_API_VERSION = os.getenv('SALESFORCE_API_VERSION', 'v54.0')  # Default API version
SALESFORCE_SCOPES = os.getenv('SALESFORCE_SCOPES', 'full refresh_token offline_access')  # OAuth scopes

# Timeout settings for Salesforce API requests (in seconds)
SALESFORCE_API_TIMEOUT = int(os.getenv('SALESFORCE_API_TIMEOUT', 30))  # Default timeout of 30 seconds

# Retry configuration in case of failed requests
SALESFORCE_API_MAX_RETRIES = int(os.getenv('SALESFORCE_API_MAX_RETRIES', 3))  # Default 3 retries for failed requests

# Enable logging for Salesforce API calls
SALESFORCE_API_LOGGING_ENABLED = os.getenv('SALESFORCE_API_LOGGING_ENABLED', 'True') == 'True'

# Salesforce Token Expiry Handling
SALESFORCE_TOKEN_EXPIRY_BUFFER = int(os.getenv('SALESFORCE_TOKEN_EXPIRY_BUFFER', 300))  # Buffer in seconds to refresh tokens before expiry

# Logger setup
if SALESFORCE_API_LOGGING_ENABLED:
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info("Salesforce API logging is enabled.")

# Example usage of logging
def log_api_request(request_type, url):
    if SALESFORCE_API_LOGGING_ENABLED:
        logger.info(f"Making {request_type} request to {url}")

# Function to refresh token (example)
def refresh_salesforce_token():
    # Logic to refresh Salesforce token
    logger.info("Refreshing Salesforce token...")
    # Add actual refresh logic here...

