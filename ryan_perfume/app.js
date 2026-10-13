/**
 * ==========================================================================
 * RYAN'S PERFUME - ANGULARJS APPLICATION LOGIC
 * Architecture: Model-View-Controller (AngularJS 1.8.2)
 * Module: ryanPerfumeApp
 * Controller: PerfumeController
 * ==========================================================================
 */

var app = angular.module("ryanPerfumeApp", []);

app.controller("PerfumeController", function($scope) {

    // 1. Core Signature Perfume Collection (Menu)
    $scope.menu = [
        {
            name: "Ryan's Royal Oud",
            category: "Extrait De Parfum",
            notes: "Cambodian Oud • Saffron • Warm Amber",
            description: "An opulent, aristocratic scent blending deep smoky Cambodian oud with warm spices, rare saffron, and rich resinous amber.",
            price: 2499,
            image: "https://images.unsplash.com/photo-1541643600914-78b084683601?auto=format&fit=crop&w=600&q=80"
        },
        {
            name: "Velvet Amber & Vanilla",
            category: "Eau De Parfum",
            notes: "Golden Amber • Bourbon Vanilla • Tonka Bean",
            description: "A warm and seductive oriental gourmand boasting intoxicating bourbon vanilla, roasted tonka bean, and molten golden amber.",
            price: 1899,
            image: "https://images.unsplash.com/photo-1592945403244-b3fbafd7f539?auto=format&fit=crop&w=600&q=80"
        },
        {
            name: "Noir Sauvage",
            category: "Eau De Parfum",
            notes: "Calabrian Bergamot • Sichuan Pepper • Vetiver",
            description: "A daring, nocturnal statement opening with zesty Italian bergamot, charged with crushed black pepper, and anchored by smoky Haitian vetiver.",
            price: 2199,
            image: "https://images.unsplash.com/photo-1594035910387-fea47794261f?auto=format&fit=crop&w=600&q=80"
        },
        {
            name: "Celestial Rose & Peony",
            category: "Floral Elixir",
            notes: "Grasse Rose • Fresh Peony • White Musk",
            description: "An ethereal floral melody capturing delicate Damask rose petals kissed with morning dew, pink peonies, and soft cashmere musk.",
            price: 1750,
            image: "https://images.unsplash.com/photo-1588405748880-12d1d2a59f75?auto=format&fit=crop&w=600&q=80"
        },
        {
            name: "Oceanic Drift",
            category: "Aquatic Fresh",
            notes: "Sea Salt • Sicilian Grapefruit • Driftwood",
            description: "An exhilarating blast of invigorating sea spray, chilled citrus peel, mineral salt crystals, and sun-bleached coastal driftwood.",
            price: 1599,
            image: "https://images.unsplash.com/photo-1523293182086-7651a899d37f?auto=format&fit=crop&w=600&q=80"
        },
        {
            name: "Gilded Santal",
            category: "Woody Oriental",
            notes: "Mysore Sandalwood • Cardamom • Iris",
            description: "Creamy Mysore sandalwood harmonized with crushed green cardamom pods, powdery Florentine iris root, and smooth leather.",
            price: 2299,
            image: "https://images.unsplash.com/photo-1615397349754-cfa2066a298e?auto=format&fit=crop&w=600&q=80"
        }
    ];

    // 2. Special Offers & Limited Edition Sets
    $scope.specials = [
        {
            name: "Royal Duo Gift Set (2 x 50ml)",
            notes: "Royal Oud + Velvet Amber",
            description: "Our two crown-jewel fragrances encased in a handcrafted royal velvet gift case. Perfect for day and evening wear.",
            price: 3499,
            image: "https://images.unsplash.com/photo-1547887537-6158d64c35b3?auto=format&fit=crop&w=600&q=80"
        },
        {
            name: "Artisan Discovery Coffret",
            notes: "5 x 10ml Travel Sprays",
            description: "Explore the full Ryan's Perfume universe. Includes 5 deluxe travel atomizers across our floral, woody, aquatic, and oud families.",
            price: 1299,
            image: "https://images.unsplash.com/photo-1595425970377-c9703cf48b6d?auto=format&fit=crop&w=600&q=80"
        },
        {
            name: "Midnight Seduction (Collector Flacon)",
            notes: "Smoky Birch • Saffron • Black Plum",
            description: "Ultra-concentrated limited bottling (35% perfume oil). Macerated for 8 months in French oak casks for unprecedented intensity.",
            price: 2999,
            image: "https://images.unsplash.com/photo-1508746829417-e6f548d8d6ed?auto=format&fit=crop&w=600&q=80"
        }
    ];

    // 3. State Management
    $scope.cart = [];
    $scope.message = "";
    $scope.customer = {};
    $scope.contactMessage = "";

    // 4. Cart Operations: Add
    $scope.addToCart = function(item) {
        $scope.cart.push(item);
        $scope.message = item.name + " added to your fragrance bag!";
    };

    // 5. Cart Operations: Remove
    $scope.removeFromCart = function(index) {
        var removed = $scope.cart[index];
        $scope.cart.splice(index, 1);
        $scope.message = (removed ? removed.name : "Item") + " removed from your bag.";
    };

    // 6. Dynamic Total Price Calculation
    $scope.total = function() {
        var sum = 0;
        angular.forEach($scope.cart, function(item) {
            sum += item.price;
        });
        return sum;
    };

    // 7. Order Placement (Demo Checkout)
    $scope.placeOrder = function() {
        if ($scope.cart.length === 0) {
            $scope.message = "Please add at least one fragrance to your bag first!";
        } else {
            $scope.message = "Thank you! Your order for " + $scope.cart.length + " fragrance(s) totalling Rs. " + $scope.total() + " has been placed. (Demo confirmation)";
        }
    };

    // 8. Contact Form Interaction
    $scope.sendMessage = function() {
        $scope.contactMessage = "Thank you, " + $scope.customer.name + "! Your message has been received by Ryan's Concierge team. We will reply to " + $scope.customer.email + " promptly.";
        $scope.customer = {};
    };
});
