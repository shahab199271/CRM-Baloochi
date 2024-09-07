

# settings.py

SALESFORCE_CLIENT_ID = 'your_salesforce_client_id'
SALESFORCE_CLIENT_SECRET = 'your_salesforce_client_secret'
SALESFORCE_REDIRECT_URI = 'http://localhost:8000/salesforce/callback/'  # This should match your Salesforce app settings
SALESFORCE_AUTH_URL = 'https://login.salesforce.com/services/oauth2/authorize'
SALESFORCE_TOKEN_URL = 'https://login.salesforce.com/services/oauth2/token'
SALESFORCE_API_BASE_URL = 'https://your_instance.salesforce.com'
