function validacion(){
    var valor = true;

    let pais_origen = document.getElementById('pais')
    let ciudad_origen = document.getElementById('ciudad')
    let pais_destino = document.getElementById('paisdestino')
    let ciudad_destino = document.getElementById('ciudaddestino')

    let fecha_ida = document.getElementById('fechaida')
    let fecha_regreso = document.getElementById('fecharegreso')

    let espacio_disponible = document.getElementById('espaciodisp')
    let kilos_disponibles = document.getElementById('kilosdisp')

    let email = document.getElementById('email')
    let telefono = document.getElementById('celular')

    // patterns
    let mailformat = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
    let phoneformat = /^\+\d{11}$/;
    let dateformat = /([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))$/;

    // Campos obligatorios
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
    if (!fecha_ida){
        valor = false;
        fecha_ida.style.borderColor = "red"
    }
    if (!fecha_regreso){
        valor = false;
        fecha_regreso.style.borderColor = "red"
    }
    if (espacio_disponible.value == 'Seleccionar...'){
        valor = false;
        espacio_disponible.style.borderColor = "red"
    }
    if (!kilos_disponibles.value == 'Seleccionar...'){
        valor = false;
        kilos_disponibles.style.borderColor = "red"
    }
    if (!email){
        valor = false;
        email.style.borderColor = "red"
    }

    // Formatos
    fecha_ida.style.borderColor = "#ced4da"
    if (!fecha_ida.value.match(dateformat)){
        valor = false;
        fecha_ida.style.borderColor = "red"
    }    
    fecha_regreso.style.borderColor = "#ced4da"
    if (!fecha_regreso.value.match(dateformat)){
        valor = false;
        fecha_regreso.style.borderColor = "red"
    }
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

    // fechas distintas REVISAR
    if (fecha_ida.value <= fecha_regreso.value){
        valor = false;
        fecha_ida.style.borderColor = "red"
        fecha_regreso.style.borderColor = "red"
    }

    return valor
}