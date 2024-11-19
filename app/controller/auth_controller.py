from flask import Blueprint, render_template, redirect, request, flash, url_for

auth_bluprint = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bluprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Formdan gelen veriyi al
        username = request.form.get('username')
        password = request.form.get('password')

        # Örnek kontrol (gerçek uygulamalarda veritabanı kontrolü yapılır)
        if username == "admin" and password == "1234":
            flash("Giriş başarılı!", "success")
            return redirect(url_for('app_page'))  # Giriş başarılıysa yönlendirme
        else:
            flash("Kullanıcı adı veya şifre hatalı!", "danger")

    # GET isteği için login sayfasını göster
    return render_template('auth/login.html')

@auth_bluprint.route("/register")
def register():
    return render_template("auth/register.html")