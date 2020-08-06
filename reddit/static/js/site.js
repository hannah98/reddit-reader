$.fn.thing = function() {
    /* Returns the first thing that is a parent of the current element */
    return this.parents(".thing:first");
};
function togglecomment(e){
    var t=$(e).thing();
    n=t.find(".expand:first");
    r=t.hasClass("collapsed");
    t.toggleClass("collapsed noncollapsed");
    r?n.text("[-]"):n.text("[+]");
}
//determines if the user has a set theme
function detectColorScheme(){
    var theme="light";    //default to light

    //local storage is used to override OS theme settings
    if(localStorage.getItem("theme")){
        if(localStorage.getItem("theme") == "dark"){
            var theme = "dark";
        }
    } else if(!window.matchMedia) {
        //matchMedia method not supported
        var theme = "light";
    } else if(window.matchMedia("(prefers-color-scheme: dark)").matches) {
        //OS theme setting detected as dark
        var theme = "dark";
    }

    document.documentElement.setAttribute("data-theme", theme);
}

//function that changes the theme, and sets a localStorage variable to track the theme between page loads
function switchTheme(e) {
    if (document.documentElement.getAttribute("data-theme") == "light"){
        localStorage.setItem('theme', 'dark');
        document.documentElement.setAttribute('data-theme', 'dark');
    } else {
        localStorage.setItem('theme', 'light');
        document.documentElement.setAttribute('data-theme', 'light');
    }    
}

$( document ).ready(function() {
    detectColorScheme();
    const toggleSwitch = document.querySelector('#theme-switch');

    //listener for changing themes
    toggleSwitch.addEventListener('click', switchTheme, false);

});
