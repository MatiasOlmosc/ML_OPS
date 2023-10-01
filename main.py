from fastapi import FastAPI
import pyarrow.parquet as pq
import pandas as pd

app = FastAPI()

# Carga los datos desde el archivo Parquet y el archivo CSV
df_items = pd.read_parquet('items.parquet')
df_games = pd.read_csv('df_games.csv')
merged_df = pd.read_csv('merged_data.csv')

@app.get("/")
async def read_root():
    return {"message": "Bienvenido a la API de Steam"}

@app.get("/PlayTimeGenre")
def read_playtime_genre(genero: str = 'Género X'):
    games_filtered = df_games[df_games['genres'].str.contains(genero, case=False, na=False)] 
    merged_df = pd.merge(df_items, games_filtered, left_on='item_id', right_on='id', how='inner')
    merged_df['release_date'] = pd.to_datetime(merged_df['release_date'])
    merged_df['release_year'] = merged_df['release_date'].dt.year
    grouped = merged_df.groupby('release_year')['playtime_forever'].sum()
    max_year = grouped.idxmax()
    return {'Launch year with more hours played by Genre': max_year}


@app.get("/UserForGenre")
def read_user_for_genre(genero: str = 'Género X'):
    result = UserForGenre(genero)
    return {"message": result}

def UserForGenre(genero: str):
    games_filtrados = df_games[df_games['genres'].str.contains(genero, case=False, na=False)]
    merged_df = pd.merge(df_items, games_filtrados, left_on='item_id', right_on='id', how='inner')
    merged_df['release_date'] = pd.to_datetime(merged_df['release_date'])
    merged_df['release_year'] = merged_df['release_date'].dt.year
    grouped = merged_df.groupby(['user_id', 'release_year'])['playtime_forever'].sum().reset_index()

    max_user = grouped.groupby('user_id')['playtime_forever'].sum().idxmax()
    horas_por_anio = grouped[grouped['user_id'] == max_user][['release_year', 'playtime_forever']].to_dict('records')

    return {
        "Usuario con más horas jugadas para Género X": max_user,
        "Horas jugadas": horas_por_anio
    }

@app.get("/UsersRecommend")
def read_users_recommend(year: int):
    result = UsersRecommend(year)
    return {"message": result}

def UsersRecommend(year: int):
    # Filtra las reseñas por el año proporcionado
    df_filtered = merged_df[merged_df['date'].str.contains(str(year), na=False)]

    # Filtra las reseñas recomendadas y con sentimiento positivo o neutral
    df_filtered = df_filtered[(df_filtered['recommend'] == True) & (df_filtered['sentiment_analysis'] >= 1)]

    # Cuenta cuántas veces se recomienda cada juego
    top_games = df_filtered['title'].value_counts().head(3)

    # Formatea los resultados en el formato deseado
    result = [{"Puesto {}".format(i + 1): game} for i, game in enumerate(top_games.index)]
    return result

@app.get("/UsersNotRecommend")
def read_users_not_recommend(year: int):
    result = UsersNotRecommend(year)
    return {"message": result}


def UsersNotRecommend(year):
    # Filtra las reseñas por el año proporcionado
    df_filtered = merged_df[merged_df['date'].str.contains(str(year), na=False)]

    # Filtra las reseñas no recomendadas y con sentimiento negativo
    df_filtered = df_filtered[(df_filtered['recommend'] == False) & (df_filtered['sentiment_analysis'] == 0)]

    # Cuenta cuántas veces no se recomienda cada juego
    top_not_recommended_games = df_filtered['title'].value_counts().head(3)

    # Formatea los resultados en el formato deseado
    result = [{"Puesto {}".format(i + 1): game} for i, game in enumerate(top_not_recommended_games.index)]
    return result

@app.get("/sentiment_analysis")
def read_sentiment_analysis(year: int):
    result = sentiment_analysis(year)
    return result

def sentiment_analysis(year):
    # Convertir la columna 'release_date' en un formato de fecha
    merged_df['release_date'] = pd.to_datetime(merged_df['release_date'])

    # Filtrar las reseñas por el año de lanzamiento
    review_year = merged_df[merged_df['release_date'].dt.year == year]
    
    # Contar la cantidad de reseñas para cada categoría de análisis de sentimiento
    count_negative = (review_year['sentiment_analysis'] == 0).sum()
    count_neutral = (review_year['sentiment_analysis'] == 1).sum()
    count_positive = (review_year['sentiment_analysis'] == 2).sum()
    
    # Crear el diccionario de resultados
    result = {
        'Negative': int(count_negative),
        'Neutral': int(count_neutral),
        'Positive': int(count_positive)
    }
    
    return result
