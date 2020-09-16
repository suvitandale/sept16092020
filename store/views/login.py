from django.views import View
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer

class LoginView(View):
    def get(self,request):
        if request.method == 'GET':
            return render(request, 'login.html')
    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_msg = None
        if customer:
            flag = check_password(password,customer.password)
            if flag:
                print(customer.id)
                request.session['customer_id'] = customer.id
                request.session['customer_email'] = customer.email
                return redirect('homepage')
            else:
                error_msg='Email or Password Invalid ..!!'
        else:
            error_msg = 'Customer is not Registered..!!'
        return render(request,'login.html',{'error':error_msg})
