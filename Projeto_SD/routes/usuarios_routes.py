from flask import Blueprint, request, jsonify
from models.usuario_model import (
    criar_usuario,
    listar_usuarios,
    buscar_usuario_por_id,
    atualizar_usuario,
    deletar_usuario
)

usuarios_bp = Blueprint("usuarios", __name__, url_prefix="/usuarios")


@usuarios_bp.route("", methods=["POST"])
def criar():
    dados = request.json
    if not dados:
        return jsonify({"erro": "Dados não enviados"}), 400

    nome = dados.get("nome")
    email = dados.get("email")
    setor = dados.get("setor")

    if not all([nome, email, setor]):
        return jsonify({"erro": "Campos obrigatórios não preenchidos"}), 400

    criar_usuario(nome, email, setor)
    return jsonify({"mensagem": "Usuário criado com sucesso"}), 201


@usuarios_bp.route("", methods=["GET"])
def listar():
    return jsonify(listar_usuarios()), 200


@usuarios_bp.route("/<int:id>", methods=["GET"])
def buscar(id):
    usuario = buscar_usuario_por_id(id)
    if not usuario:
        return jsonify({"erro": "Usuário não encontrado"}), 404
    return jsonify(usuario), 200


@usuarios_bp.route("/<int:id>", methods=["PUT"])
def atualizar(id):
    dados = request.json

    nome = dados.get("nome")
    email = dados.get("email")
    setor = dados.get("setor")

    if not all([nome, email, setor]):
        return jsonify({"erro": "Campos obrigatórios não preenchidos"}), 400

    atualizar_usuario(id, nome, email, setor)
    return jsonify({"mensagem": "Usuário atualizado com sucesso"}), 200


@usuarios_bp.route("/<int:id>", methods=["DELETE"])
def deletar(id):
    deletar_usuario(id)
    return "", 204