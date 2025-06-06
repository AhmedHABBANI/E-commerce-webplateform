from app import app, db
from app.models import Product
from app.models import User

# Ouvre un contexte d'application Flask
with app.app_context():
    db.create_all()
    
    products = [
        Product(name="T-shirt blanc", price=129.00, image="tshirt.jpg", description="T-shirt en coton bio", category="Vêtements", stock=25),
        Product(
            name="Stitch", 
            price=59.99, 
            image="stitch_plush.jpg", 
            description="Peluche douce et câline de Stitch (Lilo et Stitch), 40 cm de hauteur, matière hypoallergénique.",
            category="Jouets", 
            stock=25
        ),
        Product(name="Casquette noire", price=89.00, image="cap.jpg", description="Casquette ajustable", category="Accessoires", stock=40),
        Product(name="Montre en cuir", price=899.00, image="watch.jpg", description="Montre élégante", category="Accessoires", stock=8),
        Product(name="Chaussures de sport", price=499.00, image="shoes.jpg", description="Chaussures confortables", category="Chaussures", stock=12),
        Product(
    name="Sac à dos noir", 
    price=199.00, 
    image="backpack.jpg", 
    description="Sac à dos résistant avec compartiment pour ordinateur portable, 20L", 
    category="Accessoires", 
    stock=30
),
Product(
    name="Mug personnalisé", 
    price=39.90, 
    image="mug.jpg", 
    description="Mug en céramique de haute qualité, personnalisable avec texte ou image", 
    category="Maison", 
    stock=50
),
Product(
    name="Écouteurs sans fil", 
    price=349.00, 
    image="earbuds.jpg", 
    description="Écouteurs Bluetooth avec réduction de bruit active et autonomie de 20h", 
    category="Électronique", 
    stock=15
),
Product(
    name="Livre 'Le Petit Prince'", 
    price=24.99, 
    image="petit_prince.jpg", 
    description="Édition collector du classique de Saint-Exupéry avec illustrations originales", 
    category="Livres", 
    stock=60
),
Product(
    name="Bougie parfumée vanille", 
    price=45.00, 
    image="candle.jpg", 
    description="Bougie artisanale à la vanille, durée de combustion 40h", 
    category="Décoration", 
    stock=35
),
Product(
    name="Ballon de football", 
    price=129.00, 
    image="soccer_ball.jpg", 
    description="Ballon officiel taille 5, résistant et adapté pour terrains extérieurs", 
    category="Sports", 
    stock=20
),
Product(
    name="Tapis de yoga", 
    price=79.99, 
    image="yoga_mat.jpg", 
    description="Tapis antidérapant et écologique, épaisseur 5mm", 
    category="Fitness", 
    stock=18
),
Product(
    name="Pantalon jogger gris", 
    price=149.99, 
    image="jogger.jpg", 
    description="Pantalon décontracté en coton extensible, taille ajustable", 
    category="Vêtements", 
    stock=22
),
Product(
    name="Peluche Pikachu", 
    price=49.99, 
    image="pikachu_plush.jpg", 
    description="Peluche officielle Pokémon, 35 cm, douce et lavable", 
    category="Jouets", 
    stock=30
),
Product(
    name="Écharpe en laine", 
    price=79.00, 
    image="scarf.jpg", 
    description="Écharpe hiver en laine mérinos, uni noir", 
    category="Accessoires", 
    stock=40
),
Product(
    name="Baskets vintage", 
    price=599.00, 
    image="sneakers.jpg", 
    description="Baskets rétro style années 90, semelle confortable", 
    category="Chaussures", 
    stock=10
),
Product(
    name="Coussin décoratif", 
    price=35.50, 
    image="cushion.jpg", 
    description="Coussin velours, motif géométrique, 40x40 cm", 
    category="Maison", 
    stock=45
),
Product(
    name="Chargeur sans fil", 
    price=129.00, 
    image="wireless_charger.jpg", 
    description="Chargeur Qi compatible iPhone et Android, 15W", 
    category="Électronique", 
    stock=25
),
Product(
    name="Harry Potter à l'école des sorciers", 
    price=29.90, 
    image="harry_potter.jpg", 
    description="Édition illustrée du premier tome de la saga Harry Potter", 
    category="Livres", 
    stock=50
),
Product(
    name="Tableau abstrait", 
    price=199.00, 
    image="painting.jpg", 
    description="Tableau moderne, toile imprimée haute qualité, 60x90 cm", 
    category="Décoration", 
    stock=8
),
Product(
    name="Raquette de tennis", 
    price=899.00, 
    image="tennis_racket.jpg", 
    description="Raquette professionnelle, poids léger, grip ergonomique", 
    category="Sports", 
    stock=12
),
Product(
    name="Haltères ajustables", 
    price=199.99, 
    image="dumbbells.jpg", 
    description="Set de 2 haltères (2kg à 10kg réglables)", 
    category="Fitness", 
    stock=20
)
    ]


    db.session.add_all(products)
    db.session.commit()
    print("Base de données initialisée avec succès.")
