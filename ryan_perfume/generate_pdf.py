import os
import subprocess
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from PIL import Image

def generate_pdf():
    pdf_filename = "Ryans_Perfume_Project_Report.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=A4)
    width, height = A4 # 595.28 x 841.89 points

    # --- Helper drawing functions ---
    def draw_heading(canv, text, x, y):
        canv.setFont("Helvetica-Bold", 12)
        canv.drawString(x, y, text)

    def draw_body(canv, text, x, y, font="Helvetica", size=10):
        canv.setFont(font, size)
        canv.drawString(x, y, text)

    # -------------------------------------------------------------
    # PAGE 1: COVER PAGE
    # -------------------------------------------------------------
    cover_img_path = "cover_perfume.jpg"
    if os.path.exists(cover_img_path):
        img_w, img_h = 240, 160
        img_x = (width - img_w) / 2
        img_y = height - 280
        c.drawImage(cover_img_path, img_x, img_y, width=img_w, height=img_h, preserveAspectRatio=True, mask='auto')

    # Brand Title
    c.setFont("Helvetica-Bold", 36)
    title_text = "RYAN'S PERFUME"
    c.drawCentredString(width / 2, height / 2 - 20, title_text)

    # Student Info at bottom left
    c.setFont("Helvetica-Bold", 11)
    info_y = 120
    line_gap = 22
    c.drawString(72, info_y + 2 * line_gap, "NAME : DANISH BASHA")
    c.drawString(72, info_y + 1 * line_gap, "RRN : 241371601008")
    c.drawString(72, info_y, "BSC COMPUTER SCIENCE ( 3RD YEAR)")

    c.showPage() # End Page 1

    # -------------------------------------------------------------
    # PAGE 2: SECTIONS 1 TO 5
    # -------------------------------------------------------------
    margin_x = 72
    curr_y = height - 72

    # 1. INTRODUCTION
    draw_heading(c, "1. INTRODUCTION", margin_x, curr_y)
    curr_y -= 18
    intro_lines = [
        "Ryan's Perfume is a responsive luxury perfume website developed using HTML5, CSS3, JavaScript, and",
        "AngularJS. It allows users to explore perfume collections, search for fragrances, add items to a",
        "shopping cart, calculate the total price, and contact the boutique concierge. The website provides an",
        "attractive and user-friendly interface."
    ]
    for line in intro_lines:
        draw_body(c, line, margin_x, curr_y)
        curr_y -= 14

    curr_y -= 10
    # 2. OBJECTIVES
    draw_heading(c, "2. OBJECTIVES", margin_x, curr_y)
    curr_y -= 18
    objectives = [
        "●  To develop an attractive luxury perfume shop website.",
        "●  To display artisanal fragrances and perfume items with prices.",
        "●  To implement fragrance search and shopping cart functionality.",
        "●  To calculate the total order amount dynamically.",
        "●  To create a contact form for customer feedback and inquiries.",
        "●  To demonstrate basic frontend development concepts."
    ]
    for obj in objectives:
        draw_body(c, obj, margin_x + 15, curr_y)
        curr_y -= 15

    curr_y -= 10
    # 3. TECHNOLOGIES USED
    draw_heading(c, "3. TECHNOLOGIES USED", margin_x, curr_y)
    curr_y -= 18
    techs = [
        ("HTML5: ", "Creates the structure of the webpage."),
        ("CSS3: ", "Provides styling, colours, layouts, animations, and responsive design."),
        ("JavaScript: ", "Implements the application's functions and logic."),
        ("AngularJS 1.8.2: ", "Provides data binding, menu filtering, event handling, and dynamic"),
        ("", "updates."),
        ("Web Browser: ", "Executes and displays the website.")
    ]
    for prefix, desc in techs:
        if prefix:
            c.setFont("Helvetica-Bold", 10)
            c.drawString(margin_x, curr_y, prefix)
            p_len = c.stringWidth(prefix, "Helvetica-Bold", 10)
            c.setFont("Helvetica", 10)
            c.drawString(margin_x + p_len, curr_y, desc)
        else:
            c.setFont("Helvetica", 10)
            c.drawString(margin_x, curr_y, desc)
        curr_y -= 15

    curr_y -= 10
    # 4. KEY FEATURES
    draw_heading(c, "4. KEY FEATURES", margin_x, curr_y)
    curr_y -= 18
    features = [
        ("Home Page: ", "Displays the perfume brand name, welcome message, and navigation links."),
        ("Menu Section: ", "Displays Royal Oud, Velvet Amber, Noir Sauvage, and Rose scents with descriptions and prices."),
        ("Search Function: ", "Helps users find perfumes and scent notes using the search box."),
        ("Shopping Cart: ", "Allows users to add and remove items and view the selected products."),
        ("Price Calculation: ", "Automatically calculates the total cost of selected items."),
        ("Special Offers: ", "Displays promotional products and gift combo offers."),
        ("Contact Form: ", "Accepts the customer's name, email, and message."),
        ("Responsive Design: ", "Adjusts the layout for different screen sizes.")
    ]
    for prefix, desc in features:
        c.setFont("Helvetica-Bold", 10)
        c.drawString(margin_x, curr_y, prefix)
        p_len = c.stringWidth(prefix, "Helvetica-Bold", 10)
        c.setFont("Helvetica", 10)
        c.drawString(margin_x + p_len, curr_y, desc)
        curr_y -= 15

    curr_y -= 10
    # 5. APPLICATION ARCHITECTURE
    draw_heading(c, "5. APPLICATION ARCHITECTURE", margin_x, curr_y)
    curr_y -= 18
    draw_body(c, "The application consists of three main parts:", margin_x, curr_y)
    curr_y -= 16
    arch_bullets = [
        "●  HTML: Defines the webpage structure and content.",
        "●  CSS: Controls the appearance and layout.",
        "●  AngularJS: Manages perfume data, cart operations, price calculation, and form",
        "    interactions."
    ]
    for b in arch_bullets:
        draw_body(c, b, margin_x + 15, curr_y)
        curr_y -= 15

    c.showPage() # End Page 2

    # -------------------------------------------------------------
    # PAGE 3: SECTIONS 6 TO 9 + START OF SOURCE CODE
    # -------------------------------------------------------------
    curr_y = height - 72
    draw_body(c, "The ryanPerfumeApp module initializes the application, while the PerfumeController manages its", margin_x, curr_y)
    curr_y -= 14
    draw_body(c, "functionality.", margin_x, curr_y)
    curr_y -= 18

    # 6. WORKING PRINCIPLE
    draw_heading(c, "6. WORKING PRINCIPLE", margin_x, curr_y)
    curr_y -= 18
    principles = [
        "1.  The user opens the Ryan's Perfume website.",
        "2.  The user browses or searches the perfume collection.",
        "3.  The user adds products to the shopping cart.",
        "4.  The cart displays selected items and their prices.",
        "5.  The total amount is calculated automatically.",
        "6.  The user can remove items or place a demo order.",
        "7.  The user can submit a message through the contact form."
    ]
    for pr in principles:
        draw_body(c, pr, margin_x + 15, curr_y)
        curr_y -= 15

    curr_y -= 10
    # 7. ADVANTAGES
    draw_heading(c, "7. ADVANTAGES", margin_x, curr_y)
    curr_y -= 18
    advantages = [
        "●  Simple and user-friendly interface.",
        "●  Easy perfume searching by name and scent notes.",
        "●  Dynamic shopping cart and price calculation.",
        "●  Attractive luxury design with hover effects.",
        "●  Responsive layout for different devices.",
        "●  Easy to maintain and modify."
    ]
    for adv in advantages:
        draw_body(c, adv, margin_x + 15, curr_y)
        curr_y -= 15

    curr_y -= 10
    # 8. LIMITATIONS
    draw_heading(c, "8. LIMITATIONS", margin_x, curr_y)
    curr_y -= 18
    limitations = [
        "●  No backend or database connection.",
        "●  Orders are not processed in real time.",
        "●  Online payment is unavailable.",
        "●  Cart details are not permanently stored.",
        "●  Contact messages are not sent to a real email account."
    ]
    for lim in limitations:
        draw_body(c, lim, margin_x + 15, curr_y)
        curr_y -= 15

    curr_y -= 10
    # 9. FUTURE ENHANCEMENTS
    draw_heading(c, "9. FUTURE ENHANCEMENTS", margin_x, curr_y)
    curr_y -= 18
    enhancements = [
        "●  Database integration.",
        "●  Customer login and registration.",
        "●  Online payment facility.",
        "●  Real-time order tracking.",
        "●  Admin dashboard for perfume collection management.",
        "●  Customer reviews and ratings."
    ]
    for enh in enhancements:
        draw_body(c, enh, margin_x + 15, curr_y)
        curr_y -= 15

    curr_y -= 25
    # SOURCE CODE HEADING
    draw_heading(c, "SOURCE CODE", margin_x, curr_y)
    curr_y -= 20
    code_p3 = [
        "<html>",
        "<!DOCTYPE html>",
        '<html lang="en" ng-app="ryanPerfumeApp">',
        "<head>",
        '<meta charset="UTF-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
    ]
    c.setFont("Helvetica", 10)
    for code_l in code_p3:
        c.drawString(margin_x, curr_y, code_l)
        curr_y -= 16

    c.showPage() # End Page 3

    # -------------------------------------------------------------
    # PAGES 4 TO 19: SOURCE CODE
    # -------------------------------------------------------------
    code_pages = {
        4: [
            "<title>Ryan's Perfume - Luxury Fragrances</title>",
            "",
            "<!-- AngularJS -->",
            "<script",
            'src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"></script>',
            "",
            "<style>",
            "* {",
            "margin: 0;",
            "padding: 0;",
            "box-sizing: border-box;",
            "scroll-behavior: smooth;",
            "}",
            "",
            "body {",
            "font-family: Arial, sans-serif;",
            "background: #fff8ef;",
            "color: #3e2723;",
            "}",
            "",
            "header {",
            "background: #3e2723;",
            "color: white;",
            "padding: 20px 8%;",
            "display: flex;",
            "justify-content: space-between;",
            "align-items: center;",
            "flex-wrap: wrap;",
            "}",
            "",
            "header h1 {"
        ],
        5: [
            "color: #ffcc80;",
            "font-size: 30px;",
            "}",
            "",
            "nav a {",
            "color: white;",
            "text-decoration: none;",
            "margin: 10px;",
            "font-weight: bold;",
            "}",
            "",
            "nav a:hover {",
            "color: #ffcc80;",
            "}",
            "",
            ".hero {",
            "min-height: 450px;",
            "padding: 80px 20px;",
            "text-align: center;",
            "color: white;",
            "background:",
            "linear-gradient(#0007, #0007),",
            'url("https://images.unsplash.com/photo-1616949755610-8c9bbc08f138?auto=format&fit=crop&w=1600&q=80");',
            "background-size: cover;",
            "background-position: center;",
            "}",
            "",
            ".hero h2 {",
            "font-size: 48px;",
            "margin: 50px 0 15px;"
        ],
        6: [
            "}",
            "",
            ".hero p {",
            "font-size: 19px;",
            "margin-bottom: 20px;",
            "}",
            "",
            ".btn {",
            "display: inline-block;",
            "background: #ffcc80;",
            "color: #3e2723;",
            "padding: 12px 25px;",
            "border: none;",
            "border-radius: 25px;",
            "text-decoration: none;",
            "font-weight: bold;",
            "cursor: pointer;",
            "margin-top: 10px;",
            "}",
            "",
            ".btn:hover {",
            "background: #ffffff;",
            "}",
            "",
            "section {",
            "padding: 55px 8%;",
            "text-align: center;",
            "}",
            "",
            "section h2 {",
            "color: #6f4e37;"
        ],
        7: [
            "font-size: 32px;",
            "margin-bottom: 15px;",
            "}",
            "",
            ".menu {",
            "display: flex;",
            "justify-content: center;",
            "flex-wrap: wrap;",
            "gap: 25px;",
            "margin-top: 30px;",
            "}",
            "",
            ".card {",
            "background: white;",
            "width: 260px;",
            "padding: 15px;",
            "border-radius: 15px;",
            "box-shadow: 0 4px 12px #0002;",
            "transition: 0.3s;",
            "}",
            "",
            ".card:hover {",
            "transform: translateY(-8px);",
            "}",
            "",
            ".card img {",
            "width: 100%;",
            "height: 180px;",
            "object-fit: cover;",
            "border-radius: 10px;",
            "}"
        ],
        8: [
            ".card h3 {",
            "margin: 12px 0;",
            "}",
            "",
            ".card p {",
            "margin: 8px 0;",
            "}",
            "",
            ".price {",
            "color: #8b4513;",
            "font-size: 20px;",
            "font-weight: bold;",
            "}",
            "",
            "#about {",
            "background: #f2e1ce;",
            "line-height: 1.8;",
            "}",
            "",
            "#special {",
            "background: white;",
            "}",
            "",
            ".contact-box {",
            "max-width: 500px;",
            "margin: auto;",
            "background: white;",
            "padding: 25px;",
            "border-radius: 15px;",
            "box-shadow: 0 4px 12px #0002;"
        ],
        9: [
            "}",
            "",
            "input, textarea {",
            "width: 100%;",
            "padding: 12px;",
            "margin: 10px 0;",
            "border: 1px solid #c9a88a;",
            "border-radius: 8px;",
            "font-family: Arial, sans-serif;",
            "}",
            "",
            ".cart {",
            "max-width: 500px;",
            "margin: 30px auto;",
            "padding: 20px;",
            "background: #fff0d9;",
            "border-radius: 10px;",
            "}",
            "",
            ".cart li {",
            "margin: 10px;",
            "}",
            "",
            "footer {",
            "background: #3e2723;",
            "color: white;",
            "text-align: center;",
            "padding: 25px;",
            "line-height: 2;",
            "}"
        ],
        10: [
            "footer a {",
            "color: #ffcc80;",
            "text-decoration: none;",
            "}",
            "",
            "@media (max-width: 600px) {",
            "header {",
            "justify-content: center;",
            "text-align: center;",
            "}",
            "",
            "nav {",
            "margin-top: 15px;",
            "}",
            "",
            ".hero h2 {",
            "font-size: 34px;",
            "margin-top: 40px;",
            "}",
            "}",
            "</style>",
            "</head>",
            "",
            '<body ng-controller="PerfumeController">',
            "",
            "<!-- Header -->",
            "<header>",
            "<h1>Ryan's Perfume</h1>",
            "<nav>",
            '<a href="#home">Home</a>'
        ],
        11: [
            '<a href="#menu">Collection</a>',
            '<a href="#about">About</a>',
            '<a href="#special">Specials</a>',
            '<a href="#contact">Contact</a>',
            "</nav>",
            "</header>",
            "",
            "<!-- Home Section -->",
            "<main>",
            '<section class="hero" id="home">',
            "<h2>Welcome to Ryan's Perfume!</h2>",
            "<p><em>Where every scent tells a story.</em></p>",
            "<p>Fresh essences, rare perfumes, and unforgettable moments.</p>",
            '<a href="#menu" class="btn">Explore Our Collection</a>',
            "</section>",
            "",
            "<!-- Menu Section -->",
            '<section id="menu">',
            "<h2>Our Signature Collection</h2>",
            "<p>Handcrafted and bottled with elegance.</p>",
            "",
            '<input type="text"',
            'ng-model="searchText"',
            'placeholder="Search oud, vanilla, rose, amber...">',
            "",
            '<div class="menu">',
            '<article class="card"',
            'ng-repeat="item in menu | filter:searchText">',
            '<img ng-src="{{item.image}}"',
            'alt="{{item.name}}"'
        ],
        12: [
            'loading="lazy">',
            "<h3>{{item.name}}</h3>",
            "<p>{{item.description}}</p>",
            '<p class="price">Rs. {{item.price}}</p>',
            '<button class="btn" ng-click="addToCart(item)">',
            "Add to Order",
            "</button>",
            "</article>",
            "</div>",
            "",
            "<!-- Shopping Cart -->",
            '<div class="cart">',
            "<h3>Your Order</h3>",
            "<p>Items selected: {{cart.length}}</p>",
            "<ul>",
            '<li ng-repeat="item in cart track by $index">',
            "{{item.name}} - Rs. {{item.price}}",
            '<button ng-click="removeFromCart($index)">',
            "Remove",
            "</button>",
            "</li>",
            "</ul>",
            "<h3>Total: Rs. {{total()}}</h3>",
            '<button class="btn" ng-click="placeOrder()">',
            "Place Order",
            "</button>"
        ],
        13: [
            "<p>{{message}}</p>",
            "</div>",
            "</section>",
            "",
            "<!-- About Section -->",
            '<section id="about">',
            "<h2>About Ryan's Perfume</h2>",
            "<p>",
            "At Ryan's Perfume, we believe perfume is more than a scent.",
            "It is a moment of elegance and an everlasting memory to connect",
            "with people.",
            "</p>",
            "<p>",
            "From freshly extracted florals to royal aged oud,",
            "we make every bottle special.",
            "</p>",
            "<blockquote>",
            "<q>Good perfume, good mood, great memories!</q>",
            "</blockquote>",
            "</section>",
            "",
            "<!-- Special Offers -->",
            '<section id="special">',
            "<h2>Today's Specials</h2>",
            '<div class="menu">',
            '<article class="card">',
            "<img",
            'src="https://images.unsplash.com/photo-1547887537-6158d64c35b3?auto=format&fit=crop&w=600&q=80"',
            'alt="Royal Duo Gift Set">'
        ],
        14: [
            "<h3>Royal Duo Gift Set</h3>",
            "<p>Start your journey with our signature perfume pair.</p>",
            '<p class="price">Rs. 3499</p>',
            "</article>",
            '<article class="card">',
            "<img",
            'src="https://images.unsplash.com/photo-1595425970377-c9703cf48b6d?auto=format&fit=crop&w=600&q=80"',
            'alt="Discovery Coffret">',
            "<h3>Discovery Coffret</h3>",
            "<p>A sweet treat of 5 travel minis for happy moments.</p>",
            '<p class="price">Rs. 1299</p>',
            "</article>",
            '<article class="card">',
            "<img",
            'src="https://images.unsplash.com/photo-1508746829417-e6f548d8d6ed?auto=format&fit=crop&w=600&q=80"',
            'alt="Midnight Seduction">',
            "<h3>Midnight Seduction</h3>",
            "<p>Your favourite limited extrait with rich sillage.</p>",
            '<p class="price">Rs. 2999</p>',
            "</article>",
            "</div>",
            "</section>",
            "",
            "<!-- Contact Section -->",
            '<section id="contact">',
            "<h2>Contact Us</h2>",
            "<p>We would love to hear from you!</p>"
        ],
        15: [
            '<div class="contact-box">',
            '<form ng-submit="sendMessage()">',
            '<label for="name">Your Name</label>',
            '<input id="name" type="text"',
            'ng-model="customer.name"',
            'placeholder="Enter your name" required>',
            "",
            '<label for="email">Email Address</label>',
            '<input id="email" type="email"',
            'ng-model="customer.email"',
            'placeholder="Enter your email" required>',
            "",
            '<label for="feedback">Your Message</label>',
            '<textarea id="feedback"',
            'ng-model="customer.feedback"',
            'rows="4"',
            'placeholder="Write your message..."',
            "required></textarea>",
            "",
            '<button type="submit" class="btn">',
            "Send Message",
            "</button>",
            "<p>{{contactMessage}}</p>",
            "</form>",
            "</div>",
            "",
            "<address>",
            "<p>Address: Chennai, Tamil Nadu</p>",
            "<p>Phone: +91 98765 43210</p>",
            "<p>Email: hello@ryansperfume.example</p>"
        ],
        16: [
            "</address>",
            "</section>",
            "</main>",
            "",
            "<!-- Footer -->",
            "<footer>",
            "<p>&copy; 2026 Ryan's Perfume. All Rights Reserved.</p>",
            "<p>Made with love and passion.</p>",
            '<p><a href="#home">Back to Top</a></p>',
            "</footer>",
            "",
            "<!-- AngularJS Functionality -->",
            "<script>",
            'var app = angular.module("ryanPerfumeApp", []);',
            'app.controller("PerfumeController", function($scope) {',
            "$scope.menu = [",
            "{",
            'name: "Royal Oud",',
            'description: "Strong and rich woody oud.",',
            "price: 2499,",
            "image:",
            '"https://images.unsplash.com/photo-1541643600914-78b084683601?auto=format&fit=crop&w=600&q=80"',
            "},",
            "{",
            'name: "Velvet Amber",',
            'description: "Warm bourbon vanilla with amber.",',
            "price: 1899,"
        ],
        17: [
            "image:",
            '"https://images.unsplash.com/photo-1592945403244-b3fbafd7f539?auto=format&fit=crop&w=600&q=80"',
            "},",
            "{",
            'name: "Noir Sauvage",',
            'description: "Bold bergamot and spicy vetiver.",',
            "price: 2199,",
            "image:",
            '"https://images.unsplash.com/photo-1594035910387-fea47794261f?auto=format&fit=crop&w=600&q=80"',
            "},",
            "{",
            'name: "Celestial Rose",',
            'description: "Fresh Damask rose and white musk.",',
            "price: 1750,",
            "image:",
            '"https://images.unsplash.com/photo-1588405748880-12d1d2a59f75?auto=format&fit=crop&w=600&q=80"',
            "},",
            "{",
            'name: "Oceanic Drift",',
            'description: "A fresh marine and sea salt breeze.",',
            "price: 1599,",
            "image:",
            '"https://images.unsplash.com/photo-1523293182086-7651a899d37f?auto=format&fit=crop&w=600&q=80"',
            "},",
            "{",
            'name: "Gilded Santal",',
            'description: "Creamy sandalwood and green cardamom.",',
            "price: 2299,"
        ],
        18: [
            "image:",
            '"https://images.unsplash.com/photo-1615397349754-cfa2066a298e?auto=format&fit=crop&w=600&q=80"',
            "}",
            "];",
            "",
            "$scope.cart = [];",
            '$scope.message = "";',
            "$scope.customer = {};",
            "",
            "$scope.addToCart = function(item) {",
            "$scope.cart.push(item);",
            "$scope.message =",
            'item.name + " added to your order!";',
            "};",
            "",
            "$scope.removeFromCart = function(index) {",
            "$scope.cart.splice(index, 1);",
            '$scope.message = "Item removed from your order.";',
            "};",
            "",
            "$scope.total = function() {",
            "var sum = 0;",
            "angular.forEach($scope.cart, function(item) {",
            "sum += item.price;",
            "});",
            "return sum;",
            "};",
            "",
            "$scope.placeOrder = function() {"
        ],
        19: [
            "if ($scope.cart.length === 0) {",
            '$scope.message = "Please add an item first!";',
            "} else {",
            "$scope.message =",
            '"Thank you! Your demo order total is Rs. " +',
            "$scope.total() +",
            '". No real order has been sent.";',
            "}",
            "};",
            "",
            "$scope.sendMessage = function() {",
            "$scope.contactMessage =",
            '"Thank you, " + $scope.customer.name +',
            '"! Your demo message has been received.";',
            "$scope.customer = {};",
            "};",
            "",
            "});",
            "</script>",
            "",
            "</body>",
            "</html>"
        ]
    }

    for p_num in range(4, 20):
        lines = code_pages[p_num]
        curr_y = height - 72
        c.setFont("Helvetica", 10)
        for line in lines:
            c.drawString(margin_x, curr_y, line)
            curr_y -= 17
        c.showPage() # End Page p_num

    # -------------------------------------------------------------
    # PAGE 20: WEBPAGE SCREENSHOT
    # -------------------------------------------------------------
    screenshot_file = "website_screenshot.png"
    if os.path.exists(screenshot_file):
        # Open with PIL to get aspect ratio
        with Image.open(screenshot_file) as im:
            orig_w, orig_h = im.size
        
        # Calculate fit within margins
        max_w = width - 120
        max_h = height - 120
        scale = min(max_w / orig_w, max_h / orig_h)
        draw_w = orig_w * scale
        draw_h = orig_h * scale
        draw_x = (width - draw_w) / 2
        draw_y = (height - draw_h) / 2

        c.drawImage(screenshot_file, draw_x, draw_y, width=draw_w, height=draw_h, preserveAspectRatio=True)

    c.showPage() # End Page 20

    c.save()
    print(f"PDF generated successfully: {pdf_filename}")

if __name__ == "__main__":
    generate_pdf()
