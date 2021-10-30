from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):

    # After Submit username and password 
    if request.method == 'POST':

        # It create a form with the given information
        form = UserRegisterForm(request.POST)

        # Check the given username is not repeated and two password is same or not
        if form.is_valid():

            # To save the user data
            form.save()
            username = form.cleaned_data.get('username')

            # Display success login message
            '''
            Type of message:
            messages.debug
            messages.info
            messages.success
            messages.warning
            message.error
            ''' 
            messages.success(request, f'Your account has been created! You are now able to log in')

            # Redirect to login after register
            return redirect('login')
    else:    
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required  # This decorator will take to login page if user try to enter in profile via url
def profile(request):
    if request.method == 'POST':

         # Fill up info in form which already is there
        u_form = UserUpdateForm(request.POST, instance=request.user)

         # Fill up info in form which already is there
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            
            # Redirect to profile after updating profile
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)    
