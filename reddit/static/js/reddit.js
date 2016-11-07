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
$( document ).ready(function() {
});
