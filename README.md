# 🪙 Crypto Store - Buy Cryptocurrency & Explore Services

Crypto Store is a Django-based web application that allows users to **buy cryptocurrencies** securely and **explore a variety of crypto-related services**. It's designed to be simple, intuitive, and informative for both beginners and experienced traders.

---

## 🌟 Features

- 💸 **Buy Crypto Easily**  
  Purchase popular cryptocurrencies like Bitcoin, Ethereum, and more using a simple, user-friendly interface.

- 📊 **Live Price Tracking**  
  Real-time crypto market prices and changes, powered by a live API.

- 🛍️ **Crypto Services Page**  
  Learn about wallet setup, investment tips, security best practices, and more.

- 👥 **User Authentication**  
  Secure login/signup system for managing user profiles and transactions.

- 🧾 **Transaction History**  
  View and manage your crypto purchases and transaction details.

- 📱 **Mobile Responsive**  
  Fully responsive design that works great on phones and tablets.

---

## 🛠️ Tech Stack

- **Backend:** Django, Python  
- **Frontend:** HTML, CSS, Bootstrap (or Tailwind)  
- **Database:** SQLite / PostgreSQL  
- **API Integration:** CoinGecko or similar for real-time data  
- **Authentication:** Django’s built-in auth system  

---

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/yourusername/crypto-store.git
cd crypto-store

# Set up virtual environment
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver
