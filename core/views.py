from django.shortcuts import render

# Define a view for the account page
def account_view(request):
	# Render the account template
	return render(request, 'account/account.html')