from flask import Blueprint, request, jsonify
from models.atendimento_model import (
    criar_atendimento,
    listar_atendimentos_por_chamado,
    buscar_atendimento_por_id,
    deletar_atendimento
)

atendimentos_bp = Blueprint("atendimentos", __name__, url_prefix="/atendimentos")


@atendimentos_bp.route("", methods=["POST"])
def criar():
    dados = request.json
    if not dados:
        return jsonify({"erro": "Dados não enviados"}), 400

    descricao = dados.get("descricao")
    chamado_id = dados.get("chamado_id")

    if not all([descricao, chamado_id]):
        return jsonify({"erro": "Campos obrigatórios não preenchidos"}), 400

    atendimento_id = criar_atendimento(descricao, chamado_id)

    return jsonify({
        "mensagem": "Atendimento criado com sucesso",
        "id": atendimento_id
    }), 201


@atendimentos_bp.route("/chamado/<int:chamado_id>", methods=["GET"])
def listar_por_chamado(chamado_id):
    atendimentos = listar_atendimentos_por_chamado(chamado_id)

    if not atendimentos:
        return jsonify({"mensagem": "Nenhum atendimento encontrado"}), 404

    return jsonify(atendimentos), 200


@atendimentos_bp.route("/<int:id>", methods=["GET"])
def buscar(id):
    atendimento = buscar_atendimento_por_id(id)

    if not atendimento:
        return jsonify({"erro": "Atendimento não encontrado"}), 404

    return jsonify(atendimento), 200


@atendimentos_bp.route("/<int:id>", methods=["DELETE"])
def deletar(id):
    removido = deletar_atendimento(id)

    if not removido:
        return jsonify({"erro": "Atendimento não encontrado"}), 404

    return "", 204