import streamlit as st
import streamlit.components.v1 as components
import requests

# Título da aplicação
st.title("Obter Localização do Usuário e Endereço")

# Função para converter coordenadas em endereço usando a API do Nominatim
def get_address(lat, lon):
    try:
        url = "https://nominatim.openstreetmap.org/reverse"
        params = {
            'format': 'jsonv2',
            'lat': lat,
            'lon': lon,
            'zoom': 18,
            'addressdetails': 1
        }
        headers = {'User-Agent': 'Streamlit App'}
        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data.get('display_name', 'Endereço não encontrado.')
        else:
            return f"Erro ao obter o endereço: {response.status_code}"
    except Exception as e:
        return f"Erro ao obter o endereço: {e}"

# Obtém os parâmetros da URL
query_params = st.query_params
lat = query_params.get("lat")
lon = query_params.get("lon")

# Placeholder para exibir o endereço
if lat and lon:
    try:
        latitude = float(lat[0])
        longitude = float(lon[0])
        address = get_address(latitude, longitude)
        st.success(f"📍 **Endereço:** {address}")
    except ValueError:
        st.error("Erro: Coordenadas inválidas fornecidas.")
else:
    # HTML e JavaScript para obter a localização e recarregar a página com as coordenadas
    html_code = """
        <script>
            function getLocation() {
                if (navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(
                        function(position) {
                            const latitude = position.coords.latitude;
                            const longitude = position.coords.longitude;
                            // Redireciona para a mesma página com parâmetros de consulta
                            const params = new URLSearchParams();
                            params.append("lat", latitude);
                            params.append("lon", longitude);
                            window.location.href = window.location.pathname + "?" + params.toString();
                        },
                        function(error) {
                            alert("Erro ao obter a localização: " + error.message);
                        }
                    );
                } else {
                    alert("Geolocalização não suportada neste navegador.");
                }
            }
        </script>
        <button onclick="getLocation()" style="
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            margin-top: 20px;
        ">
            📍 Obter Minha Localização
        </button>
    """
    # Exibe o HTML com o botão de geolocalização em um iframe com altura mínima
    components.html(html_code, height=200, scrolling=False)

    # Informação adicional para o usuário
    st.info("Clique no botão acima para permitir o acesso à sua localização e obter o endereço correspondente.")
