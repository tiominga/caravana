function getCsrfToken() {
        return document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    }

    function save_passageiro(){     
    let formData = new FormData(document.getElementById('form_passageiro'));
    fetch('/passageiro/save/', {    
     method: 'POST',
        headers: {
            'X-CSRFToken': getCsrfToken(),
        },
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.return === 'success') {
            liveToast('bg-success', data.message || 'Saved successfully.');           
        } else if (data.error) {
            liveToast('bg-danger', data.error);
        } else {
            liveToast('bg-warning', 'Unexpected response.');
        }
    })
    .catch(error => {
        liveToast('bg-danger', 'Network error: ' + error);
    });
}


    function delete_passageiro(){
        if (confirm('Are you sure you want to delete this record?')) {            
            let id = document.getElementById('id').value;
            fetch('/passageiro/delete/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCsrfToken(),
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ id: id })
            })
            .then(response => response.json())
            .then(data => {
                if (data.return === 'success') {
                    liveToast('bg-success', 'Deleted successfully.');                    
                } else if (data.error) {
                    liveToast('bg-danger', data.error);
                } else {
                    liveToast('bg-warning', 'Unexpected response.');
                }
            })
            .catch(error => {
                liveToast('bg-danger', 'Network error: ' + error);
            });
        }
    }
    