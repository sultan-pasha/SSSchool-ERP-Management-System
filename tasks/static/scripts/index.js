$(document).ready(
    function(){
        $(".message").click(function(){
            $(this).hide(1000)
        });
    }
);
let navbar = document.querySelector(".navbar");
let body = document.querySelector("body");
let img = document.querySelector("#brandimg");
let btnnav = document.querySelector(".navbar-toggler");
let navcollapse = document.querySelector(".navbar-collapse ");
let lastscroll = 0;

document.addEventListener('scroll',

function navHide(){
    let cscro = document.documentElement.scrollTop || document.body.scrollTop; // Get Current Scroll Value
    if(cscro > 0 && lastscroll <= cscro && window.screen.availHeight > 1000){
        lastscroll = cscro;
        navbar.style.cssText = 'height: 42px; position: fixed; top:0; left: 0; right: 0; background-color:#212529!important; padding:0';
        img.style.cssText = 'width: 100px;';
        body.style.cssText="padding-top:65px; overflowY:scroll";
        navcollapse.classList.remove("show");
    }
    else if(cscro > 0 && lastscroll <= cscro && window.screen.availHeight < 1000 && navcollapse.classList[2]=="show"){
        lastscroll = cscro;
        navbar.style.cssText = 'height: 100vh; width=100vh; position: fixed; top:0; overflow:scroll;';
    }
    else if(cscro > 0 && lastscroll <= cscro && navcollapse.classList[2]!="show"){
        lastscroll = cscro;
        navbar.style.cssText = 'height: 42px; position: fixed; top:0; left: 0; right: 0; background-color:#212529!important; padding:0';
        img.style.cssText = 'width: 100px;';
        body.style.cssText="padding-top:65px; overflowY:scroll";
        navcollapse.classList.remove("show");
    }
    else if(cscro < 5){
        navbar.style.cssText = 'height: auto; position: auto;';
        img.style.cssText = 'width: 200px;';
        body.style.cssText="padding-top:0px; overflowY:scroll";
    }
    else if(cscro > 0 && lastscroll-180 >= cscro && window.screen.availHeight > 1000){
        lastscroll=cscro
        navbar.style.cssText = 'height: auto; position: fixed; top:0;';
        img.style.cssText = 'width: 200px;';
        body.style.cssText="padding-top:0px; overflowY:scroll";
    }
}
)

btnnav.addEventListener('click',
    function(){
        navbar.style.cssText = 'height: auto; position: fixed; top:0;';
        img.style.cssText = 'width: 200px;';
        body.style.cssText="padding-top:0px; overflowY:scroll";
        lastscroll = 0;
    }
)