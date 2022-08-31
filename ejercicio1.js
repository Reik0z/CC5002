// Ejercicio 1
function validacion(){

    let validacion = true;

    let errores = '';
    let caja_errores = document.getElementById('contenedorErrores');

    let nombre = $('#inputNombre');
    let comentarios = $('#inputComentario');
    let direccion = $('#inputDireccion');
    // let pizza = document.getElementById('inputPizza')

    let telephone = document.getElementById('phone');
    let regex_phone = /^\+\d{11}$/;

    // LARGO DE COSAS
    if (nombre.val().length < 5){
        errores += '<p> El nombre es demasiado corto. </p>'
        validacion = false;
        document.getElementById('inputNombre').style.borderColor = "red"
    } else{
        validacion = true;
        document.getElementById('inputNombre').style.borderColor = "#ced4da"
    }

    if (nombre.val().length > 100){
        errores += '<p> El nombre es demasiado largo. </p>'
        validacion = false;
        document.getElementById('inputNombre').style.borderColor = "red"
    }

    if (comentarios.val().length >= 1000){
        errores += '<p> Comentario excede el límite de 1000 caracteres. </p>'
        validacion = false;
        document.getElementById('inputComentarios').style.borderColor = "red"
    }

    if (direccion.val().length < 5){
        errores += '<p> La dirección es demasiado corta. </p>'
        validacion = false;
        document.getElementById('inputDireccion').style.borderColor = "red"
    } else{
        validacion = true;
        document.getElementById('inputDireccion').style.borderColor = "#ced4da"
    }

    if (direccion.val().length > 100){
        errores += '<p> La dirección es demasiado larga. </p>'
        validacion = false;
        document.getElementById('inputDireccion').style.borderColor = "red"
    }

    // ERROR EN TELEFONO
    if (!regex_phone.test(phone.value)){
        errores += '<p> Telefono incorrecto. </p>'
        validacion = false;
        document.getElementById('phone').style.borderBlockColor = "red"
    }

    // CAMPOS OBLIGATORIOS
    if (!nombre){
        errores += '<p> Tiene que ingresar su nombre </p>'
        validacion = false; 
        document.getElementById('inputNombre').style.borderColor = "red"
    }

    if (!telephone){ // NOSE?
        errores += '<p> Tiene que ingresar su teléfono. </p>'
        validacion = false; 
        document.getElementById('phone').style.borderColor = "red"
    }

    if (!direccion){
        errores += '<p> Tiene que ingresar su dirección. </p>'
        validacion = false; 
        document.getElementById('inputDireccion').style.borderColor = "red"
    }

    caja_errores.innerHTML = errores;
    return validacion
}