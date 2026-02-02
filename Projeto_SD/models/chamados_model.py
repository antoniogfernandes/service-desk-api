from database import conectar_com_banco


def criar_chamado(titulo, descricao, prioridade, usuario_id):
    conn = conectar_com_banco()
    cursor = conn.cursor()

    sql = """
        INSERT INTO chamados (titulo, descricao, prioridade, usuario_id)
        VALUES (%s, %s, %s, %s)
    """

    cursor.execute(sql, (titulo, descricao, prioridade, usuario_id))
    conn.commit()

    chamado_id = cursor.lastrowid

    cursor.close()
    conn.close()

    return chamado_id


def listar_chamados(prioridade=None, usuario_id=None):
    conn = conectar_com_banco()
    cursor = conn.cursor(dictionary=True)

    sql = "SELECT * FROM chamados WHERE 1=1"
    params = []

    if prioridade:
        sql += " AND prioridade = %s"
        params.append(prioridade)

    if usuario_id:
        sql += " AND usuario_id = %s"
        params.append(usuario_id)

    cursor.execute(sql, params)
    chamados = cursor.fetchall()

    cursor.close()
    conn.close()

    return chamados


def atualizar_status(chamado_id, novo_status):
    conn = conectar_com_banco()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE chamados SET status = %s WHERE id = %s",
        (novo_status, chamado_id)
    )

    conn.commit()
    atualizado = cursor.rowcount > 0

    cursor.close()
    conn.close()

    return atualizado


def deletar_chamado(chamado_id):
    conn = conectar_com_banco()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM chamados WHERE id = %s",
        (chamado_id,)
    )

    conn.commit()
    removido = cursor.rowcount > 0

    cursor.close()
    conn.close()

    return removido
