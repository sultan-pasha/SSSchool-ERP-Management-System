var brand = document.querySelector('.nav-brand'),
    nav = document.querySelector('nav'),
    navbtn = document.querySelector('.navbtn');
    if (brand != null) {
        brand.addEventListener('click', function () {
            (nav.style.display = 'none'), (navbtn.style.display = 'inline');
        })
    }
    navbtn.addEventListener('click', function () {
        (nav.style.display = 'flex'), (navbtn.style.display = 'none');
    });

var bar = document.getElementById('serachInput');
var box = document.getElementById('searchBox');

bar.addEventListener('focus', function () {
    box.style.display = 'initial';
});
bar.addEventListener('keyup', function (e) {
    if (e.key == 'Enter') {
        window.location = window.location.origin + window.location.pathname + '?q=' + e.target.value;
    }
});
document.getElementsByClassName('main')[0].addEventListener('click', function () {
        box.style.display = 'none';
    });
document.getElementsByClassName('container')[0].addEventListener('click', function () {
    box.style.display = 'none';
});
