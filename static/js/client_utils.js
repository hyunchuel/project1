var utils = (function(){

    var error = function(str){
        alert(str)
        throw new Error(str)
    }


    return {
        error : error
    }
})()