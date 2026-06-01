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










