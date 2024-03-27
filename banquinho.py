import sqlite3

class Database:

    def __init__(self):
        self.conn = sqlite3.connect("produtos.db", detect_types=sqlite3.PARSE_DECLTYPES)

        self.conn.row_factory = sqlite3.Row
        
        self.conn.cursor().execute('''
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                empresa TEXT,
                descricao TEXT,
                quantidade INTEGER,
                marca TEXT,
                valor FLOAT
            )
        ''')

    def query(self, sql, params=()):
        return self.conn.cursor().execute(sql, params)

    def consulta_produtos(self):
        return self.query("SELECT * FROM produtos").fetchall()

    def create_produto(self, produto):
        self.query("INSERT INTO produtos (nome, empresa, descricao, quantidade, marca, valor) VALUES(?, ?, ?, ?, ?, ?)",
            (produto["nome"], produto["empresa"], produto["descricao"], produto["quantidade"], produto["marca"], produto["valor"]))
        self.conn.commit()
        self.conn.close()

    def consulta_produtos_por_nome(self, nome):
        return self.query("SELECT * FROM produtos WHERE nome = ?", (nome,)).fetchall()
