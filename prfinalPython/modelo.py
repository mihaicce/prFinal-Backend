import sqlite3

# Aqui hemos conectado con la base de datos
def post_cita(new_cita):
    con = sqlite3.connect("newCita.db")
    cur = con.cursor()
    values = (new_cita['id'], new_cita['nume'], new_cita['prenume'], new_cita['telefon'], new_cita['ora'], new_cita['motiv'], new_cita['data'])
    cur.execute("INSERT INTO citas (id, nume, prenume, telefon, ora, motiv, data) VALUES (?, ?, ?, ?, ?, ?, ?)", values)
    con.commit()
    con.close()
    return "********he recibido una cita"


