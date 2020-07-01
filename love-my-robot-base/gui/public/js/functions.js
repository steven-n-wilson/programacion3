$(document).ready(function() {
    $('.say').click(function() {
        // let newFuncion = $(this).closest('#task')
        let oldName = $(this).closest("#task").clone().children().remove().end().text();
        $.post('/save-user', {funcion:oldName}, function(data, status) {
            console.log(`${data.message} and status is ${status}`)
            alert(data.message)
            setTimeout(function() {
                location.reload();
            }, 0001);
        })
        
    })
})


$(document).ready(function() {
    $('.delete').click(function() {
        let oldName = $(this).closest("#target").clone().children().remove().end().text();
        console.log(oldName);
        
        if (oldName && oldName.length > 0) {
            $.post('/delete-user', {oldtask:oldName}, function(data, status) {
                console.log(`${data.message} and status is ${status}`)
                alert(data.message)
                setTimeout(function() {
                    location.reload();
                }, 2000);
            })
        }
    })
})