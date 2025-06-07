

function alredy_selected(){

    var form = document.getElementById('form_poltrona');       
        fetch(form.action,{
        method: 'POST',
        body: new FormData(form)
    })
        .then(res => res.json())
        .then(data => {           
            liveToast(data.bg, data.message);
            if (data.redirect != 'None'){

                setTimeout(function() {
                window.location.href = data.redirect;
                }, 2000);

            } 

           
    });

}   
    

