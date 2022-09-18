from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth # login işlemlerini kontrol etmeek için bunu kullanıyoruz
from django.contrib import messages # kullanıcıya mesaj vermek için bunu kullanıyoruz

# Create your views here.

def login(request):

    if request.method == 'POST': # Eğer talep POST değilse demek ki sayfa ilk defa çağırılıyor
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None: # kullanıcı eğer varsa sessionid kontrolü yapmamız lazım
            auth.login(request, user) # sessionid oluşturduk
            messages.add_message(request, messages.SUCCESS, 'Oturum açıldı.')
            return redirect('index')
        else:
            messages.add_message(request, messages.ERROR, 'Hatalı username ya da parola')
            return redirect('login')
    else: # sayfa ilk defa çağırılmıyorsa
        return render(request, 'user/login.html')

def register(request):
    if request.method == 'POST':

        # get form values
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password == repassword:
            # Username
            if User.objects.filter(username = username).exists():
                messages.add_message(request, messages.WARNING, 'Bu kullanıcı adı daha önce alınmış.')
                return redirect('register')
            else:
                if User.objects.filter(email = email).exists():
                    messages.add_message(request, messages.WARNING, 'Bu email adı daha önce alınmış.')
                    return redirect('register')
                else:
                    # her şey güzel
                    user = User.objects.create_user(username=username,password=password, email=email) # create_superuser deseydik admin user'ı oluşturacaktı
                    user.save()
                    messages.add_message(request, messages.SUCCESS, 'Hesabınız oluşturuldu.')
                    return redirect('login')

        else:
            print('parolalar eşleşmiyor')
            return redirect('register')
    else:
        return render(request, 'user/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.add_message(request, messages.SUCCESS, 'Oturumunuz kapatıldı.')
        return redirect('index')
