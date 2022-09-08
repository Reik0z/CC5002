function validacion(){
    let valor = true;

    let descripcion = document.getElementById('descripcion')

    let espacio_solicitado = document.getElementById('espaciosol')
    let kilos_solicitados = document.getElementById('kilossol')

    let pais_origen = document.getElementById('pais')
    let ciudad_origen = document.getElementById('ciudad')
    let pais_destino = document.getElementById('paisdestino')
    let ciudad_destino = document.getElementById('ciudaddestino')

    let files = document.getElementById('formFileMultiple')

    let email = document.getElementById('email')
    let telefono = document.getElementById('celular')

    // patterns
    let mailformat = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
    let phoneformat = /^\+\d{11}$/;

    // Campos obligatorios
    if (!descripcion.value || descripcion.value.length > 250){
        valor = false;
        descripcion.style.borderColor = "red"
    }
    if (espacio_solicitado.value == 'Seleccionar...'){
        valor = false;
        espacio_solicitado.style.borderColor = "red"
    }
    if (!kilos_solicitados.value == 'Seleccionar...'){
        valor = false;
        kilos_solicitados.style.borderColor = "red"
    }
    if (pais_origen.value == 'Seleccionar...'){
        valor = false;
        pais_origen.style.borderColor = "red"
    }
    if (ciudad_origen.value == 'Seleccionar...'){        
        valor = false;
        ciudad_origen.style.borderColor = "red"
    }
    if (pais_destino.value == 'Seleccionar...' || pais_destino.value == pais_origen.value){
        valor = false;
        pais_destino.style.borderColor = "red"
    }
    if (ciudad_destino.value == 'Seleccionar...' || ciudad_destino.value == ciudad_origen.value){
        valor = false;
        ciudad_destino.style.borderColor = "red"
    }
    
    if (files.value.length == 0 || files.value.length > 3){
        valor = false;
        files.style.borderColor = "red"
    }

    if (!email.value){
        valor = false;
        email.style.borderColor = "red"
    }

    // Formatos
    email.style.borderColor = "#ced4da"
    if (!email.value.match(mailformat)){
        valor = false;
        email.style.borderColor = "red"
    }
    telefono.style.borderColor = "#ced4da"
    if (telefono.value != "" && !telefono.value.match(phoneformat)){
        valor = false;
        telefono.style.borderColor = "red"
    }

    return valor
}