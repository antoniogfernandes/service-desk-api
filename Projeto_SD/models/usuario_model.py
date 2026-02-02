from database import conectar_com_banco


def criar_usuario(nome, email, setor):
    conn = conectar_com_banco()
    cursor = conn.cursor()

    sql = """
        INSERT INTO usuarios (nome, email, setor)
        VALUES (%s, %s, %s)
    """

    cursor.execute(sql, (nome, email, setor))
    conn.commit()

    usuario_id = cursor.lastrowid

    cursor.close()
    conn.close()

    return usuario_id


def listar_usuarios():
    conn = conectar_com_banco()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    cursor.close()
    conn.close()

    return usuarios


def buscar_usuario_por_id(usuario_id):
    conn = conectar_com_banco()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM usuarios WHERE id = %s",
        (usuario_id,)
    )

    usuario = cursor.fetchone()

    cursor.close()
    conn.close()

    return usuario


def atualizar_usuario(usuario_id, nome, email, setor):
    conn = conectar_com_banco()
    cursor = conn.cursor()

    sql = """
        UPDATE usuarios
        SET nome = %s, email = %s, setor = %s
        WHERE id = %s
    """

    cursor.execute(sql, (nome, email, setor, usuario_id))
    conn.commit()

    atualizado = cursor.rowcount > 0

    cursor.close()
    conn.close()

    return atualizado


def deletar_usuario(usuario_id):
    conn = conectar_com_banco()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM usuarios WHERE id = %s",
        (usuario_id,)
    )

    conn.commit()

    removido = cursor.rowcount > 0

    cursor.close()
    conn.close()

    return removido


if __name__ == "__main__":
    user_id = criar_usuario("Antônio", "antonio@email.com", "TI")
    print("Usuário criado com ID:", user_id)
    print("Usuários:", listar_usuarios())
