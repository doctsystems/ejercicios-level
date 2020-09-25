$("#persona-form").submit(function(e){
	e.preventDefault();
	var _url = $("#Url").attr("data-url");
    var serializedData=$(this).serialize();
    $.ajax({
        type: 'POST',
        url: _url,
        dataType: 'json',
        data: serializedData,
        success: function(response){
            $("#persona-form").trigger('reset');
            $("#id_nombre").focus();

            var instance=JSON.parse(response["instance"]);
            var fields=instance[0]["fields"];
            var id=instance[0]["pk"];
            $("#personas tbody").prepend(
                `<tr>
                <th scope="row"> ${id}</th>
                <td> ${fields["nombre"]}</td>
                <td> ${fields["email"]}</td>
                <td> ${fields["kms"]}</td>
                </tr>`
            )
        },
		error: function(e){
			console.log(e)
			if (e.responseJSON.error.email)
				alert(e.responseJSON.error.email);
			if (e.responseJSON.error.__all__)
				alert(e.responseJSON.error.__all__);
		}
    });
})