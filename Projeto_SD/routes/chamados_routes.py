from flask import Blueprint, request, jsonify
from models.chamados_model import (
    criar_chamado,
    listar_chamados,
    atualizar_status,
    deletar_chamado
)

chamados_bp = Blueprint("chamados", __name__, url_prefix="/chamados")

PRIORIDADES_VALIDAS = [
    "Baixa", 
    "Média", 
    "Alta"
    ]

STATUS_VALIDOS = [
    "Aberto",
    "Em Atendimento",
    "Concluído"
    ]


@chamados_bp.route("", methods=["POST"])
def abrir_chamado():
    dados = request.json

    if not dados:
        return jsonify({"erro": "Dados não enviados"}), 400

    titulo = dados.get("titulo")
    descricao = dados.get("descricao")
    prioridade = dados.get("prioridade")
    usuario_id = dados.get("usuario_id")

    if not all([titulo, descricao, prioridade, usuario_id]):
        return jsonify({"erro": "Campos obrigatórios não preenchidos"}), 400

    if prioridade not in PRIORIDADES_VALIDAS:
        return jsonify({"erro": "Prioridade inválida"}), 400

    chamado_id = criar_chamado(
        titulo=titulo,
        descricao=descricao,
        prioridade=prioridade,
        usuario_id=usuario_id
    )

    return jsonify({
        "mensagem": "Chamado criado com sucesso",
        "id": chamado_id
    }), 201


@chamados_bp.route("", methods=["GET"])
def listar():
    prioridade = request.args.get("prioridade")
    setor = request.args.get("setor")

    chamados = listar_chamados(prioridade, setor)

    if not chamados:
        return jsonify({"mensagem": "Nenhum chamado encontrado"}), 404

    return jsonify(chamados), 200


@chamados_bp.route("/<int:id>/status", methods=["PATCH"])
def alterar_status(id):
    dados = request.json
    novo_status = dados.get("status") if dados else None

    if not novo_status:
        return jsonify({"erro": "Status não informado"}), 400

    if novo_status not in STATUS_VALIDOS:
        return jsonify({"erro": "Status inválido"}), 400

    atualizado = atualizar_status(id, novo_status)

    if not atualizado:
        return jsonify({"erro": "Chamado não encontrado"}), 404

    return jsonify({"mensagem": "Status atualizado com sucesso"}), 200


@chamados_bp.route("/<int:id>", methods=["DELETE"])
def excluir(id):
    removido = deletar_chamado(id)

    if not removido:
        return jsonify({"erro": "Chamado não encontrado"}), 404

    return "", 204