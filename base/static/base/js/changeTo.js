function changeto(input) {
    // toString(input);
    let str = input.toString();
    const inputParams = str.split("-");
    let idToHide = "";
    if(inputParams[0]=='front'){
        idToHide += "back";
    }
    else{
        idToHide += "front";
    }
    idToHide += "-"+inputParams[1];
    document.getElementById(idToHide).style.display='none';
    document.getElementById(str).style.display="block";
    let inputBtn = document.getElementById(str+'-button');
    if(inputBtn.classList.contains('opacity-50')){
        // console.log(inputBtn.classList);
        
        // console.log(inputBtn.classList);
    }
    inputBtn.classList.remove('opacity-50');
    let btnToHide = document.getElementById(idToHide+'-button');
    btnToHide.classList.add('opacity-50');
    // console.log(idToHide)
}