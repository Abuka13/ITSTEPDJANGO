from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/success')
def success():
    return render_template('success.html')






@app.route('/buycamels', methods=['GET', "POST"])
def buy_camels():
    breed = request.form.get("breed", "").strip()
    con_camel = mysql.connector.connect(
        host='localhost',
        user='Abuka',
        password='Takanashi_13',
        database='animals'
    )
    cursor = con_camel.cursor()
    cursor.execute("""select id, breed, gender, age, weight, nature, price from camel where breed LIKE %s""", (f"%{breed}%",))
    rows = cursor.fetchall()

    _camels = []
    for record in rows:
        new_dict = {
            "id": record[0],
            "breed": record[1],
            "gender": record[2][:15:1] + "..." if len(record[2]) > 15 else record[2],
            "age": record[3],
            "weight": record[4],
            "nature": record[5],
            "price": record[6]
        }
        _camels.append(new_dict)

    cursor.close()
    con_camel.close()
    return render_template('todo_camel.html', camels=_camels, search=breed)


@app.route('/sellcamel', methods=['GET', 'POST'])
def create_camel():
    if request.method == "GET":
        return render_template('create_camel.html')
    elif request.method == "POST":

        breed = request.form['breed'].strip()
        gender = request.form['gender'].strip()
        weight = request.form['weight'].strip()
        age = request.form['age'].strip()
        nature = request.form['nature'].strip()
        price = request.form['price'].strip()
        con_camel = mysql.connector.connect(
            host='localhost',
            user='Abuka',
            password='Takanashi_13',
            database='animals'
        )
        cursor = con_camel.cursor()
        cursor.execute("INSERT INTO camel (breed, gender, age, weight,nature,price) VALUES (%s, %s,%s, %s, %s, %s);",
                               (breed, gender, age, weight, nature, price))


        con_camel.commit()
        cursor.close()
        con_camel.close()
        return redirect(url_for('buy_camels'))

@app.route("/changecamel", methods=["GET", "POST"])
def change_camel():
    if request.method == "GET":
        pk = request.args.get('pk', default=0, type=int)

        con = mysql.connector.connect(
            host='localhost',
            user='Abuka',
            password='Takanashi_13',
            database='animals'
        )
        cursor = con.cursor()

        cursor.execute(
            """SELECT id, breed, gender, age, weight, nature, price FROM camel WHERE id = %s""",
            (pk,)
        )

        raw_row = cursor.fetchone()

        if raw_row:
            new_dict = {
                "id": raw_row[0],
                "breed": raw_row[1],
                "gender": raw_row[2],
                "age": raw_row[3],
                "weight": raw_row[4],
                "nature": raw_row[5],
                "price": raw_row[6]
            }

            cursor.close()
            con.close()

            return render_template('change_camel.html', post=new_dict)
    elif request.method == 'POST':
        pk = request.form.get('pk')
        breed = request.form['breed'].strip()
        gender = request.form['gender'].strip()
        age = request.form['age'].strip()
        weight = request.form['weight'].strip()
        nature = request.form['nature'].strip()
        price = request.form['price'].strip()
        con = mysql.connector.connect(
            host='localhost',
            user='Abuka',
            password='Takanashi_13',
            database='animals'
        )
        cursor = con.cursor()

        cursor.execute(
            """UPDATE camel SET breed = %s, gender = %s, age = %s, weight = %s, nature = %s, price = %s WHERE id = %s""",
            (breed, gender, age,weight,nature,price, pk)
        )

        con.commit()

        cursor.close()
        con.close()
        return redirect(url_for('buy_camels'), 301)

@app.route("/deletecamel", methods=["GET"])
def delete_camel():
    """Удаляет существующую публикацию"""

    pk = request.args.get('pk', default=0, type=int)

    con = mysql.connector.connect(
        host='localhost',
        user='Abuka',
        password='Takanashi_13',
        database='animals'
    )
    cursor = con.cursor()

    cursor.execute("DELETE FROM camel WHERE id = %s", (pk,))

    con.commit()

    cursor.close()
    con.close()

    return redirect(url_for('buy_cats'), 301)


@app.route('/sellcat', methods=['GET', 'POST'])  # TODO Create (POST) [INSERT] Страница формой для создания книг
def create_cat():
    if request.method == "GET":
        return render_template('create_cat.html')
    elif request.method == "POST":

        breed = request.form['breed'].strip()
        color = request.form['color'].strip()
        age = request.form['age'].strip()
        weight = request.form['weight'].strip()
        nature = request.form['nature'].strip()
        price = request.form['price'].strip()
        con_cat = mysql.connector.connect(
            host='localhost',
            user='Abuka',
            password='Takanashi_13',
            database='animals'
        )
        cursor = con_cat.cursor()
        cursor.execute("INSERT INTO cat (breed, color, age, weight,nature,price) VALUES (%s, %s,%s, %s, %s, %s);",
                               (breed, color, age, weight, nature, price))


        con_cat.commit()
        cursor.close()
        con_cat.close()
        return redirect(url_for('buy_cats'))
@app.route('/buycats', methods=['GET', "POST"])
def buy_cats():
    breed = request.form.get("breed", "").strip()
    con_cat = mysql.connector.connect(
        host='localhost',
        user='Abuka',
        password='Takanashi_13',
        database='animals'
    )
    cursor = con_cat.cursor()
    cursor.execute("""select id, breed, color, age, weight, nature, price from cat where breed LIKE %s""", (f"%{breed}%",))
    rows = cursor.fetchall()

    _cats = []
    for record in rows:
        new_dict = {
            "id": record[0],
            "breed": record[1],
            "color": record[2][:15:1] + "..." if len(record[2]) > 15 else record[2],
            "age": record[3],
            "weight": record[4],
            "nature": record[5],
            "price": record[6]
        }
        _cats.append(new_dict)

    cursor.close()
    con_cat.close()
    return render_template('todo_cat.html', cats=_cats, search=breed)






@app.route("/changecat", methods=["GET", "POST"])
def change_cat():
    if request.method == "GET":
        pk = request.args.get('pk', default=0, type=int)

        con = mysql.connector.connect(
            host='localhost',
            user='Abuka',
            password='Takanashi_13',
            database='animals'
        )
        cursor = con.cursor()

        cursor.execute(
            """SELECT id, breed, color, age, weight, nature, price FROM cat WHERE id = %s""",
            (pk,)
        )

        raw_row = cursor.fetchone()

        if raw_row:
            new_dict = {
                "id": raw_row[0],
                "breed": raw_row[1],
                "color": raw_row[2],
                "age": raw_row[3],
                "weight": raw_row[4],
                "nature": raw_row[5],
                "price": raw_row[6]
            }

            cursor.close()
            con.close()

            return render_template('change_cat.html', post=new_dict)
    elif request.method == 'POST':
        pk = request.form.get('pk')
        breed = request.form['breed'].strip()
        color = request.form['color'].strip()
        age = request.form['age'].strip()
        weight = request.form['weight'].strip()
        nature = request.form['nature'].strip()
        price = request.form['price'].strip()
        con = mysql.connector.connect(
            host='localhost',
            user='Abuka',
            password='Takanashi_13',
            database='animals'
        )
        cursor = con.cursor()

        cursor.execute(
            """UPDATE cat SET breed = %s, color = %s, age = %s, weight = %s, nature = %s, price = %s WHERE id = %s""",
            (breed, color, age,weight,nature,price, pk)
        )

        con.commit()

        cursor.close()
        con.close()
        return redirect(url_for('buy_cats'), 301)
@app.route("/deletecat", methods=["GET"])
def delete_cat():
    """Удаляет существующую публикацию"""

    pk = request.args.get('pk', default=0, type=int)

    con = mysql.connector.connect(
        host='localhost',
        user='Abuka',
        password='Takanashi_13',
        database='animals'
    )
    cursor = con.cursor()

    cursor.execute("DELETE FROM cat WHERE id = %s", (pk,))

    con.commit()

    cursor.close()
    con.close()

    return redirect(url_for('buy_cats'), 301)
if __name__ == '__main__':
    app.run()
