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
    if (item.value != '') {
        item.parentNode.classList.add('highlight');
    }
    item.addEventListener('input', function() {
        var inputValue = item.value;
    
        if (inputValue.trim() !== '') {
            item.parentNode.classList.add('highlight');
        } else {
            item.parentNode.classList.remove('highlight');
        }
    });
});

document.querySelectorAll('input[type="radio"]').forEach(function(radioInput) {
    radioInput.addEventListener('input', function() {
        // Check if the radio input is checked
        if (radioInput.checked) {
            // Add highlight class to the parent label
            radioInput.parentNode.parentNode.classList.add('highlight');
        } else {
            // Remove highlight class from the parent label
            radioInput.parentNode.parentNode.classList.remove('highlight');
        }
    });
});

// document.getElementById('from_college').addEventListener('input', function(e){
//     change(this);
// })