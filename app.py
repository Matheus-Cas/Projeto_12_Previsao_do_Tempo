import streamlit as st
from dados_api import previsao_temperatura

# Cidades
cidades = {
    "Santana de Parnaíba" : [-23.44678351765508, -46.91831900177454],
    "Barueri" : [-23.50799255835785, -46.880596037148734],
    "Marrakech" : [31.627871655547732, -7.998243274187909],
    "Kangerlussuaq" : [67.02646380267024, -50.28432821631744],
    "Manaus" : [-3.120196639956995, -60.0030506359003],
    "Nevada" : [39.88794459311581, -117.0297042241502]
    
}





# ------------------------- SIDEBAR
st.sidebar.title("Previsão do tempo")
st.sidebar.image("logo.png")

cidade = st.sidebar.selectbox("Escolha a cidade:", cidades.keys())
latitude , longitude = cidades[cidade]


# ------------------------- BODY
st.title(f'Previsão do tempo em {cidade} para os próximos 7 dias')

st.markdown("---")

# Previsão de temperatura
dados, temperatura_media = previsao_temperatura(latitude, longitude)


for i, d in temperatura_media.iterrows():
    # st.write(d['dia'], d['mes'], d['temperatura_media'])
    with st.container(border=True):
        st.subheader(d['dia_semana'])

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Data",f'{int(d['dia'])}/{int(d['mes'])}')

        with col2:
            st.metric("Temperatura média", f"{d['temperatura_media']:.2f}º")

        with col3:
            if d['temperatura_media'] < 10:
                temp = "cold.png"

            elif d['temperatura_media'] < 18:
                temp = "cool.png"

            elif d['temperatura_media'] < 25:
                temp = "comfort.png"

            else:
                temp = "warm.png"

            st.image(temp, width=40)

            

