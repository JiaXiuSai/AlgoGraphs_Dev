// form check and outputs userInput in a string
const inputForm = document.getElementById('userInputForm');
inputForm.addEventListener('submit', function (event) {
    try {
        // stop default form action (client-side)
        event.preventDefault();
        var radios = document.getElementsByName('Radio');
        // find and record check radio value
        for (var i = 0, length = radios.length; i < length; i++) {
            if (radios[i].checked) {
                graph = radios[i].value
                break
            }
        }
        // TODO: Implement some type of check to ensure the backend can compute it
        var example = document.getElementById('example').value;
        var nodes = document.getElementById('nodes').value;
        var algorithms = document.getElementById('algorithms').value;
        userInput = [graph,example,nodes,algorithms]
        alert(userInput)
    } catch (error) {
        window.alert(error);
    }
});