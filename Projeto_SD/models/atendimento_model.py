from database import conectar_com_banco


def criar_atendimento(descricao, chamado_id):
    conn = conectar_com_banco()
    cursor = conn.cursor()

    sql = """
        INSERT INTO atendimentos (descricao, chamado_id)
        VALUES (%s, %s)
    """

    cursor.execute(sql, (descricao, chamado_id))
    conn.commit()

    atendimento_id = cursor.lastrowid

    cursor.close()
    conn.close()

    return atendimento_id


def listar_atendimentos_por_chamado(chamado_id):
    conn = conectar_com_banco()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM atendimentos WHERE chamado_id = %s",
        (chamado_id,)
    )

    atendimentos = cursor.fetchall()

    cursor.close()
    conn.close()

    return atendimentos


def buscar_atendimento_por_id(atendimento_id):
    conn = conectar_com_banco()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM atendimentos WHERE id = %s",
        (atendimento_id,)
    )

    atendimento = cursor.fetchone()

    cursor.close()
    conn.close()

    return atendimento


def deletar_atendimento(atendimento_id):
    conn = conectar_com_banco()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM atendimentos WHERE id = %s",
        (atendimento_id,)
    )

    conn.commit()
    removido = cursor.rowcount > 0

    cursor.close()
    conn.close()

    return removido
