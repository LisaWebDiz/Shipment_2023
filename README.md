### Shipment Project 2023

### Description
Cargo Search Web Application
A Django-based web application for managing cargos, locations, and trucks. The application allows to import CSV data, auto-generating truck records, and managing cargo details via a user-friendly admin panel and a documented REST API.

### Quick start
```bash
git clone https://github.com/yourusername/shipment_2023.git
cd shipment_2023.git
cp example.env .env

python3 -m venv venv  
source ./venv/bin/activate  
pip install -r requirements.txt  
python manage.py makemigrations  
python manage.py migrate  
python manage.py runserver
```
Enjoy!


### Key Features
    • Upload a CSV file with location data and automatically extract specific columns into designated PostgreSQL database fields
    • Auto-generate a default database of trucks with random license plate numbers in the format 1000–9999 + random latin uppercase letter
    • Randomized current locations
    • Load default trucks using a Django fixture
    • Search for cargo by ID with a detailed view
    • Django admin panel for managing data at http://localhost:8000/admin/
    • Fully documented REST API
    • Data storage using PostgreSQL
    • Built-in pgAdmin interface for managing the database at http://localhost:5050
    • Catalogue list view and detail view for locations, trucks & cargos
    • Add / edit / delete entries — available for registered users
