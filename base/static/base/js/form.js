function checkInputValue(item) {
    var inputValue = item.value;
    
    if (inputValue.trim() !== '') {
        item.parentNode.classList.add('highlight');
    } else {
        item.parentNode.classList.remove('highlight');
    }
}
function change(item) {
    var inputValue = item.value;
    
    if (inputValue.trim() == 'No') {
        item.parentNode.parentElement.parentElement.classList.add('clg');
        item.parentNode.parentElement.parentElement.classList.remove('out');
    } else {
        item.parentNode.parentElement.parentElement.classList.add('out');
        item.parentNode.parentElement.parentElement.classList.remove('clg');
    }
}

const inputs = document.querySelectorAll('input[type="text"], input[type="email"] , select' );

inputs.forEach(function(item, index) {
    item.addEventListener('input', function() {
        checkInputValue(item);
    });
});

document.getElementById('from_college').addEventListener('input', function(e){
    change(this);
})