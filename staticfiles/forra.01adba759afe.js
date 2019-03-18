window.onload = function() {
    // loop if in the url there is the anchor to highlight
    splitted_url = window.location.href.split('#');
    // if there is it, go to the section defined
    if(splitted_url.length == 2) {
        switch_section(splitted_url[1]);
    } else {
        switch_section('Dati')
    }

}

function switch_section(id) {

    // Switch active section

    var e = document.getElementById(id);

    // something might go wrong and the id does not exist.
    // in this case, simply show the data section and nothing should break
    if(!e) {
        switch_section('Dati');
        return;
    }

    var els = document.getElementsByClassName("section");

    for(var i=0; i<els.length; ++i) {
        els[i].style.display = "none";
    }

    e.style.display = "";

    // Switch active section link in navbar

    var name = "Link-".concat(id);
    var link = document.getElementById(name);
    var ls = document.getElementsByClassName("nav-link");

    for(var i=0; i<ls.length; ++i) {
        ls[i].classList.remove("bg-primary");
    }

    link.classList.add("bg-primary");
}
