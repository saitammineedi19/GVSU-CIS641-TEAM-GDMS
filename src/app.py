from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask import jsonify
import sqlite3
import hashlib

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def get_db():
    try:
        db = sqlite3.connect('users.db')
        return db
    except sqlite3.Error as e:
        print("Database connection error:", e)
        return None

# Function to create the 'users' table
def create_users_table():
    connection = get_db()
    if connection:
        cursor = connection.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT
            )
        ''')
        
        connection.commit()
        connection.close()
    else:
        print("Failed to establish a database connection.")

# Call the function to create the 'users' table
create_users_table()

# Function to create a user
def create_user(username, password):
    db = get_db()
    if db:
        try:
            cursor = db.cursor()
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            db.commit()
            db.close()
            print("User created successfully.")
        except sqlite3.Error as e:
            print("Error creating user:", e)
    else:
        print("Failed to establish a database connection.")

def user_exists(username):
    db = get_db()
    if db:
        try:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
            user = cursor.fetchone()
            db.close()
            return user is not None
        except sqlite3.Error as e:
            print("Error executing SQL query:", e)
            return False
    else:
        print("Failed to establish a database connection.")
        return False

def authenticate_user(username, password):
    db = get_db()
    if db:
        try:
            cursor = db.cursor()
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hashed_password))
            user = cursor.fetchone()
            db.close()
            return user
        except sqlite3.Error as e:
            print("Error executing SQL query:", e)
            return None
    else:
        print("Failed to establish a database connection.")
        return None


# Routes for signup, signin, and home pages
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']  # This is the line where the 'password' variable is obtained from the form
        if user_exists(username):
            flash('Username already exists. Please choose a different username.', 'error')
        else:
            create_user(username, password)
            flash('Account created successfully!', 'success')
            return redirect(url_for('signin'))
    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user=authenticate_user(username,password)

        if user:
            session['username'] = username
            flash('Logged in successfully!', 'success')
            return redirect(url_for('inventory'))
        else:
            flash('Invalid username or password. Please try again.', 'error')

    return render_template('signin.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logged out successfully!', 'success')
    return redirect(url_for('home'))


# Function to create the database and table
def create_table():
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    quantity INTEGER,
                    price REAL,
                    location TEXT
                )''')
    conn.commit()
    conn.close()

create_table()

# Route to display all inventory items
@app.route('/index', methods=['GET', 'POST'])
def inventory():
    #if 'username' in session:
        page = request.args.get('page', 1, type=int)  # Get the page number from query parameters
        per_page = 5 # Number of items to display per page

        conn = sqlite3.connect('inventory.db')
        c = conn.cursor()

        # Retrieve items for the current page
        c.execute('SELECT * FROM items LIMIT ? OFFSET ?', (per_page, (page - 1) * per_page))
        items = c.fetchall()

        # Count total number of items
        c.execute('SELECT COUNT(*) FROM items')
        total_items = c.fetchone()[0]

        conn.close()

        total_pages = (total_items + per_page - 1) // per_page  # Calculate total pages

        return render_template('index.html', items=items, total_pages=total_pages, current_page=page)
   # else:
        #return redirect(url_for('signin'))

# Route to add new item to inventory
@app.route('/add_item', methods=['GET'])
def display_add_item():
    return render_template('add_item.html')

@app.route('/add_item', methods=['POST'])
def add_item():
    if request.method == 'POST':
        name = request.form.get('name')
        quantity = request.form.get('quantity')
        price = request.form.get('price')
        location = request.form.get('location')

        if name:  # Check if name is not empty before insertion
            conn = sqlite3.connect('inventory.db')
            try:
                c = conn.cursor()
                # Check if the item already exists in the same location
                c.execute('SELECT id FROM items WHERE name=? AND location=?', (name, location))
                existing_item = c.fetchone()

                if existing_item:
                    conn.close()
                    return jsonify({'error':'Item already exists in the same location. Please update the item or provide a different item name.'})
                
                #insert item
                c.execute('INSERT INTO items (name, quantity, price, location) VALUES (?, ?, ?, ?)', (name, quantity, price, location))
                conn.commit()
                print("Item inserted successfully")  # Print a success message

                # Fetch updated inventory list after adding the item
                c.execute('SELECT * FROM items')
                items = c.fetchall()
                conn.close()
                return jsonify({'success':'Item added successfully'})

            except sqlite3.Error as e:
                conn.close()
                return jsonify({'error':'Error inserting item: {e}. Please try again.'})
        else:
            return jsonify({'error': 'Item name cannot be empty. Please provide a name.'})
    else:
        return jsonify({'error': 'Invalid request'})
    
@app.route('/update_item/<int:item_id>', methods=['POST'])
def update_item(item_id):
    if request.method == 'POST':
        name = request.form.get('name')
        quantity = request.form.get('quantity')
        price = request.form.get('price')
        location = request.form.get('location')

        try:
            conn = sqlite3.connect('inventory.db')
            c = conn.cursor()

            # Check if an item with the same name already exists at the same location (excluding the current item being updated)
            c.execute('SELECT id FROM items WHERE name=? AND location=? AND id != ?', (name, location, item_id))
            existing_item = c.fetchone()

            if existing_item:
                conn.close()
                return jsonify({'error': 'An item with the same name already exists at the same location. Please provide a different item name.'})

            # Update item details in the database
            c.execute('UPDATE items SET name=?, quantity=?, price=?, location=? WHERE id=?', (name, quantity, price, location, item_id))
            conn.commit()
            print(f"Item {item_id} updated successfully")
            
           # Return a JSON response indicating success
            return jsonify({'message': 'Item updated successfully'})
        except sqlite3.Error as e:
            print(f"Error updating item: {e}")
            conn.rollback()  # Rollback changes if an error occurs
            return jsonify({'error': f"Error updating item: {e}. Please try again."})
        finally:
            conn.close()

    return jsonify({'error': 'Invalid request'})

@app.route('/transfer_items', methods=['GET'])
def display_transfer_items():
    return render_template('transfer_items.html')

@app.route('/transfer_items', methods=['POST'])
def transfer_items():
    from_location = request.form.get('from_location')
    to_location = request.form.get('to_location')
    quantity = request.form.get('quantity')
    item_name=request.form.get('name')

    # Check if the item exists in both locations
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()

    c.execute('SELECT quantity FROM items WHERE name = ? AND location = ?', (item_name, from_location))
    from_location_quantity = c.fetchone()

    c.execute('SELECT quantity FROM items WHERE name = ? AND location = ?', (item_name, to_location))
    to_location_quantity = c.fetchone()

    if from_location_quantity is None or to_location_quantity is None:
        conn.close()
        error_message="Item not found in both locations"
        return jsonify({'error':error_message})

    # Check if there's enough quantity in the 'from' location
    if from_location_quantity[0] < int(quantity):
        conn.close()
        error_message="Not enough quantity in the from location"
        return jsonify({'error':error_message})
    # Perform item transfer by updating quantities in both locations
    new_from_quantity = from_location_quantity[0] - int(quantity)
    new_to_quantity = to_location_quantity[0] + int(quantity)

    c.execute('UPDATE items SET quantity = ? WHERE name = ? AND location = ?', (new_from_quantity, item_name, from_location))
    c.execute('UPDATE items SET quantity = ? WHERE name = ? AND location = ?', (new_to_quantity, item_name, to_location))

    conn.commit()
    conn.close()
    success_message= "Transfer performed successfully"

    return jsonify({'success': success_message})


if __name__ == '__main__':
    app.run(debug=True)
