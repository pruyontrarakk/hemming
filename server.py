# Skyla Cui sc5146

from flask import Flask
from flask import render_template, Response, request, jsonify, url_for, redirect

app = Flask(__name__)

data = {
    "1": {
        "id": "1",
        "name": "matcha latte",
        "image": "https://cdn.loveandlemons.com/wp-content/uploads/2023/06/iced-matcha-latte-recipe.jpg",
        "flavorprofile": "A matcha latte has a grassy and vegetal taste from the matcha powder, which is balanced by the creaminess of milk. It carries umami notes with a subtle natural sweetness that enhances its complexity. Depending on the quality of matcha used, it may have a slightly bitter edge that lingers on the palate. The overall taste is smooth and earthy, making it a comforting and energizing drink.",
        "caffeinemg": "150",
        "similarcaffeineids": [3, 5, 7],
        "ingredients": ["matcha powder", "water", "milk"]
    },
    "2": {
        "id": "2",
        "name": "black coffee",
        "image": "https://somedayilllearn.com/wp-content/uploads/2020/05/cup-of-black-coffee-1536x1283.webp",
        "flavorprofile": "Black coffee has a strong and bold taste with a slightly bitter edge. The flavor varies based on the roast level, with lighter roasts being more acidic and fruity, while darker roasts have deeper chocolate and nutty undertones. Its simplicity allows the natural characteristics of the coffee beans to shine through. The absence of milk or sugar keeps its profile intense and robust, making it a go-to for coffee purists.",
        "caffeinemg": "95",
        "similarcaffeineids": [4, 6, 9],
        "ingredients": ["coffee", "water"]
    },
    "3": {
        "id": "3",
        "name": "cappuccino",
        "image": "https://www.allrecipes.com/thmb/BmpkR1pEH4WBzHgoH-oMQloHZi8=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/8624835-how-to-make-a-cappuccino-beauty-4x3-0301-13d55eaad60b42058f24369c292d4ccb.jpg",
        "flavorprofile": "Cappuccino is a well-balanced coffee drink with a strong espresso base and a creamy texture. The steamed milk adds a slight sweetness, which contrasts with the bitterness of the espresso. The frothy foam layer on top gives it a velvety mouthfeel and a lightness that enhances the drinking experience. The overall flavor is rich, smooth, and satisfying, making it a favorite among espresso lovers.",
        "caffeinemg": "150",
        "similarcaffeineids": [1, 5, 7],
        "ingredients": ["espresso", "milk", "foam"]
    },
    "4": {
        "id": "4",
        "name": "chai latte",
        "image": "https://www.evolvingtable.com/wp-content/uploads/2023/08/chai-tea-latte-19.jpg",
        "flavorprofile": "Chai latte is a warm and aromatic drink infused with bold spices like cinnamon, cardamom, and ginger. The black tea base provides a slight astringency, which is softened by the creaminess of steamed milk. It has a natural sweetness from the spices, often enhanced with honey or sugar. The blend of spicy and creamy flavors makes it a comforting and invigorating beverage.",
        "caffeinemg": "50",
        "similarcaffeineids": [2, 6, 8],
        "ingredients": ["black tea", "milk", "cinnamon", "cardamom", "ginger", "cloves"]
    },
    "5": {
        "id": "5",
        "name": "flat white",
        "image": "https://assets.bonappetit.com/photos/57d6f16acba257a52320dd7a/16:9/w_2240,c_limit/4675028010_c32a244dcf_o.jpg",
        "flavorprofile": "A flat white has a rich espresso flavor with a smooth and velvety texture. The microfoamed milk creates a creamy consistency that blends seamlessly with the coffee. It is less foamy than a cappuccino, allowing the espresso to shine while still maintaining a soft, luxurious mouthfeel. The balance of bold coffee and silky milk makes it a refined yet strong choice.",
        "caffeinemg": "150",
        "similarcaffeineids": [1, 3, 7],
        "ingredients": ["espresso", "milk"]
    },
    "6": {
        "id": "6",
        "name": "green tea",
        "image": "https://assets.epicurious.com/photos/5887d21b5f76684c78cf57db/16:9/w_2240,c_limit/green_tea_24012017.jpg",
        "flavorprofile": "Green tea has a delicate and refreshing taste with grassy and slightly sweet notes. It carries a mild astringency that varies depending on how it is brewed. Some variations may have floral or nutty undertones, adding to its complexity. The light and clean flavor make it a soothing and revitalizing beverage.",
        "caffeinemg": "30",
        "similarcaffeineids": [2, 4, 8],
        "ingredients": ["green tea leaves", "water"]
    },
    "7": {
        "id": "7",
        "name": "latte",
        "image": "https://www.cuisinart.com/dw/image/v2/ABAF_PRD/on/demandware.static/-/Sites-us-cuisinart-sfra-Library/default/dw2ca0aa66/images/recipe-Images/cafe-latte1-recipe.jpg?sw=1200&sh=1200&sm=fit",
        "flavorprofile": "A latte has a smooth and creamy taste with a mild coffee flavor. The steamed milk balances out the intensity of the espresso, making it a mellow yet rich drink. It has a slightly sweet undertone, even without added sugar, due to the natural sweetness of the milk. The silky texture and subtle espresso notes make it a comforting choice for coffee drinkers.",
        "caffeinemg": "150",
        "similarcaffeineids": [1, 3, 5],
        "ingredients": ["espresso", "milk"]
    },
    "8": {
        "id": "8",
        "name": "earl grey tea",
        "image": "https://cdnimg.webstaurantstore.com/images/products/large/69556/2245238.jpg",
        "flavorprofile": "Earl Grey tea has a bold and fragrant flavor with a distinct citrusy aroma from the bergamot oil. The black tea base provides a slightly bitter and tannic profile, balanced by the floral and fruity notes. It has a bright and refreshing taste that lingers pleasantly on the palate. The unique combination of bergamot and tea makes it a sophisticated and energizing drink.",
        "caffeinemg": "40",
        "similarcaffeineids": [4, 6, 10],
        "ingredients": ["black tea", "bergamot oil", "water"]
    },
    "9": {
        "id": "9",
        "name": "espresso",
        "image": "https://www.sharmispassions.com/wp-content/uploads/2012/07/espresso-coffee-recipe022.jpg",
        "flavorprofile": "Espresso is a concentrated coffee with a bold and intense flavor. It has deep notes of dark chocolate, caramel, and nuts, depending on the roast and origin of the beans. The crema on top adds a slight bitterness and smooth texture. Despite its strength, a well-pulled espresso is balanced and full-bodied.",
        "caffeinemg": "65",
        "similarcaffeineids": [2, 7, 10],
        "ingredients": ["coffee"]
    },
    "10": {
        "id": "10",
        "name": "honey lavender latte",
        "image": "https://www.starbucksathome.com/ca/sites/default/files/styles/recipe_ingredient/public/2021-03/Honey%20and%20Lavender%20Latte_3.jpg?itok=i25Nav_5",
        "flavorprofile": "Honey lavender latte is a floral and aromatic drink with subtle hints of sweetness. The honey adds a natural depth of flavor, balancing the slightly bitter espresso base. The lavender provides a gentle, calming aroma that enhances the smoothness of the milk. The result is a harmonious blend of sweet, creamy, and slightly earthy notes.",
        "caffeinemg": "80",
        "similarcaffeineids": [8, 9, 6],
        "ingredients": ["espresso", "milk", "honey", "lavender"]
    }
}


hem_steps = [
    {
        "title": "Introduction to Hemming",
        "images": ["1.1.png", "1.2.png"],
        "html": """
        <p><strong>What is hemming?</strong><br>
        A technique to finish the edge of fabric to prevent fraying and give a clean look.</p>
        <p><strong>When do you hem?</strong><br>
        Shortening garments, finishing handmade items, adjusting curtains, etc.</p>
        <p><strong>Why hand stitch your hem?</strong><br>
        More control, invisible finishes, great for delicate or thick fabrics.</p>
        """
    },
    {
        "title": "Tools You'll Need to Hem",
        "images": ["2.1.png"],
        "html": """
        <ul>
            <li>Needle (sharp, small-eyed)</li>
            <li>Thread (matching the fabric color)</li>
            <li>Pins or clips</li>
            <li>Scissors</li>
            <li>Measuring tape</li>
            <li>Iron (optional but recommended)</li>
        </ul>
        """
    },
    {
        "title": "Step 1: Mark your hemline with chalk or pins",
        "images": ["3.1.png"],
        "instructions": [
            "Try on the garment and make a small mark for approximate length",
            "Use chalk or pins to create a visible, removable guide",
            "Mark evenly across the full width for a straight hem",
            "Double-check that the marked hemline is level",
            "Try on the garment and check the length"
        ]
    },
    {
        "title": "Step 2: Fold up the raw edge once (¼”–½”) and press",
        "images": ["4.1.png"],
        "instructions": [
            "Fold up the raw edge by ¼–½ inch",
            "Use a measuring tape for consistency across the garment",
            "Press to set the fold and keep fabric from shifting, using an iron if needed",
            "Make sure all of the raw edge is hidden for a clean finish"
        ]
    },
    {
        "title": "Step 3: Fold again to desired hem depth and press",
        "images": ["5.1.png"],
        "instructions": [
            "Fold to the final hem depth (e.g., 1–2 inches)",
            "Match the hemline to your original markings from part 1",
            "Press firmly to crease the fold cleanly, using an iron if needed",
            "Take care to align any curves or seams"
        ]
    },
    {
        "title": "Step 4: Pin in place to secure",
        "images": ["6.1.png"],
        "instructions": [
            "Pin horizontally and evenly along the fold",
            "This step secures everything before stitching begins",
            "Now you’re ready to start sewing!"
        ]
    },

    {
        "title": "Choosing your hemming stitch type (Backstitch vs Slip stitch)",
        "images": [],
        "html": """
        <div style="display: flex; gap: 4rem;">
            <div>
                <strong>Why Backstitch</strong>
                <ul>
                    <li>Provides one of the strongest, most durable seams in hand sewing</li>
                    <li>Ideal for structural seams (e.g. garment construction, bag straps, repairs)</li>
                    <li>Cleaner and tighter, which are better for edges</li>
                    <li>Machine-like finish without using a machine</li>
                </ul>
            </div>
            <div>
                <strong>Slip stitch</strong>
                <ul>
                    <li>Nearly invisible on the outside — perfect for clean, professional-looking hems</li>
                    <li>Ideal for finishing hems on dress pants, skirts, formalwear, and curtains</li>
                    <li>Great for delicate or lightweight fabrics</li>
                    <li>Flexible and forgiving — allows the hem to move naturally without puckering</li>
                </ul>
            </div>
        </div>
        """
    },
    {
        "title": "How to Identify (Backstitch vs Slip stitch)",
        "images": ["8.1.png", "8.2.png", "8.3.png", "8.4.png"],
        "html": """
        <div style="display: flex; gap: 4rem;">
            <div>
                <strong>Backstitch</strong><br><br>
                <em>Frontside:</em><br>
                <p>A solid, continuous line of stitching that resembles machine sewing, with no gaps between stitches.</p>
                <em>Backside:</em><br>
                <p>A series of overlapping or slightly offset stitches, creating a somewhat dashed or broken line effect.</p>
            </div>
            <div>
                <strong>Slip stitch</strong><br><br>
                <em>Frontside:</em><br>
                <p>Nearly invisible, with only small, evenly spaced out stitches.</p>
                <em>Backside:</em><br>
                <p>Thread travels hidden within the hem fold, creating a long horizontal stitch line.</p>
            </div>
        </div>
        """
    }
]



@app.route('/')
def home():
   return render_template('home.html')   


@app.route('/hem')
def hem_index():
    return redirect(url_for('hem_step', step=0))

@app.route('/hem/<int:step>')
def hem_step(step):
    return render_template("hem.html", step=hem_steps[step], step_num=step,
                           prev_step=step - 1 if step > 0 else None,
                           next_step=step + 1 if step < len(hem_steps) - 1 else None)


@app.route('/backstitch')
def backstitch():
   return render_template('home.html')   

@app.route('/slipstitch')
def slipstitch():
   return render_template('home.html')   

@app.route('/quiz')
def quiz():
   return render_template('home.html')   

# @app.route('/search')
# def search():
#     ogquery = request.args.get('in', '')
#     query = ogquery.strip().lower()
    
#     matched_items = []

#     for item in data.values():
#         name_match = query in item['name'].lower()
#         flavor_match = query in item['flavorprofile'].lower()
#         ingredients_match = any(query in ing.lower() for ing in item['ingredients'])
#         caffeine_match = query == str(item['caffeinemg'])  # Match caffeine content exactly

#         if name_match or flavor_match or ingredients_match or caffeine_match:
#             matched_items.append(item)

#     return render_template('searchresults.html', results=matched_items, search_term=query, ogquery=ogquery)

# @app.route('/view/<item_id>')  # <item_id> must match the variable name in HTML
# def view_item(item_id):
#     item = data.get(item_id)  # Get item from dictionary using string key
#     if item:
#         return render_template("view.html", item=item, data=data)
#     return "Item not found", 404


# @app.route('/findpopularitems', methods=['GET'])
# def findpopularitems():
#     popularitems = list(data.values())[:3] # select first 3 items
#     return jsonify(popularitems)

# @app.route('/add', methods=['GET', 'POST'])
# def add():
#     if request.method == 'POST':
#         new_id = str(len(data) + 1)  # Generate a new unique ID
#         name = request.form.get('name', '').strip()
#         image = request.form.get('image', '').strip()
#         flavorprofile = request.form.get('flavorprofile', '').strip()
#         caffeinemg = request.form.get('caffeinemg', '').strip()
#         ingredients = request.form.get('ingredients', '').strip()

#         # Error handling
#         errors = {}
#         if not name:
#             errors['name'] = "Name is required."
#         if not image:
#             errors['image'] = "Image URL is required."
#         if not flavorprofile:
#             errors['flavorprofile'] = "Flavor profile is required."
#         if not caffeinemg.isdigit():
#             errors['caffeinemg'] = "Caffeine content is required and must be a number."
#         if not ingredients:
#             errors['ingredients'] = "Ingredients are required."

#         if errors:
#             return jsonify({'success': False, 'errors': errors})

#         # Save the new item
#         all_drinks = list(data.values())
#         all_drinks.sort(key=lambda x: abs(int(x["caffeinemg"]) - int(caffeinemg)))  # Sort by caffeine difference
#         similar_drinks = [drink["id"] for drink in all_drinks[:3]]  # Take the closest 3 drinks

#         data[new_id] = {
#             "id": new_id,
#             "name": name,
#             "image": image,
#             "flavorprofile": flavorprofile,
#             "caffeinemg": caffeinemg,
#             "ingredients": ingredients.split(", "),
#             "similarcaffeineids": similar_drinks  # Store 3 closest matches
#         }

#         return jsonify({'success': True, 'redirect': url_for('view_item', item_id=new_id)})
#     return render_template('add.html')

# @app.route('/edit/<item_id>', methods=['GET', 'POST'])
# def edit_item(item_id):
#     item = data.get(item_id)  # Retrieve existing item
    
#     if not item:
#         return "Item not found", 404

#     if request.method == 'POST':
#         # Get form data
#         name = request.form.get('name', '').strip()
#         image = request.form.get('image', '').strip()
#         flavorprofile = request.form.get('flavorprofile', '').strip()
#         caffeinemg = request.form.get('caffeinemg', '').strip()
#         ingredients = request.form.get('ingredients', '').strip()

#         # Error handling
#         errors = {}
#         if not name:
#             errors['name'] = "Name is required."
#         if not image:
#             errors['image'] = "Image URL is required."
#         if not flavorprofile:
#             errors['flavorprofile'] = "Flavor profile is required."
#         if not caffeinemg.isdigit():
#             errors['caffeinemg'] = "Caffeine content is required and must be a number."
#         if not ingredients:
#             errors['ingredients'] = "Ingredients are required."

#         if errors:
#             return jsonify({'success': False, 'errors': errors})

#         # Update the item
#         item["name"] = name
#         item["image"] = image
#         item["flavorprofile"] = flavorprofile
#         item["caffeinemg"] = int(caffeinemg)
#         item["ingredients"] = ingredients.split(", ")

#         # Update similar drinks based on caffeine content
#         all_drinks = list(data.values())
#         all_drinks.sort(key=lambda x: abs(int(x["caffeinemg"]) - int(caffeinemg)))
#         item["similarcaffeineids"] = [drink["id"] for drink in all_drinks[:3] if drink["id"] != item_id]

#         return jsonify({'success': True, 'redirect': url_for('view_item', item_id=item_id)})

#     return render_template('edit.html', item=item)


if __name__ == '__main__':
   app.run(debug = True, port=5001)