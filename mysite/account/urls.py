from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('signup/',views.SignupView.as_view(), name='signup'),
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='change_password.html',
                                                                    success_url=reverse_lazy('home')),name='change_password'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='reset_password.html',
                                                                subject_template_name='password_reset_subject.txt',
                                                                email_template_name='password_reset_email.html',
                                                                success_url=reverse_lazy('account:password_reset_done')), name='reset_password'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset_password/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',
                                                                                        success_url=reverse_lazy('account:password_reset_complete')),
                                                                                         name='password_reset_confirm'),
    path('password_reset/complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete')
]
