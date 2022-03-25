
function getUsers(){
    fetch('http://localhost:5000/users')
        .then(res =>  res.json())
        .then(data => {
            var users = document.getElementById('users');
            for( let i = 0; i < data.length; i++){
                let row = document.createElement('tr');

                let name = document.createElement('td');
                name.innerHTML = data[i].user_name;
                row.appendChild(name);
                
                let email = document.createElement('td');
                email.innerHTML = data[i].email;
                row.appendChild(email);
                users.appendChild(row);
            }
        })

}
getUsers();

$(function(){
    $('#form').on('submit',function(e){
        e.preventDefault();
        var return_form = new FormData($(this)[0]);
        fetch("http://localhost:5000/create/user", { method:'POST', body : return_form})
            .then( response => response.json() )
            .then( data => {
                
                fetch(`http://localhost:5000/users/${data}`)
                    .then( response => response.json())
                    .then( data => {
                        var users = $('#users')[0]
                        let row = document.createElement('tr');

                        let name = document.createElement('td');
                        name.innerHTML = data.user_name;
                        row.appendChild(name);
                        
                        let email = document.createElement('td');
                        email.innerHTML = data.email;
                        row.appendChild(email);
                        users.appendChild(row);
                    })

            } )
        $('#user_name').val('')
        $('#email').val('')
    });
});
