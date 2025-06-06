from app import app, db
from flask import session, redirect, url_for, request, render_template
from app.models import Product


from datetime import datetime

@app.route('/')
def index():
    return render_template('index.html', now=datetime.utcnow())


@app.route('/products')
def products():
    category = request.args.get('category')
    if category:
        products = Product.query.filter_by(category=category).all()
    else:
        products = Product.query.all()

    # Obtenir la liste unique des catégories pour l’affichage du filtre
    all_categories = db.session.query(Product.category).distinct().all()
    categories = [c[0] for c in all_categories]

    return render_template("products.html", products=products, categories=categories, selected_category=category)



@app.route('/cart')
def cart():
    cart_items = session.get("cart", [])
    total = sum(item["price"] * item["quantity"] for item in cart_items)
    return render_template("cart.html", cart=cart_items, total=total)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    else:
        product_id = request.form.get('product_id')
        name = request.form.get('product_name')
        price = float(request.form.get('product_price'))

    item = {"id": product_id, "name": name, "price": price, "quantity": 1}

    if "cart" not in session:
        session["cart"] = []

    # Vérifie si l'article existe déjà
    cart = session["cart"]
    for p in cart:
        if p["id"] == product_id:
            p["quantity"] += 1
            break
    else:
        cart.append(item)

    session["cart"] = cart
    return redirect(url_for('products'))
@app.route('/clear_cart', methods=['POST'])
def clear_cart():
    session.pop("cart", None)
    return redirect(url_for('cart'))

@app.route('/update_cart', methods=['POST'])
def update_cart():
    cart = session.get('cart', [])

    for item in cart:
        item_id = str(item['id'])
        quantity_key = f'quantities[{item_id}]'

        if quantity_key in request.form:
            try:
                item['quantity'] = max(1, int(request.form[quantity_key]))
            except ValueError:
                pass  # ignorer les valeurs invalides

    session['cart'] = cart
    return redirect(url_for('cart'))

#inscription 
from flask import request, redirect, url_for, render_template, flash, session
from app.models import User
from app import db

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # Vérification des champs
        if not username or not email or not password:
            flash("Tous les champs sont requis.", "danger")
            return redirect(url_for('register'))

        # Vérification unicité
        if User.query.filter_by(username=username).first():
            flash("Nom d'utilisateur déjà pris.", "danger")
            return redirect(url_for('register'))
        if User.query.filter_by(email=email).first():
            flash("Email déjà utilisé.", "danger")
            return redirect(url_for('register'))

        # Création de l'utilisateur
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        flash("Inscription réussie. Vous pouvez maintenant vous connecter.", "success")
        return redirect(url_for('login'))

    return render_template('register.html')



from flask import request, redirect, url_for, render_template, session, flash
from app.models import User

from flask import request, redirect, url_for, render_template, flash, session
from app.models import User

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()

        if not email or not password:
            flash("Veuillez remplir tous les champs.", "danger")
            return redirect(url_for('login'))

        from app.models import User
        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash("Connexion réussie.", "success")
            return redirect(url_for('index'))
        else:
            flash("Adresse e-mail ou mot de passe incorrect.", "danger")
            return redirect(url_for('login'))

    return render_template('login.html')



@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    return redirect(url_for('index'))



