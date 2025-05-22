    //constantes url_origem e destino no viagem_find.html para usar o namespace e evitar hardcoded
document.addEventListener("DOMContentLoaded", function() {

    fetch(URL_ORIGEM)  
        .then(response => response.text())
        .then(data => {
            document.getElementById('origem').innerHTML = data;
            
    });

    fetch(URL_DESTINO)  
        .then(response => response.text())
        .then(data => {
            document.getElementById('destino').innerHTML = data;
    }); 
});       