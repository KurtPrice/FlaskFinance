function addCard() {
    var list = getCards();
    var card = getSelectedCard();
    var div = document.getElementById("cardlist");

    var html = "<ul>";

    for (var i = 0; i < list.length; i++) {
        html += "<li class='cardEntry'>" + list[i] + "</li>"
    }

    html += "<li class='cardEntry'>" + card + "</li>";
    html += "</ul>";
    div.innerHTML = html;
}

function getCards() {
    var elements = document.getElementsByClassName("cardEntry")
    var list = [];

    for (var i = 0; i < elements.length; i++) {
        list.push(elements[i].innerHTML);
    }
    return list;
}

function submitGet() {
    var form = document.createElement("form");
    form.setAttribute("method", "POST");
    form.setAttribute("action", "benefits");
    var hiddenField = document.createElement("input");
    var cards = getCards();
    hiddenField.setAttribute("name", "card_list")
    hiddenField.setAttribute("value", JSON.stringify(cards));
    form.appendChild(hiddenField);
    document.body.appendChild(form);
    form.submit()
}

function getSelectedCard() {
    var cardselector = document.getElementById("cards_selector");
    return cardselector[cardselector.selectedIndex].text;
}