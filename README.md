# Ryan's Perfume ✦ Luxury Fragrance Purchasing Frontend

A responsive luxury e-commerce frontend for **Ryan's Perfume**, developed with **HTML5**, **CSS3**, **JavaScript**, and **AngularJS (1.8.2)** following the exact software architecture demonstrated in the reference project.

---

## 🌟 Overview & Highlights

- **Brand:** Ryan's Perfume (*Haute Parfumerie & Artisanal Scents*)
- **Theme:** Luxury Obsidian & Champagne Gold (`#0e0f12`, `#16181f`, `#cfa859`)
- **Key Modules:**
  - 🏠 **Hero Banner:** Brand story and call-to-action button.
  - 🔍 **Live Search Filter:** Dynamic filtering by perfume name, fragrance family, or scent notes (oud, amber, rose, vanilla, bergamot, etc.).
  - 🛍️ **Interactive Shopping Bag (Cart):** Real-time item additions, item removals, and automatic total price calculation (`Rs. {{total()}}`).
  - 💎 **Curated Specials & Bundles:** Discovery coffrets and limited edition collector flacons.
  - 📜 **About Section:** Brand legacy and perfume maceration philosophy.
  - ✉️ **Concierge Contact Form:** Client name, email, and inquiry with immediate feedback message.
  - 📱 **Mobile Responsive:** Adapts cleanly across mobile, tablet, and desktop screens.

---

## 🚀 How to Run

### Method 1: Direct Browser Launch (Easiest)
Simply double-click the **`index.html`** file in your file explorer, or right-click and choose **Open With > Google Chrome / Microsoft Edge / Firefox**.
Because it uses CDN links for fonts and AngularJS, it runs instantly with no local web server required.

### Method 2: Local HTTP Server (Optional)
If you prefer running through a local development server:

Using Python:
```bash
python -m http.server 8000
```
Then open `http://localhost:8000` in your browser.

Using Node.js:
```bash
npx serve .
```

---

## 📂 File Architecture

| File | Description |
|---|---|
| [**`index.html`**](file:///c:/Users/Danish%20Basha/Desktop/ryan_perfume/index.html) | Standalone complete frontend with embedded styling and AngularJS controller. |
| [**`style.css`**](file:///c:/Users/Danish%20Basha/Desktop/ryan_perfume/style.css) | Modular stylesheet containing the full luxury color palette and responsive rules. |
| [**`app.js`**](file:///c:/Users/Danish%20Basha/Desktop/ryan_perfume/app.js) | Modular AngularJS controller managing product catalog, cart, and events. |
| [**`PROJECT_REPORT.md`**](file:///c:/Users/Danish%20Basha/Desktop/ryan_perfume/PROJECT_REPORT.md) | Full academic project report (Objectives, Architecture, Working Principle, Advantages, etc.). |

---

## 🛠️ Technology Stack
- **HTML5:** Semantic markup (`header`, `nav`, `main`, `section`, `article`, `form`, `footer`)
- **CSS3:** Flexbox, CSS Grid, custom properties, animations, media queries
- **JavaScript (ES6):** Core application logic
- **AngularJS 1.8.2:** Two-way data binding, scope controllers, filters, and directives (`ng-app`, `ng-controller`, `ng-repeat`, `ng-model`, `ng-click`, `ng-submit`)
