from connexionBDD import db_connexion

# Exécution de requêtes simples
def select_all_book():
    conn = db_connexion()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM book")  # Remplace par ta table
    results = cursor.fetchall()
    
    for row in results:
        print(row)
    
    cursor.close()
    conn.close()
