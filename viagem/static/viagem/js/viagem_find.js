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

function viagem_find_submit(){

   const form = document.querySelector('#form_consulta_viagem');  

   fetch(URL_FIND,{
        method: "POST",
        headers: {
            "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value,
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: new URLSearchParams(new FormData(form))
    })
    .then(r => r.json())
    .then(d => resultado_consulta.innerHTML = d.tabela)
    .catch(e => resultado_consulta.innerHTML = "<p>Erro.</p>");
}





