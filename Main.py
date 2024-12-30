import streamlit as st
import streamlit.components.v1 as components

st.title("Obter Localização do Usuário")

# Código JavaScript para obter a localização
html_code = """
    <script>
        function getLocation() {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(
                    function(position) {
                        const latitude = position.coords.latitude;
                        const longitude = position.coords.longitude;
                        document.getElementById("output").value = `Latitude: ${latitude}, Longitude: ${longitude}`;
                    },
                    function(error) {
                        document.getElementById("output").value = "Erro ao obter a localização: " + error.message;
                    }
                );
            } else {
                document.getElementById("output").value = "Geolocalização não suportada neste navegador.";
            }
        }
    </script>
    <button onclick="getLocation()">Obter Localização</button>
    <br><br>
    <input type="text" id="output" style="width: 100%; height: 50px;" readonly />
"""

# Exibir o código HTML no Streamlit
components.html(html_code)
