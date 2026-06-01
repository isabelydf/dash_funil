"""Dashboard Automático - Funil de Vendas
Importa até 5 planilhas CSV/XLSX e gera análises e insights automáticos.
Compatível com Google Sheets exportado como CSV ou XLSX.
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import os
import io
import base64
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")


# Dicionário de tradução e um guia de estilo
# Mapeamento de colunas comuns para padronização

COLUMN_MAP= {

    'data': ['data', 'date', 'dt'],
    'supervisor': ['supervisor', 'supervisora'],
    'consultor': ['consultor', 'vendedor'],
    'lead': ['lead', 'leads'],
    'prioridade': ['prioridade'],
    'repasse': ['repasse'],
    'cliente': ["nome do cliente", "cliente", "customer", "nome_cliente", "nome cliente"],
    'telefone': ['telefone', 'celular', 'contato'],
    'status': ['status', 'etapa', 'fase'],
    'etapa': ['etapa', 'fase'],
    'categoria': ['categoria', 'tipo']
}

STATUS_COLORS = {
    'venda': '#02f66c',
    'negociação': '#59b6b1',
    'tratativa': '#59b6b1',
    'prospecção': '#59b6b1',
    'aguardando dados': '#59b6b1',
    'analise realizada': '#6ce175',
    'quer emprestimo': '#e74c3c',
    'sem interesse': '#e74c3c',
    'não localizado': '#e74c3c',
    'tel.inválido': '#e74c3c',
    'bloqueado': '#e74c3c',
    'sem financiamento': '#e74c3c',
    'parcelas baixas': '#e74c3c',
    'outra assessoria/reclame aqui': '#e74c3c'
}

