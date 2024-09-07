


# views.py
import os
import requests
from django.shortcuts import redirect, render
from django.conf import settings

# Redirect to Salesforce for OAuth login
def salesforce_login(request):
    salesforce_login_url = (
        f"{settings.SALESFORCE_AUTH_URL}?"
        f"response_type=code&client_id={settings.SALESFORCE_CLIENT_ID}"
        f"&redirect_uri={settings.SALESFORCE_REDIRECT_URI}"
    )
    return redirect(salesforce_login_url)

# Handle Salesforce callback after OAuth login
def salesforce_callback(request):
    code = request.GET.get('code')
    if code:
        token_url = settings.SALESFORCE_TOKEN_URL
        response = requests.post(token_url, data={
            'grant_type': 'authorization_code',
            'client_id': settings.SALESFORCE_CLIENT_ID,
            'client_secret': settings.SALESFORCE_CLIENT_SECRET,
            'redirect_uri': settings.SALESFORCE_REDIRECT_URI,
            'code': code
        })

        if response.status_code == 200:
            token_data = response.json()
            request.session['access_token'] = token_data['access_token']
            request.session['instance_url'] = token_data['instance_url']
            return redirect('salesforce_query')  # Go to query page after successful login
        else:
            return render(request, 'error.html', {'error': 'Failed to get token'})
    else:
        return render(request, 'error.html', {'error': 'No code returned'})

# Perform a Salesforce query after authentication
def salesforce_query(request):
    access_token = request.session.get('access_token')
    instance_url = request.session.get('instance_url')

    if access_token and instance_url:
        query = "SELECT Id, Name FROM Account LIMIT 10"  # Example SOQL query
        headers = {'Authorization': f'Bearer {access_token}'}
        api_url = f"{instance_url}/services/data/v56.0/query"
        response = requests.get(api_url, headers=headers, params={'q': query})

        if response.status_code == 200:
            data = response.json()
            return render(request, 'salesforce_data.html', {'data': data['records']})
        else:
            return render(request, 'error.html', {'error': 'Failed to query Salesforce'})
    else:
        return redirect('salesforce_login')
