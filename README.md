# Sistema de Recomendação de Culturas Agrícolas

## Integrantes

- Matheus Machado Tamião Barbi

## Aplicação

Link da aplicação publicada no Streamlit:

https://projeto-ia-recomendacao-de-plantio.streamlit.app/

## Como executar o projeto

Instale as dependências:

```bash
pip install -r requirements.txt
```

Depois execute a aplicação com:

```bash
python -m streamlit run app.py
```

A aplicação será aberta localmente no navegador.

O arquivo `crop_model.joblib` deve permanecer na mesma pasta do `app.py`, pois ele contém o modelo treinado utilizado nas previsões.
