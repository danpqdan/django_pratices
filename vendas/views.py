from django.shortcuts import render, redirect, get_object_or_404
from .models import Venda, ItemVenda
from .forms import VendaForm, ItemVendaForm


def lista_vendas(request):
    vendas = Venda.objects.all()
    return render(request, "lista_vendas.html", {"vendas": vendas})


def criar_venda(request):
    if request.method == "POST":
        form = VendaForm(request.POST)
        if form.is_valid():
            venda = form.save()
            return redirect("editar_venda", venda_id=venda.num_venda)
    else:
        form = VendaForm()
        return render(request, "criar_venda.html", {"form": form})


def editar_venda(request, venda_id):
    venda = get_object_or_404(
        Venda, num_venda=venda_id
    )  # Alterado de 'id' para 'num_venda'
    itens = ItemVenda.objects.filter(venda=venda)
    if request.method == "POST":
        form = ItemVendaForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.venda = venda
            # Obtém o valor unitário do produto
            item.valor_unit = (
                item.produto.preco
            )  # Certifique-se de que 'preco' existe no modelo Produto
            # Calcula o valor total
            item.valor_total = item.valor_unit * item.quantidade
            item.save()
            # Atualiza o total da venda
            venda.total_venda = sum(i.valor_total for i in venda.itens.all())
            venda.save()
            return redirect(
                "editar_venda", venda_id=venda.num_venda
            )  # Alterado de 'id' para 'num_venda'
    else:
        form = ItemVendaForm()
        return render(
            request,
            "editar_venda.html",
            {"venda": venda, "itens": itens, "form": form},
        )


def excluir_venda(request, venda_id):
    venda = get_object_or_404(Venda, num_venda=venda_id)
    venda.delete()
    return redirect("lista_vendas")


def imprimir_venda(request, venda_id):
    venda = get_object_or_404(Venda, num_venda=venda_id)
    itens = ItemVenda.objects.filter(venda=venda)
    return render(
        request, "imprimir_venda.html", {"venda": venda, "itens": itens}
    )


def excluir_item_venda(request, item_id):
    item = get_object_or_404(ItemVenda, id=item_id)
    venda = item.venda
    item.delete()
    # Recalcula o total da venda
    venda.total_venda = sum(i.valor_total for i in venda.itens.all())
    venda.save()
    return redirect("editar_venda", venda_id=venda.num_venda)


def menu_principal(request):
    return render(request, "menu.html")
